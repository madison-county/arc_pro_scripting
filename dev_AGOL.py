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

# Windows Pathing
TempsG = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/temps/'
structuresFolder = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/structures/'
newRoadStructureLocation = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/new_roads/' + os.path.sep
backupFolder = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/backup/'
outWorkspace = backupFolder + '/Backup-' + label
newTempLocation = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/temps_local/'
TempName = 'Temp'
temporaryOutWorkspace = outWorkspace + '/Temps' + label
copyLocation = structuresFolder + os.path.sep + 'TransferFolder'
originalRoadStructureLocation = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/routing/'
originalRouteLocation = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/original_routing/'
newRouteLocation = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/new_routes/'