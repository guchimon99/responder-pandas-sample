from models.titanic import get_titanic

def get_ages_statistics():
  titanic = get_titanic()

  return {
    "max": titanic["Age"].max(),
    "min": titanic["Age"].min(),
  }
