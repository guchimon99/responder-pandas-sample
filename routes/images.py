import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from api_instance import api

from models.air_quality import get_air_quality

@api.route("/images/air_quality/station_paris")
async def plot (req, resp):
  air_quality = get_air_quality()
  plot = air_quality["station_paris"].plot()
  figure = plot.get_figure()

  output = io.BytesIO()
  FigureCanvas(figure).print_png(output)

  resp.content = output.getvalue()
  resp.mimetype = "image/png"
