import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os

headers = []
data_types = []

def extract():
    global headers, data_types

    url = 'HealthCareAnalysis/data/rawData/MUP_DPR_RY24_P04_V10_DY22_NPIBN.csv'
    chunkSize = 500000
    dataTypes = {
        "Prscrbr_NPI": "Int64",
        "Prscrbr_Last_Org_Name": "str",
        "Prscrbr_First_Name": "str",
        "Prscrbr_City": "str",
        "Prscrbr_State_Abrvtn": "str",
        "Prscrbr_Type": "str",
        "Brnd_Name": "str",
        "Gnrc_Name": "str",
        "Tot_Clms": "Int64",
        "Tot_30day_Fills": "float",
        "Tot_Day_Suply": "Int64",
        "Tot_Drug_Cst": "float",
        "Tot_Benes": "Int64",
        "GE65_Tot_Clms": "Int64",
        "GE65_Tot_30day_Fills": "float",
        "GE65_Tot_Drug_Cst": "float",
        "GE65_Tot_Day_Suply": "Int64",
        "GE65_Tot_Benes": "Int64"
    }

    dropColumns = ["Prscrbr_State_FIPS", "Prscrbr_Type_Src", "GE65_Sprsn_Flag", "GE65_Bene_Sprsn_Flag"]
    keepColumns = [x for x in dataTypes if x not in dropColumns]

    int_columns = ["Prscrbr_NPI", "Tot_Clms", "Tot_Day_Suply", "Tot_Benes",
                   "GE65_Tot_Clms", "GE65_Tot_Day_Suply", "GE65_Tot_Benes"]

    chunks = pd.read_csv(url, chunksize=chunkSize, dtype=dataTypes, usecols=keepColumns, na_values=["", "NA", "NaN"])
    headers = chunks.get_chunk(0).columns.to_list()

    chunkCount = 1

    for chunk in chunks:
        # Replace pd.NA or None with a consistent representation (e.g., None) for string columns
        for col in chunk.columns:
            if dataTypes[col] == "str":
                chunk[col] = chunk[col].where(chunk[col].notna(), None)

        # Drop rows where any integer column has NA (None)
        chunk = chunk.dropna(subset=int_columns)

        # Save to CSV without headers
        outputFile = f'HealthCareAnalysis/data/processedData/processedData_{chunkCount}.csv'
        chunk.to_csv(outputFile, mode='w', header=False, index=False)
        chunkCount += 1

def Load():
    """Load the processed CSV files into a PostgreSQL database."""
    load_dotenv()
    db_params = {
        "dbname": os.environ.get("DB_NAME"),
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASSWORD"),
        "host": os.environ.get("DB_HOST"),
        "port": os.environ.get("DB_PORT")
    }

    table_name = "cms"

    column_definitions = {
        "Prscrbr_NPI": "INTEGER",
        "Prscrbr_Last_Org_Name": "TEXT",
        "Prscrbr_First_Name": "TEXT",
        "Prscrbr_City": "TEXT",
        "Prscrbr_State_Abrvtn": "TEXT",
        "Prscrbr_Type": "TEXT",
        "Brnd_Name": "TEXT",
        "Gnrc_Name": "TEXT",
        "Tot_Clms": "INTEGER",
        "Tot_30day_Fills": "FLOAT",
        "Tot_Day_Suply": "INTEGER",
        "Tot_Drug_Cst": "FLOAT",
        "Tot_Benes": "INTEGER",
        "GE65_Tot_Clms": "INTEGER",
        "GE65_Tot_30day_Fills": "FLOAT",
        "GE65_Tot_Drug_Cst": "FLOAT",
        "GE65_Tot_Day_Suply": "INTEGER",
        "GE65_Tot_Benes": "INTEGER"
    }

    headers = [
        "Prscrbr_NPI", "Prscrbr_Last_Org_Name", "Prscrbr_First_Name", "Prscrbr_City",
        "Prscrbr_State_Abrvtn", "Prscrbr_Type", "Brnd_Name", "Gnrc_Name", "Tot_Clms",
        "Tot_30day_Fills", "Tot_Day_Suply", "Tot_Drug_Cst", "Tot_Benes", "GE65_Tot_Clms",
        "GE65_Tot_30day_Fills", "GE65_Tot_Drug_Cst", "GE65_Tot_Day_Suply", "GE65_Tot_Benes"
    ]

    dataTypes = {
        "Prscrbr_NPI": "Int64",
        "Prscrbr_Last_Org_Name": "str",
        "Prscrbr_First_Name": "str",
        "Prscrbr_City": "str",
        "Prscrbr_State_Abrvtn": "str",
        "Prscrbr_Type": "str",
        "Brnd_Name": "str",
        "Gnrc_Name": "str",
        "Tot_Clms": "Int64",
        "Tot_30day_Fills": "float",
        "Tot_Day_Suply": "Int64",
        "Tot_Drug_Cst": "float",
        "Tot_Benes": "Int64",
        "GE65_Tot_Clms": "Int64",
        "GE65_Tot_30day_Fills": "float",
        "GE65_Tot_Drug_Cst": "float",
        "GE65_Tot_Day_Suply": "Int64",
        "GE65_Tot_Benes": "Int64"
    }

    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        print("Connected to PostgreSQL database.")

        create_table_query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
            sql.Identifier(table_name),
            sql.SQL(", ").join(
                sql.SQL("{} {}").format(sql.Identifier(col), sql.SQL(dtype))
                for col, dtype in column_definitions.items()
            )
        )
        cur.execute(create_table_query)
        conn.commit()
        print(f"Table '{table_name}' created or already exists.")

        chunkCount = 1
        while True:
            csv_file = f'HealthCareAnalysis/data/processedData/processedData_{chunkCount}.csv'
            try:
                df = pd.read_csv(csv_file, names=headers, dtype=dataTypes)
                rows = [tuple(row) for index, row in df.iterrows()]
                insert_query = sql.SQL("INSERT INTO {} ({}) VALUES %s").format(
                    sql.Identifier(table_name),
                    sql.SQL(", ").join(map(sql.Identifier, headers))
                )
                execute_values(cur, insert_query, rows)
                conn.commit()
                print(f"Loaded chunk {chunkCount} from {csv_file} into database.")
                chunkCount += 1
            except FileNotFoundError:
                print(f"No more files found after chunk {chunkCount - 1}. Loading complete.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()

    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
        print("Database connection closed.")

def main():
    extract()
    Load()

if __name__ == "__main__":
    main()