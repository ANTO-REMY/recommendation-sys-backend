
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

class Recommender:
    def __init__(self, data_path=None):
        if data_path is None:
            data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'interactions.csv')
        self.data_path = data_path
        self.user_item_matrix = None
        self.similarity_matrix = None
        self.users = None
        self.items = None
        self._load_data()

    def _load_data(self):
        # Load interactions.csv: columns = user_id, item_id, rating
        try:
            df = pd.read_csv(self.data_path)
        except Exception:
            self.user_item_matrix = pd.DataFrame()
            self.similarity_matrix = None
            self.users = []
            self.items = []
            return
        if df.empty:
            self.user_item_matrix = pd.DataFrame()
            self.similarity_matrix = None
            self.users = []
            self.items = []
            return
        self.user_item_matrix = df.pivot_table(index='user_id', columns='item_id', values='rating', fill_value=0)
        self.users = self.user_item_matrix.index.tolist()
        self.items = self.user_item_matrix.columns.tolist()
        self._build_similarity_matrix()

    def _build_similarity_matrix(self):
        # Compute cosine similarity between users
        if self.user_item_matrix.empty:
            self.similarity_matrix = None
            return
        self.similarity_matrix = cosine_similarity(self.user_item_matrix)

    def rebuild(self):
        self._load_data()

    def recommend(self, user_id, top_n=5):
        if self.user_item_matrix is None or self.similarity_matrix is None:
            return []
        if user_id not in self.users:
            return []
        user_idx = self.users.index(user_id)
        # Get similarity scores for the user
        sim_scores = self.similarity_matrix[user_idx]
        # Weighted sum of ratings from similar users
        user_ratings = self.user_item_matrix.values
        scores = np.dot(sim_scores, user_ratings)
        # Zero out already rated items
        already_rated = self.user_item_matrix.loc[user_id] > 0
        scores[already_rated.values] = -np.inf
        # Get top N item indices
        top_indices = np.argsort(scores)[-top_n:][::-1]
        recommended_items = [self.items[i] for i in top_indices if scores[i] != -np.inf]
        return recommended_items
