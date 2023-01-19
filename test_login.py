from arcgis.gis import *
from arcgis.gis import GIS
from dotenv import load_dotenv

# Load user ArcGIS password from the .env file
load_dotenv()
ARCGIS_PASSWORD = os.getenv("ARCGIS_PW")