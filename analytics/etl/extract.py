from sqlalchemy import create_engine
import pandas as pd
import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

print("ETL DATABASE_URL =", DATABASE_URL)

def extract_tasks():

    engine = create_engine(DATABASE_URL)

    query = """
        SELECT
            id,
            status,
            created_at,
            completed_at
        FROM tasks
    """


    df = pd.read_sql(
        query,
        engine
    )

    return df