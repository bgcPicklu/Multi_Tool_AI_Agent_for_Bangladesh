import os
import pandas as pd
import sqlite3

# Ensure target directories exist
os.makedirs("databases", exist_ok=True)

def sanitize_columns(df):
    """Clean column names to make sure they play nice with SQLite syntax"""
    df.columns = df.columns.str.strip().str.replace(r'[.\s]+', '_', regex=True).str.upper()
    return df

# -----------------------------
# 1. Institutions Database
# -----------------------------
try:
    inst_df = pd.read_csv("data/InstitutionalInformation.csv")
    inst_df = sanitize_columns(inst_df)
    with sqlite3.connect("databases/institutions.db") as conn:
        inst_df.to_sql("institutions", conn, if_exists="replace", index=False)
    print("✔ institutions.db created successfully.")
except Exception as e:
    print(f"Error creating institutions database: {e}")

# -----------------------------
# 2. Hospitals Database
# -----------------------------
try:
    hospital_df = pd.read_csv("data/all-bangladesh-hospitals.csv")
    hospital_df = sanitize_columns(hospital_df)
    with sqlite3.connect("databases/hospitals.db") as conn:
        hospital_df.to_sql("hospitals", conn, if_exists="replace", index=False)
    print("✔ hospitals.db created successfully.")
except Exception as e:
    print(f"Error creating hospitals database: {e}")

# -----------------------------
# 3. Restaurants Database
# -----------------------------
try:
    restaurant_df = pd.read_csv("data/restaurants.csv")
    restaurant_df = sanitize_columns(restaurant_df)
    with sqlite3.connect("databases/restaurants.db") as conn:
        restaurant_df.to_sql("restaurants", conn, if_exists="replace", index=False)
    print("✔ restaurants.db created successfully.")
except Exception as e:
    print(f"Error creating restaurants database: {e}")

print("\nAll SQLite databases configured efficiently.")