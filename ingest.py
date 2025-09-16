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
coingecko_key = os.getenv("COINGECKO_KEY")


db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
    database=db_name
)

table_name = "projeto"

baseurl = "https://api.coingecko.com/api/v3"
headers = {'x-cg-demo-api-key': coingecko_key}

for i in range(10):
    engine = create_engine(db_url)


    #Cria tabela se não estiver criada
    create_table_query = text("""
        CREATE TABLE IF NOT EXISTS projeto (
            id SERIAL PRIMARY KEY,
            name VARCHAR(64),
            unit VARCHAR(16),
            value DECIMAL,
            type VARCHAR(16),
            insertion_date TIMESTAMPTZ DEFAULT NOW()
        )
    """)

    with engine.begin() as connection:
        connection.execute(create_table_query)
      #  connection.commit()
        print("Table 'projeto' is ready.")

    r = requests.get(baseurl + "/exchange_rates", headers=headers)

    #Acessa o objeto rates e transpõe os dados para ficar no formato de tabela com colunas tradicional

    df = pd.DataFrame(r.json()['rates']).T

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='append',
        index=False
    )

    time.sleep(10)

    #descomentar para gerar arquivos locais
    #df.to_csv("output"+ i + ".csv", index=False)