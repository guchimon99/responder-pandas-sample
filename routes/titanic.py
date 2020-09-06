from api_instance import api

from models.titanic import get_passenger, get_all_passengers
from models.titanic_statistics import get_ages_statistics

def buildBreadcrumbs(children = []):
  breadcrumbs = [
    { "url": "/", "label": "ホーム" },
    { "url": "/titanic", "label": "タイタニック" }
  ]

  breadcrumbs.extend(children)
  return breadcrumbs

@api.route("/titanic")
async def home (req, resp):
  resp.content = api.template(
    "pages/titanic/home.html",
    title="タイタニック",
    breadcrumbs=buildBreadcrumbs()
  )

@api.route("/titanic/passengers")
async def passngers (req, resp):
  resp.content = api.template(
    "pages/titanic/passengers.html",
    title="乗客 | タイタニック",
    breadcrumbs=buildBreadcrumbs([
      { "url": "/titanic/passengers", "label": "乗客" }
    ]),
    passengers=get_all_passengers(),
  )

@api.route("/titanic/passengers/{id}")
async def passenger (req, resp, *, id):
  passenger = get_passenger(int(id))
  name = passenger["Name"]

  resp.content = api.template(
    "pages/titanic/passenger.html",
    title="乗客 - {0} さん | タイタニック".format(name),
    breadcrumbs=buildBreadcrumbs([
      { "url": "/titanic/passengers", "label": "乗客" },
      {
        "url": "/titanic/passengers/{0}".format(id),
        "label": "{0} さん".format(name)
      },
    ]),
    passenger=passenger
  )


@api.route("/titanic/statisitics/ages")
async def passngers (req, resp):
  resp.content = api.template(
    "pages/titanic/statistics/ages.html",
    title="年齢の統計 | タイタニック",
    breadcrumbs=buildBreadcrumbs([
      { "url": "/titanic/statistics/age", "label": "年齢の統計" }
    ]),
    statistics=get_ages_statistics(),
  )
