import pandas as pd
from scipy.sparse import coo_matrix

df = pd.read_csv('data/processed/interactions.csv')

#encode users and items
user_ids = {user: idx for idx, user in enumerate(df["user"].unique())}
item_ids = {item: idx for idx, item in enumerate(df["item"].unique())}

#add integer columns
df["user_id"] = df["user"].map(user_ids)
df["item_id"] = df["item"].map(item_ids)

df["weight"] = 1 + df["verified"].astype(int)
#create sparse matrix
interaction_matrix = coo_matrix(
    (df["weight"], (df["item_id"], df["user_id"]))
    )

print("Sparse matrix shape:", interaction_matrix.shape)
print("Number of non-zero entries:", interaction_matrix.nnz)

#Popularity per item
item_popularity = df.groupby("item_id")["weight"].sum().sort_values(ascending=False)
top_items = item_popularity.head(10).index.tolist()

print("Top 10 popular item (IDs):", top_items)
print(df.head())

'''
interaction is defined as a user reviewing a product. 
I treat reviews as implicit positive feedback, and verified purchases are modeled as higher-confidence interactions. 
Absence of interaction is treated as unknown rather than negative.
'''