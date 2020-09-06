import pandas as pd

def get_air_quality():
  return pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
