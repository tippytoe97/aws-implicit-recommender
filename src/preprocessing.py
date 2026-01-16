import json
import pandas as pd
from pathlib import Path

#turn json data into pd DataFrame with only nesscery columns
#/ VS \ ?
DATA_PATH = Path('data/raw/Electronics_5.json')

records = []
with DATA_PATH.open("r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        review = json.loads(line)
        records.append({
            "user": review["reviewerID"],
            "item": review["asin"],
            "verified": review.get("verified", False),
            "timestamp": review["unixReviewTime"]
        })

df = pd.DataFrame(records)

#what the nunique() does?
print("Num interactions:", len(df))
print("Num users:", df["user"].nunique())
print("Num items:", df["item"].nunique())

#reduce data size
df = df.sort_values("timestamp")
#only keep the most recent interactions
df = df.tail(200_000) #what is 200_000?

#save cleaned data
OUTPUT_PATH = Path('data/processed/interactions.csv')
OUTPUT_PATH.parent.mkdir(parents = True, exist_ok= True) #what is this parent function/method?

print(df.head())

df.to_csv(OUTPUT_PATH, index=False)