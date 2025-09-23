import os
import requests
import time
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name
)

engine = create_engine(db_url)

df = pd.read_csv('/home/daniel/Projetos/CoinGecko-PostgreSQL/currency_metadata.csv')

df.to_sql(
        name="currency_metadata",
        con=engine,
        if_exists='replace',
        index=False
)

with engine.connect() as conn:
    conn.execute(text("""
    ALTER TABLE currency_metadata
    ADD CONSTRAINT currency_metadata_pkey PRIMARY KEY (unit);  
    """))
    conn.execute(text("""
    ALTER TABLE projeto
    ADD CONSTRAINT projeto_unit_fkey FOREIGN KEY(unit) REFERENCES currency_metadata(unit);
    """))
    conn.commit()
    conn.close()