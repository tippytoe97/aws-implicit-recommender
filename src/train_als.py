import pandas as pd
import numpy as np
from scipy.sparse import coo_matrix
from implicit.als import AlternatingLeastSquares

df = pd.read_csv("interactions.csv")

#encode user/item
user_ids = df['user_id'].astype("category").cat.codes
item_ids = df['item_id'].astype("category").cat.codes

#build sparse matrix
matrix = coo_matrix((df['interaction'], (user_ids, item_ids)))

#initialize ALS model
model = AlternatingLeastSquares(factors = 50, regularization = 0.1, iterations=10)

#train model
model.fit(matrix.T)

user_idx = 0
recommendations = model.recommend(user_idx, matrix)




