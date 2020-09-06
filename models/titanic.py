import pandas as pd

def get_titanic():
  return pd.read_csv("data/titanic.csv")

def get_all_passengers():
  return get_titanic().to_dict(orient="records")

def get_passenger(id):
  df = get_titanic()
  passenger = df[df["PassengerId"] == id].to_dict(orient="records")[0]
  return passenger
