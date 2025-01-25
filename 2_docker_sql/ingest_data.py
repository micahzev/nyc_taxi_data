#!/usr/bin/env python
# coding: utf-8


# if need pip
# pip install pandas==2.2.3

# pip install psycopg2

# pip install sqlalchemy

import argparse
import sys
import os
from time import time

import pandas as pd
from sqlalchemy import create_engine


def main(params):

  ITERROWS = 150000


  user = params.user
  password = params.password
  host = params.host
  port = params.port
  db = params.db
  table_name = params.table_name
  csv_url = params.csv_url

  csv_name = 'output.csv'

  os.system(f"wget {csv_url} -O {csv_name}")

  # download the csv

  engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

  # engine.connect()

  df_iter = pd.read_csv(csv_name, iterator=True, chunksize=ITERROWS)

  df = next(df_iter)

  df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
  df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

  df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

  t_start = time()
  print('starting insert!')
  df.to_sql(name=table_name, con=engine, if_exists='append')
  t_end = time()
  print(f'insert {ITERROWS} rows, took %.3f second' % (t_end - t_start))

  while True:
      t_start = time()
      df = next(df_iter)
      df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
      df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
      print('starting insert!')
      df.to_sql(name=table_name, con=engine, if_exists='append')

      t_end = time()
      
      print(f'insert {ITERROWS} rows, took %.3f second' % (t_end - t_start))




if __name__ == '__main__':
  print('ingestion started')
  parser = argparse.ArgumentParser(
                      prog='ProgramName',
                      description='Ingest CSV data to postgres')

  # user password host port dbname tablename url of csv

  parser.add_argument('--user', help="user name for postgres")
  parser.add_argument('--password', help="password for postgres")
  parser.add_argument('--host', help="host or postgres")
  parser.add_argument('--port', help="port for postgres")
  parser.add_argument('--db', help="database for postgres")
  parser.add_argument('--table_name', help="name of the table we will write our results to")
  parser.add_argument('--csv_url', help="url for the csv")

  # parser.add_argument('', help="")



  args = parser.parse_args()
  print(args.user, args.password)

  main(args)

