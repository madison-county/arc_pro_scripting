import os, datetime, time, arcpy, shutil
from arcgis.gis import *
from arcgis.gis import GIS
from datetime import datetime, timedelta
from dotenv import load_dotenv
from zipfile import ZipFile 

load_dotenv()
ARCGIS_PASSWORD = os.getenv("ARCGIS_PW")

# Using current time for folder labels and process tracking  
initialStartTime = datetime.now() 
time.sleep(10)