from api_instance import api

@api.route("/")
async def home (req, resp):
  resp.content = api.template(
    "pages/home.html",
    title="ホーム",
  )
