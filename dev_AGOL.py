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

label = 'testing_label'
currentTime = str(datetime.now())  
date = str(datetime.now())[:10]    
hour = str(datetime.now())[11:13]    
minute = str(datetime.now())[14:16]    
second = str(datetime.now())[16:18]
print(currentTime)
print('Initial Start Time is:  \t\t\t\t\t\t\t\t\t' + str(initialStartTime))
estCompletedTime = initialStartTime + timedelta(minutes = 6)  #    datetime.timedelta(minutes = 10)
print('Expected completion time is:   \t\t\t\t\t\t\t' + str(estCompletedTime))
print('Folder Label is:  ' + label)