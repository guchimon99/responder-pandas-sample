import pandas as pd

from api_instance import api

def buildBreadcrumbs(children = []):
  breadcrumbs = [
    { "url": "/", "label": "ホーム" },
    { "url": "/air_quality", "label": "大気の状態" }
  ]

  breadcrumbs.extend(children)
  return breadcrumbs

@api.route("/air_quality")
async def passengerDetail (req, resp):
  resp.content = api.template(
    "pages/air_quality/home.html",
    title="大気の状態",
    breadcrumbs=buildBreadcrumbs()
  )
