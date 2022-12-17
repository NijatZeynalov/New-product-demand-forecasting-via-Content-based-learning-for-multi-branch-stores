from config.helper_functions import sales_data_reading
import pytest
import pandas as pd
from pandas import Timestamp

_, sales_data = sales_data_reading()

@pytest.fixture(scope="class")
def sales_df():
  # We only want to pull this data once for each TestCase since it is an expensive operation
  df = pd.read_parquet(sales_data, engine='pyarrow')
  return df

class TestSalesData:

  def test_all_columns_present(self, sales_df):
    # ensures that the expected columns are all present
    assert "satis_tarix" in sales_df.columns
    assert "kitab_ad" in sales_df.columns
    assert "filial_id" in sales_df.columns

  def test_last_day_train(self, sales_df):
    # last date in training data
    most_recent_date = pd.to_datetime(sales_df['satis_tarix'])
    most_recent_date = max(most_recent_date)
    assert most_recent_date==Timestamp('2022-12-03 11:36:33')