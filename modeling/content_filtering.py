import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from config.helper_functions import book_data_reading
book_data, img_data = book_data_reading()

class ContentRecommender:

    def __init__(self, new_items, df_path=book_data, img_df_path=img_data):

        self.new_item = new_items
        self.df_path = df_path
        self.img_df_path = img_df_path

    def preprocess_dataframe(self):
        df = pd.read_csv(self.df_path, index_col=0)
        imgs = pd.read_csv(self.img_df_path, index_col=0)

        df = pd.merge(df, imgs, on='ad', how='inner')
        df.drop_duplicates(keep=False, inplace=True)
        df.reset_index(drop=True, inplace=True)
        self.df = df.apply(lambda x: x.str.lower() if (x.dtype == 'object') else x)

        return self.df

    def _generate_candidate_df(self):
        self.df = self.preprocess_dataframe()
        self.df = self.df[(self.df['janr'] == self.new_item[0]) & ((self.df['kolleksiya'] == self.new_item[-1]))]
        self.df = self.df.reset_index(drop=True)
        self.imgs = self.df[['ad', 'foto']]
        self.df.drop(['foto'], axis=1, inplace=True)
        return self.df

    def _calculate_new_item_similarity(self):

        self.df = self._generate_candidate_df()
        self.df.loc[len(self.df.index)] = self.new_item
        self.df['combined'] = self.df.iloc[:, :-1].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
        documents = self.df['combined']
        count_vectorizer = CountVectorizer()
        sparse_matrix = count_vectorizer.fit_transform(documents)
        scores_df = cosine_similarity(sparse_matrix, sparse_matrix)
        scores_df = pd.DataFrame(scores_df)
        return scores_df

    def recommend(self):

        scores_df = self._calculate_new_item_similarity()
        self.recommended = []
        title = self.new_item[-3]
        title = title.lower()
        self.df['ad'] = self.df['ad'].str.lower()
        index = self.df[self.df['ad'] == title].index[0]

        top10_list = list(scores_df.iloc[index].sort_values(ascending=False).iloc[1:5].index)

        for each in top10_list:
            self.recommended.append(self.df.iloc[each].ad)
        return self.recommended

    def show_images(self):

        if len(self.recommended) > 0:
            for i in self.recommended:
                photo_url = self.imgs['foto'][self.imgs.ad == i].values[0]
                print(photo_url)


