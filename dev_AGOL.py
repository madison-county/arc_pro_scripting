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

pathing_locations = [TempsG, 
                     structuresFolder, 
                    newRoadStructureLocation,
                    backupFolder,
                    outWorkspace,
                    newTempLocation,
                    TempName,
                    temporaryOutWorkspace,
                    copyLocation,
                    originalRoadStructureLocation,
                    originalRouteLocation,
                    newRouteLocation]

for path in pathing_locations:
    print(path)

def main():
    path = MakePath(backupFolder, label, initialStartTime)
    print('*** Main path: {} ***'.format(path))
    input_file_name, output_file_name, FGDB_name = downloadFromAGOL(path, initialStartTime, ARCGIS_PASSWORD)
    featureTransfer(output_file_name, FGDB_name, structuresFolder, label, initialStartTime)

def TimeCalculation(initialStartTime):    ## This is the time tracking code function.
    runTime = datetime.now() - initialStartTime
    return runTime 

def MakePath(backupFolder, label, initialStartTime):    #Makes the Geodata Backup Folder.
    path = os.path.join(backupFolder + 'Backup-'+ label + '-Geodata')
    print('***** {} *****'.format(path))
    if not os.path.exists(path):
        print('*** Creating new directory - MakePath function call: {} ***'.format(path))
        os.makedirs(path)
    print('MakePath Complete: ' + path)
    TimeCalculation(initialStartTime)
    return path

def downloadFromAGOL(backupFolder, initialStartTime, ARCGIS_PASSWORD):    # Downloads the data from AGOL to the backup folder location; calls the extraction process.
    # Get the current date and time-----------------------------------------------------------------------------------------
    date_time = time.strftime('%m%d%Y%H%M')
    print('Download Process started:   \t\t\t\t\t\t L__41 \t' + time.ctime())

    cred_gis = GIS('https://www.arcgis.com','Jboyk_MadisonCounty', ARCGIS_PASSWORD)
    print('Succcessfully logged in as '+ cred_gis.properties.user.username)
    print('Login successful \t\t\t\t\t\t\t\t L__45 \t' + str(time.ctime()))
    # Define the ArcGIS Online Item ID for Core Data------------------------------------------------------------------------
    coreFeatureService = 'ecd08dc4ffd341b1a1552f640c7c79d8'
    # coreFeatureService = 'ecd08dc4ffd341b1a1552f640c7c79d8'
    print('The coreFeatureService is defined \t\t\t\t\t L__49 \t' + str(time.ctime()))
    
    # Get the Core Data AGOL Items-------------------------------------------------------------------------------
    coreFeature_item = cred_gis.content.get(coreFeatureService)
    print('The GET command completed \t\t\t\t\t L__53 \t' + str(time.ctime()))
    
    #Notification.notificationSound(text)
    
    # Export the Structures and Roads Feature Services to FGDB--------------------------------------------------------------
    coreFeature_item_fgdb = coreFeature_item.export('CoreData_' + str(date_time),'File Geodatabase') # This was used for the original script to download the feature classes via FDGB
    #coreFeature_item_fgdb = coreFeature_item.export('CoreData_' + str(date_time),'Shapefile') #    Use this method to download shapefiles. Used to validate files if feature classes are not working. 
    print('Export completed \t\t\t\t\t\t\t\t L__57 \t' + str(time.ctime()))
    
    # Download the FGDB-----------------------------------------------------------------------------------------------------
    coreFeature_item_fgdb.download(save_path = backupFolder) # r'E:\Dropbox (Geodata)\Data\MT_NG911_Madison\AGO_Backup')
    print('Download completed \t\t\t\t\t\t\t L__61 \t' + str(time.ctime()))
    
    # Delete the FGDB Items in AGOL-----------------------------------------------------------------------------------------
    coreFeature_item_fgdb.delete()
    print('Temp file in AGOL deleted \t\t\t\t\t\t L__65 \t' + str(time.ctime()))
    
    # Create Variables for output text file
    coreFeature_item_lyrs = coreFeature_item.layers
    #backupFolder = r'E:\GIS\DailyData\2020-File-Cleanup\Grants\NG9-1-1_Grant_FY2019-21\Data\AGOLBackup' # E:\Dropbox (Geodata)\Data\MT_NG911_Madison\AGO_Backup'
    outSummary = backupFolder + os.path.sep + date_time +"_NG911_Backup_Summary" + ".txt"
    input_file_name = backupFolder + os.path.sep + "CoreData" + date_time + ".zip" # Used in Tommy's script below.
    output_file_name = input_file_name[:-4]
    outFile = open(outSummary, 'w')
    print('Variables created \t\t\t\t\t\t\t\t L__74 \t' + str(time.ctime()))
    print('Input file: {}\nOutput File: {}'.format(input_file_name, output_file_name))

    #Create Summary Text File
    for lyr in coreFeature_item_lyrs:
        feat_cnt = lyr.query(where='OBJECTID > 0', return_count_only=True)
        #arcpy.AddMessage ("Layer: {} ({})".format(lyr.properties.name, feat_cnt))
        outFile.write("Layer: " + lyr.properties.name)
        outFile.write("" + "\n")
        outFile.write("      Count: " + str(feat_cnt))
        outFile.write(""+"\n"+"\n")
    
    outFile.close()
    print('Backup Summary Completed \t\t\t\t\t\t L__86 \t' + str(time.ctime()))
    FGDB_name = extractZipFile(input_file_name, output_file_name, initialStartTime)
    print('*** FGDB: {} ***'.format(FGDB_name))
    # TODO - Fix pathing issue here
    print('FGDB_name: ' + FGDB_name)
    TimeCalculation(initialStartTime)
    return input_file_name, output_file_name, FGDB_name

def extractZipFile(input_file_name, output_file_name, initialStartTime):
    with ZipFile(input_file_name, 'r') as zip:     # Extracts the files into backup folder.
        print('Extracting the following files now...')
        print(zip.namelist())
        FGDB = zip.namelist()[0]
        FGDB_name = FGDB[0:36]
        zip.extractall(output_file_name)
        print(output_file_name + '  is Done!\n') 
    print('Backup/extraction process completed \t\t\t\t L_103 \t' + str(time.ctime()))
    print('FGDB_name =  ' + FGDB_name)
    # Set the workspace for ListFeatureClasses
    workSpace = output_file_name + os.path.sep + FGDB_name + ".gdb"    # FGDB_Path
    print('Workspace at line 143 is:  '+ workSpace) # '\n Or' + str(arcpy.env.workspace))
    arcpy.env.workspace = workSpace #    output_file_name + os.path.sep + FGDB_name    # FGDB_Path
    
    # Use the ListFeatureClasses function to print a list of shapefiles.
    featureclasses = arcpy.ListFeatureClasses()
    print('\nDownloaded features are: ')
    for fc in featureclasses:
        print('\t' + fc)
    return FGDB_name

def featureTransfer(output_file_name, FGDB_name, structuresFolder, label, initialStartTime):     # Sends files to the E drive
    #arcpy.env.workspace = structuresFolder
    #arcpy.env.overwriteOutput = True
    print('Workspace at line 195 is:  ' + str(arcpy.env.workspace))
    print('Local features are going to be overwritten with Online data')
    #    Creating TempsG shapefiles from feature classes.
    arcpy.conversion.FeatureClassToShapefile(output_file_name + os.path.sep + FGDB_name + '.gdb\SiteStructureAddressPoints;' + output_file_name + os.path.sep + FGDB_name + '.gdb\RoadCenterlines', structuresFolder + os.path.sep + 'TransferFolder')
    #arcpy.conversion.FeatureClassToShapefile(output_file_name + os.path.sep + FGDB_name + '\SiteStructureAddressPoints;' + output_file_name + os.path.sep + FGDB_name + '\RoadCenterlines', structuresFolder + os.path.sep + 'TransferFolder') # Original line from before 10/28/2021
    
    arcpy.CopyFeatures_management(structuresFolder + os.path.sep + 'TransferFolder\SiteStructureAddressPoints.shp', structuresFolder + os.path.sep + 'TransferFolder' + os.path.sep + '2020_Structures.shp')
    arcpy.CopyFeatures_management(structuresFolder + os.path.sep + 'TransferFolder\RoadCenterlines.shp', structuresFolder + os.path.sep + 'TransferFolder' + os.path.sep + '2020_Roads.shp')
    arcpy.Delete_management(structuresFolder + os.path.sep + 'TransferFolder\SiteStructureAddressPoints.shp')    # Removes the SiteStructureAddressPoints Shape File from the E:\..Road_Struct Folder.
    arcpy.Delete_management(structuresFolder + os.path.sep + 'TransferFolder\RoadCenterlines.shp')    # Removes the RoadCenterlines Shape File from the E:\..Road_Struct Folder.
    arcpy.Delete_management(output_file_name) #    Deletes the 2020_files from the Transfer folder.
    print('Files and folders transferred \t\t\t\t\t L_185')
    
    arcpy.env.overwriteOutput = False
    TimeCalculation(initialStartTime)

if __name__ == "__main__":
    main()