import pandas as pd
from sqlalchemy import create_engine

df= pd.read_csv("data/fraud_data.csv")


engine= create_engine("postgresql://postgres:postdaminisql@localhost:5432/fraud")

# Use chunked reading
chunksize = 100000  # Load 100k rows at a time

csv_path = "data/fraud_data.csv"

for i, chunk in enumerate(pd.read_csv(csv_path, chunksize=chunksize)):
    # ✅ Lowercase column names
    chunk.columns = [col.lower() for col in chunk.columns]

    # ✅ Insert into lowercase-named table
    chunk.to_sql("transactions", engine, if_exists="append", index=False)
    print(f"✅ Inserted chunk {i}")
