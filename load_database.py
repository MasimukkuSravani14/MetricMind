
import pandas as pd
import sqlite3
from pathlib import Path

# Read CSV data
df = pd.read_csv("data/sales.csv")

# Calculate profit and profit margin
df["profit"] = (
    df["revenue"]
    - df["material_cost"]
    - df["shipping_cost"]
)

df["profit_margin"] = (
    df["profit"] / df["revenue"]
) * 100

# Create SQLite database
Path("database").mkdir(exist_ok=True)

conn = sqlite3.connect("database/metricmind.db")

# Store data in database
df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

# Verify database records
result = pd.read_sql_query(
    "SELECT * FROM sales LIMIT 5",
    conn
)

print("Database created successfully!")
print("\nFirst 5 records:")
print(result)

print("\nTotal records:")
print(pd.read_sql_query(
    "SELECT COUNT(*) AS total FROM sales",
    conn
))

conn.close()
