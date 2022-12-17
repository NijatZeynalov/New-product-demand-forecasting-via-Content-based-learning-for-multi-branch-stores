import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging
logging.disable(logging.CRITICAL)
from darts.utils.likelihood_models import QuantileRegression
from darts import TimeSeries
from darts.dataprocessing.transformers import Scaler
from darts.models import TFTModel
from darts.utils.timeseries_generation import datetime_attribute_timeseries
from config.helper_functions import sales_data_reading
from config.helper_functions import sales_model_file_reading
from config.helper_functions import sales_hyperparameter_dict
import uuid

year_df, sales_df = sales_data_reading()
model_path = sales_model_file_reading()
hyperparameters = sales_hyperparameter_dict()

class TimeSeriesModeling():

    def __init__(self, book_names,n=120, sales_data=sales_df, year_data=year_df, ts_model = model_path, hp_dict = hyperparameters):

        self.n = n
        self.book_names = book_names
        self.year_data = year_data
        self.sales_data = sales_data
        self.ts_model = ts_model
        self.hyp_dict = hp_dict

    def read_and_preprocess_input_data(self):

        time_series_df = pd.read_csv(self.year_data, index_col=0)
        df = pd.read_parquet(self.sales_data, engine='pyarrow')
        df['satis_tarix'] = pd.to_datetime(df['satis_tarix']).dt.date
        self.book_df = df[df['kitab_ad'].isin(self.book_names)]

        sales_df = pd.DataFrame(self.book_df.groupby(self.book_df.satis_tarix)['kitab_ad'].count())
        sales_df.reset_index(inplace=True)
        sales_df.satis_tarix = sales_df.satis_tarix.astype(str)
        time_series_df.satis_tarix = time_series_df.satis_tarix.astype(str)

        result = pd.merge(sales_df, time_series_df, on='satis_tarix', how='right')
        result['kitab_ad'].fillna(0, inplace=True)

        result['satis_tarix'] = pd.to_datetime(result['satis_tarix'])
        self.df = result.set_index('satis_tarix')

        return self.df, self.book_df

    def time_series_data_wrangling(self):
        self.df, _ = self.read_and_preprocess_input_data()
        ts = TimeSeries.from_series(self.df["kitab_ad"])

        if isinstance(self.hyp_dict['TRAIN'], str):
            split = pd.Timestamp(self.hyp_dict['TRAIN'])
        else:
            split = self.hyp_dict['TRAIN']

        ts_train, ts_test = ts.split_after(split)
        start = ts.start_time()

        FC_HORIZ = 180
        n_per = len(ts_train) + FC_HORIZ

        ts_year = datetime_attribute_timeseries(
            pd.date_range(start=start, periods=n_per, freq="D"),
            attribute="day",
            one_hot=False)

        ts_month = datetime_attribute_timeseries(
            pd.date_range(start=start, periods=n_per, freq="D"),
            attribute="day",
            one_hot=False)

        cov = ts_year.stack(ts_month)
        cov = cov.stack(TimeSeries.from_times_and_values(
            times=cov.time_index,
            values=np.arange(n_per),
            columns=['linear_increase']))

        train_cov, test_cov = cov.split_after(split)

        scaler = Scaler()
        scaler.fit(train_cov)
        cov = cov.astype(np.float32)
        self.tcov = scaler.transform(cov)

        self.transformer = Scaler()
        ts_ttrain = self.transformer.fit_transform(ts_train)

        return self.tcov, self.transformer

    def predQ(self, ts_tpred, q):
        _, self.transformer = self.time_series_data_wrangling()

        ts_t = ts_tpred.quantile_timeseries(q)
        ts = self.transformer.inverse_transform(ts_t)
        s = TimeSeries.pd_series(ts)
        header = "Q" + format(int(q * 100), "02d")
        dfY = pd.DataFrame()
        dfY[header] = s
        return dfY

    def time_series_modeling(self):

        mpath = self.ts_model
        model = TFTModel(input_chunk_length=int(self.hyp_dict['INLEN']), output_chunk_length=int(self.hyp_dict['N_FC']), force_reset=True)
        mTFT = model.load_model(mpath)
        self.tcov, _ = self.time_series_data_wrangling()
        ts_tpred = mTFT.predict(self.n, future_covariates=self.tcov, num_samples=int(self.hyp_dict['N_SAMPLES']))

        ts_tpred.plot(low_quantile=float(self.hyp_dict['QL1']), high_quantile=float(self.hyp_dict['QU1']))
        ts_tpred.plot(low_quantile=float(self.hyp_dict['QL3']), high_quantile=float(self.hyp_dict['QU3']))
        ts_tpred.plot(central_quantile="mean", label="expected")

        quantiles = [0.5, float(self.hyp_dict['QU1']), float(self.hyp_dict['QU2']), float(self.hyp_dict['QU3']),
                     float(self.hyp_dict['QL3']), float(self.hyp_dict['QL2']), float(self.hyp_dict['QL1'])]
        dfY = [self.predQ(ts_tpred, q) for q in quantiles]
        return dfY[0]

    def result(self):

        sales_result = self.time_series_modeling().loc[self.hyp_dict['PREDICTION']:]
        sales_sum = int(sales_result['Q50'].sum())
        _, book_df = self.read_and_preprocess_input_data()

        result_df = pd.DataFrame(book_df.groupby(book_df.filial_ad)['kitab_ad'].count())
        result_df = pd.DataFrame((result_df['kitab_ad'] / result_df['kitab_ad'].sum()) * sales_sum)
        result_df['kitab_ad'] = result_df['kitab_ad'].astype('int16')
        result_df = result_df.reset_index().rename({'kitab_ad': 'kitab_say'}, axis=1)
        return result_df.to_json(force_ascii=False, orient='records')

