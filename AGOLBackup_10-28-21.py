from arcgis.gis import *
from arcgis.gis import GIS
import os, datetime, time, arcpy
from datetime import datetime, timedelta
import time, os, shutil
import Notification
import getpass
password=getpass.getpass('Enter Word: \t\n')
# gis = GIS(profile="Tommy_AGOL_prof") # Does not work here.
# Using current time for folder labels and process tracking  
initialStartTime = datetime.now() 
time.sleep(10)

label = datetime.now().strftime("%Y-%m-%d_Time-%H-%M")    #Creates the timestamp for the label
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

#Choose the download location:
#downloadPath = r'E:\GIS\DailyData\2020-File-Cleanup\Grants\NG9-1-1_Grant_FY2019-21\Data\AGOLBackup'

#password = input("What should I know?")
WorkingLocation = input("\n\tEnter 1 if you are working via VPN. \n\tEnter 2 if you are working in the Annex. \n\tEnter 3 if you are working with the old server.\n\t")
time.sleep(5)

if WorkingLocation == "1": # VPN
    print("You entered: " + WorkingLocation)
    ###    Variables for OUT-OF-Office U:\4-15-21_G-Drive-COPY-COPY\GIS
    TempsG = r'U:\GIS_2022\DailyData\Temps'  # will need to update to the T drive after migration. **************************************************************************************
    structuresFolder = r'E:\GIS\DailyData\Road_Struct'
    newRoadStructureLocation = r'U:\GIS_2022\DailyData\Road_Struct' + os.path.sep
    backupFolder = r'E:\CompletedTasks\DataBackup\Backups' #+ os.path.sep
    #backupFolder = r'U:\CompletedTasks\DataBackup\Backups' #+ os.path.sep # Original line changed 10/28/2021
    outWorkspace =backupFolder + '\Backup-' + label
    newTempLocation = 'E:/GIS/DailyData/Temps_Local/'
    TempName = 'Temp'
    temporaryOutWorkspace = outWorkspace + '\Temps-' + label
    copyLocation = structuresFolder + os.path.sep + 'TransferFolder'
    originalRoadStructureLocation = 'E:/GIS/DailyData/Road_Struct/' #Line 350
    newRoadStructureLocation = 'U:\GIS_2022/DailyData/Road_Struct/'
    originalRouteLocation = r'E:\GIS\DailyData\Road_Struct\Routing'
    newRouteLocation = r'U:\GIS_2022\DailyData\Road_Struct\Routing'
elif WorkingLocation == "2": # Annex
    print("You entered: " + WorkingLocation)
    ##    Variables for T drive (GNAS server)
    TempsG = r'T:\GIS_2022\DailyData\Temps' # will need to update to the T drive after migration. **************************************************************************************
    structuresFolder = r'E:\GIS\DailyData\Road_Struct'
    newRoadStructureLocation = r'T:\GIS_2022\DailyData\Road_Struct' + os.path.sep
    backupFolder = r'T:\CompletedTasks\DataBackup\Backups' #+ os.path.sep
    outWorkspace =backupFolder + '\Backup-' + label
    newTempLocation = 'E:/GIS/DailyData/Temps_Local/'
    TempName = 'Temp'
    temporaryOutWorkspace = outWorkspace + '\Temps-' + label
    copyLocation = structuresFolder + os.path.sep + 'TransferFolder'
    originalRoadStructureLocation = 'E:/GIS/DailyData/Road_Struct/' #Line 350
    newRoadStructureLocation = 'T:/GIS_2022/DailyData/Road_Struct/'
    originalRouteLocation = r'E:\GIS\DailyData\Road_Struct\Routing'
    newRouteLocation = r'T:\GIS_2022\DailyData\Road_Struct\Routing'
elif WorkingLocation == "3": # Old Server
    print("You entered: " + WorkingLocation)
    ##    Variables for G drive (s2 server) 
    TempsG = r'T\GIS\DailyData\Temps' # will need to update to the T drive after migration. **************************************************************************************
    structuresFolder = r'E:\GIS\DailyData\Road_Struct'
    newRoadStructureLocation = r'T:\GIS\DailyData\Road_Struct' + os.path.sep
    backupFolder = r'T:\CompletedTasks\DataBackup\Backups' #+ os.path.sep
    outWorkspace =backupFolder + '\Backup-' + label
    newTempLocation = 'E:/GIS/DailyData/Temps_Local/'
    TempName = 'Temp'
    temporaryOutWorkspace = outWorkspace + '\Temps-' + label
    copyLocation = structuresFolder + os.path.sep + 'TransferFolder'
    originalRoadStructureLocation = 'E:/GIS/DailyData/Road_Struct/' #Line 350
    newRoadStructureLocation = 'T:/GIS/DailyData/Road_Struct/'
    originalRouteLocation = r'E:\GIS\DailyData\Road_Struct\Routing'
    newRouteLocation = r'T:\GIS\DailyData\Road_Struct\Routing'
else:
    exit()



def TimeCalculation(initialStartTime):    ## This is the time tracking code function.
    # printing initial_date  
    runTime = datetime.now() - initialStartTime
    #print('Process Run Time is:  ' + str(runTime))
    return runTime 

## Placeholder portion of the script.

def MakePath(backupFolder, label, initialStartTime):    #Makes the Geodata Backup Folder.
    import os
    path = os.path.join(backupFolder + os.path.sep + 'Backup-'+ label + '-Geodata')
    if not os.path.exists(path):
        os.makedirs(path)
    return path
    print('MakePath Complete: ' + path)
    TimeCalculation(initialStartTime)
## Placeholder portion of the script.

def downloadFromAGOL(backupFolder, initialStartTime, password):    # Downloads the data from AGOL to the backup folder location; calls the extraction process.
    # coding: utf-8
    #from arcgis.gis import *
    #from arcgis.gis import GIS
    #import os, datetime, time, arcpy
    
    # Get the current date and time-----------------------------------------------------------------------------------------
    date_time = time.strftime('%m%d%Y%H%M')
    print('Download Process started:   \t\t\t\t\t\t L__41 \t' + time.ctime())

    # Login to ArcGIS Online------------------------------------------------------------------------------------------------
    #cred_gis = GIS(username="GeodataMadison",password="1141_DAHLIA_dog")
    #import getpass
    from arcgis.gis import GIS
    #password=getpass.getpass('Enter Word: \t\n')

    cred_gis = GIS('https://www.arcgis.com','tluksha', password)
    print('Succcessfully logged in as '+ cred_gis.properties.user.username)
    print('Login successful \t\t\t\t\t\t\t\t L__45 \t' + str(time.ctime()))
    # Define the ArcGIS Online Item ID for Core Data------------------------------------------------------------------------
    coreFeatureService = 'ecd08dc4ffd341b1a1552f640c7c79d8'
    # coreFeatureService = 'ecd08dc4ffd341b1a1552f640c7c79d8'
    print('The coreFeatureService is defined \t\t\t\t\t L__49 \t' + str(time.ctime()))
    
    # Get the Core Data AGOL Items-------------------------------------------------------------------------------
    coreFeature_item = cred_gis.content.get(coreFeatureService)
    print('The GET command completed \t\t\t\t\t L__53 \t' + str(time.ctime()))
    
    Notification.notificationSound(text)
    
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
    print('FGDB_name: ' + FGDB_name)
    TimeCalculation(initialStartTime)
    return input_file_name, output_file_name, FGDB_name


## Placeholder portion of the script.

def extractZipFile(input_file_name, output_file_name, initialStartTime):
    # importing required modules 
    from zipfile import ZipFile 

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

## Placeholder portion of the script.

def ask_user(prompt):    ## This is the user input function that only evaluates for "Yes" or "No"
    check = str(input(prompt)).lower().strip()
    try:
        if check[0] == 'y':
            return 'y' #    True
        elif check[0] == 'n':
            return 'n' #    False
        else:
            print('Invalid Input')
            return ask_user('You entered an invalid input. Please enter \"Yes\" or \"No\" (or \"Y\" or \"N\"):\t\t\t')
    except Exception as error:
        #print("Please enter valid inputs")
        print(error)
        return ask_user('You entered an invalid input. Please enter \"Yes\" or \"No\" (or \"Y\" or \"N\"):\t\t\t')

## Placeholder portion of the script.

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
## Placeholder portion of the script.

def copyPasteOverwrite(structuresFolder, copyLocation, initialStartTime):
    import os
    import shutil
    root_src_dir = copyLocation
    root_dst_dir = structuresFolder
    
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                # in case of the src and dst are the same file
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)
    TimeCalculation(initialStartTime)

## Placeholder portion of the script.

##                 New Code 8-12-20

def CopyStucturesTempsToBackupFolder_G(label, outWorkspace, TempsG, temporaryOutWorkspace, initialStartTime, structuresFolder):
    print("Creating Folder: " + label)
    print("Copying Files....")
    err = "Something went awry on L_274"
    if os.path.exists(outWorkspace):
        print("Already Done :( ")

    else: #IF IT DOES NOT EXIST, THEN EXECUTE THIS CODE
        try:                # The try / excepts are only to hide the errors that would normally display
            shutil.copytree(structuresFolder, outWorkspace, symlinks=False, ignore=shutil.ignore_patterns('*.lock'))
            print("Structures copied")
            shutil.copytree(TempsG, temporaryOutWorkspace, symlinks=False, ignore=shutil.ignore_patterns('*.lock'))
            print("Temps copied")
            #shutil.copytree(gpsLog, gpsLogOutWorkspace, symlinks=False, ignore=shutil.ignore_patterns('*.lock'))
            #print("GPSLog copied")
        except Exception as err:
            print('Files not copied')
            print(err)
    runTime = TimeCalculation(initialStartTime)
    print("\n\n" + "Backup Completed with a Run Time of: " + str(runTime))
    print("At:  " + str(datetime.now()) + "\n \n")


## Placeholder portion of the script.

def TempsToE(TempsG, newTempLocation, TempName, initialStartTime):
    #    Copy Temps to E drive.
    #TempsG = "G:/GIS/DailyData/Temps/"
    #newTempLocation = "E:/GIS/DailyData/Temps_Local/"
    #TempName = 'TemporaryAddress'
    print("\n \n" + "Copying Temps over" + "\n \n")
    
    for filename in os.listdir(TempsG):
        if filename.endswith(".lock"):
            print(filename + "  was not copied")
            pass
        else:
            if filename.startswith(TempName):
    
                srcLS=os.path.join(TempsG,filename)
                print(srcLS + "  has been copied.")
                shutil.copy2(srcLS,newTempLocation)
    #            print(filename + "  has been copied.")
    runTime = TimeCalculation(initialStartTime)
    print("\n\n" + "Temp transfer completed with a Run Time of: " + str(runTime))
    print("At:  " + str(datetime.now()))

## Placeholder portion of the script.

def RoadStructuresToG(originalRoadStructureLocation, newRoadStructureLocation, initialStartTime):
    print("\n \n" + "Copying Roads, Structures, Routes, etc. over" + "\n \n")
    for filename in os.listdir(originalRoadStructureLocation):
        try:
            
            if os.path.isdir(filename):
                print(filename + "  is a folder and was not copied")
                continue
            elif filename.endswith(".lock"):
                print(filename + "  was not copied")
                continue
            else:
        #        if filename.startswith("1000_Pt_Routes"):
                srcTAL=os.path.join(originalRoadStructureLocation,filename)
                print(srcTAL + "  has been copied.")
                shutil.copy2(srcTAL,newRoadStructureLocation)
        except IOError:
            print("\n " + filename + "  was PASSED over. \n")
            print(IOError)
    runTime = TimeCalculation(initialStartTime)
    print("\n\n" + "Temp transfer completed with a Run Time of: " + str(runTime))
    print("At:  " + str(datetime.now()))    
    print('\n \n  Roads and Structures were copied \n \n')

## Placeholder portion of the script.

def TempsToE(TempsG, newTempLocation, TempName, initialStartTime):
    #    Copy Temps to E drive.
    #TempsG = "G:/GIS/DailyData/Temps/"
    #newTempLocation = "E:/GIS/DailyData/Temps_Local/"
    #TempName = 'TemporaryAddress'
    print("\n \n" + "Copying Temps over" + "\n \n")
    
    for filename in os.listdir(TempsG):
        if filename.endswith(".lock"):
            print(filename + "  was not copied")
            pass
        elif filename.endswith(".gdb"):                                                                                     # Check this after files are converted into geodatabases
            print(filename + "  was not copied")
            pass        
        else:
            if filename.startswith(TempName):
    
                srcLS=os.path.join(TempsG,filename)
                print(srcLS + "  has been copied.")
                shutil.copy2(srcLS,newTempLocation)
    #            print(filename + "  has been copied.")
    runTime = TimeCalculation(initialStartTime)
    print("\n\n" + "Temp transfer completed with a Run Time of: " + str(runTime))
    print("At:  " + str(datetime.now()))

## Placeholder portion of the script.

def RoutesToG(originalRouteLocation, newRouteLocation, initialStartTime):
    print("\n \n" + "Copying Roads, Structures, Routes, etc. over" + "\n \n")
    for filename in os.listdir(originalRouteLocation):
        try:
            
            if os.path.isdir(filename):
                print(filename + "  is a folder and was not copied")
                continue
            elif filename.endswith(".lock"):
                print(filename + "  was not copied")
                continue
            else:
        #        if filename.startswith("1000_Pt_Routes"):
                srcTAL=os.path.join(originalRouteLocation,filename)
                print(srcTAL + "  has been copied.")
                shutil.copy2(srcTAL,newRouteLocation)
        except IOError:
            print("\n " + filename + "  was PASSED over. \n")
            print(IOError)
    runTime = TimeCalculation(initialStartTime)
    print("\n\n" + "Routing transfer completed with a Run Time of: " + str(runTime))
    print("At:  " + str(datetime.now()))    
    print('\n \n  Routes were copied \n \n')

## Placeholder portion of the script.


text = 'tt' #    input('What Code? \n\t')

Notification.notificationSound(text)
path = MakePath(backupFolder, label, initialStartTime)
print("The save path is: " + path)
text = 'aa' #    input('What Code? \n\t')
input_file_name, output_file_name, FGDB_name = downloadFromAGOL(path, initialStartTime, password)
print('\nCompleted\t\t\t\t\t\t\t\t\t L_298 \t' + str(time.ctime()))
print('\nOutput folder location is: \n\t  ' + output_file_name + '\n')
text = 'tt' #    input('What Code? \n\t')
featureTransfer(output_file_name, FGDB_name, structuresFolder, label, initialStartTime)
time.sleep(1)

copyPasteOverwrite(structuresFolder, copyLocation, initialStartTime)

Notification.notificationSound('MovingOn')
print('L_348')

##                 New Code 8-12-20
CopyStucturesTempsToBackupFolder_G(label, outWorkspace, TempsG, temporaryOutWorkspace, initialStartTime, structuresFolder)
prompt = "Are you Connected to the server?"
connectedToServer =  ask_user(prompt)
if connectedToServer == 'y':
    TempsToE(TempsG, newTempLocation, TempName, initialStartTime)
    RoadStructuresToG(originalRoadStructureLocation, newRoadStructureLocation, initialStartTime)
    wavName = 'Alarm06.wav'
    Notification.endTone(wavName)
else:
    pass



#routeTransfer = 'Y' #    ask_user('Should Python transfer Routes to the G drive now? Y or N: \n\n\t\t\t\t\t\t')
routeTransfer = input('Shall I transfer Routes to the G drive now: Y or N \n\t').upper()
print('You answered: ' + routeTransfer + '\n\t\t\t\t\t\t')



if routeTransfer == 'Y':
    RoutesToG(originalRouteLocation, newRouteLocation, initialStartTime) #    Copy routes to G drive
    print('Routes WERE transferred.')
else:
    print('Routes were NOT transferred')

Notification.notificationSound('Complete')
runTime = TimeCalculation(initialStartTime)
print('\n \n \nThe entire backup and file transfer process has completed with a Run Time of: \n\t\t\t\t\t' + str(runTime) + '\n')
print('\t\t\tAt:  ' + str(datetime.now()) + '\nCompared to estimated time of: ' + str(estCompletedTime))
print(str(estCompletedTime-initialStartTime))
wavName = 'Ring08.wav'
Notification.endTone(wavName)

#To process after Changes:
#arcpy.management.AddJoin(r"Online_MC_Layers\SiteStructureAddressPoints", "Site_NGUID", "StructuresTable", "Site_NGUID", "KEEP_ALL")
#arcpy.conversion.FeatureClassToFeatureClass(r"E:\GIS\DailyData\Road_Struct\Python_Structures.shp", r"E:\GIS\DailyData\Road_Struct", "PythonJoinedStructures.shp", '', r'Source "Source of Data" true true false 75 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Source,0,75;DateUpdate "Date Updated" true true false 8 Date 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.DateUpdate,-1,-1;Effective "Effective Date" true true false 8 Date 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Effective,-1,-1;Expire "Expiration Date" true true false 8 Date 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Expire,-1,-1;Site_NGUID "Site NENA Globally Unique ID" true true false 100 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Site_NGUID,0,100;Country "Country" true true false 2 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Country,0,2;State "State" true true false 2 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.State,0,2;County "County" true true false 40 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.County,0,40;AddCode "Additional Code" true true false 6 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.AddCode,0,6;AddDataURI "Additional Data URI" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.AddDataURI,0,254;Inc_Muni "Incorporated Municipality" true true false 100 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Inc_Muni,0,100;Uninc_Comm "Unincorporated Community" true true false 100 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Uninc_Comm,0,100;Nbrhd_Comm "Neighborhood Community" true true false 100 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Nbrhd_Comm,0,100;AddNum_Pre "Address Number Prefix" true true false 15 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.AddNum_Pre,0,15;Add_Number "Address Number" true true false 0 Long 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Add_Number,-1,-1;AddNum_Suf "Address Number Suffix" true true false 15 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.AddNum_Suf,0,15;St_PreMod "Street Name Pre Modifier" true true false 15 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.St_PreMod,0,15;St_PreDir "Street Name Pre Directional" true true false 9 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.St_PreDir,0,9;St_PreType "Street Name Pre Type" true true false 50 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.St_PreType,0,50;St_PreSep "Street Name Pre Type Separator" true true false 20 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.St_PreSep,0,20;St_Name "Street Name" true true false 60 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.St_Name,0,60;St_PosTyp "Street Name Post Type" true true false 50 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.St_PosTyp,0,50;St_PosDir "Street Name Post Directional" true true false 9 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.St_PosDir,0,9;St_PosMod "Street Name Post Modifier" true true false 25 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.St_PosMod,0,25;LSt_PreTyp "Legacy Street Name Pre Type" true true false 10 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LSt_PreType,0,10;LSt_PreDir "Legacy Street Name Pre Directional" true true false 2 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LSt_PreDir,0,2;LSt_Name "Legacy Street Name" true true false 75 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LSt_Name,0,75;LSt_Type "Legacy Street Name Type" true true false 10 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LSt_Type,0,10;LSt_PosDir "Legacy Street Name Post Directional" true true false 2 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LSt_PosDir,0,2;ESN "ESN" true true false 5 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.ESN,0,5;MSAGComm "MSAG Community Name" true true false 30 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.MSAGComm,0,30;Post_Comm "Postal Community Name" true true false 40 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Post_Comm,0,40;Post_Code "Postal Code" true true false 7 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Post_Code,0,7;Post_Code4 "ZIP Plus 4" true true false 4 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Post_Code4,0,4;Building "Building" true true false 75 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Building,0,75;Floor "Floor" true true false 75 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Floor,0,75;Unit "Unit" true true false 75 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Unit,0,75;Room "Room" true true false 75 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Room,0,75;Seat "Seat" true true false 75 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Seat,0,75;Addtl_Loc "Additional Location Information" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Addtl_Loc,0,255;LandmkName "Complete Landmark Name" true true false 150 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LandmkName,0,150;Mile_Post "Mile Post" true true false 150 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Mile_Post,0,150;Place_Type "Place Type" true true false 50 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Place_Type,0,50;Placement "Placement Method" true true false 25 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Placement,0,25;Long "Longitude" true true false 0 Double 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Long,-1,-1;Lat "Latitude" true true false 0 Double 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Lat,-1,-1;Elev "Elevation" true true false 0 Long 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Elev,-1,-1;MT_PlcType "Montana Place Type" true true false 0 Long 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.MT_PlcType,-1,-1;ParcelID "ParcelID" true true false 17 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.ParcelID,0,17;LocalID "Local Unique ID" true true false 38 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LocalID,0,38;GlobalID "GlobalID" false false false 38 GlobalID 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.GlobalID,-1,-1;DiscrpAgID "Discrepancy Agency ID" true true false 75 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.DiscrpAgID,0,75;FullRoadNa "FullRoadName" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.FullRoadName,0,255;FullAddres "FullAddress" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.FullAddress,0,255;FullRoad_1 "FullRoadName_MSAGComm" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.FullRoadName_MSAGComm,0,255;FullRoad_2 "FullRoadName_ESN" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.FullRoadName_ESN,0,255;FullAddr_1 "FullAddress_MSAGComm" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.FullAddress_MSAGComm,0,255;FullAddr_2 "FullAddress_ESN" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.FullAddress_ESN,0,255;Notes "Notes" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Notes,0,255;Original_F "Original_FullAddress" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Original_FullAddress,0,255;Addr_NGUID "Address NENA Globally Unique ID" true true false 100 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Addr_NGUID,0,100;AccessPoin "Access Point Present" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.AccessPoint_Present,0,255;Review_Acc "Review_AccessPresent" true true false 3 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Review_AccessPresent,0,3;Resolved_A "Resolved_AccessPresent" true true false 4 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Resolved_AccessPresent,0,4;Flag_For_D "Flag_For_Deletion" true true false 3 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Flag_For_Deletion,0,3;Geodata_Ed "Geodata Editing Notes" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Geodata_Editing_Notes,0,255;Duplicate_ "Duplicate Address" true true false 255 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Duplicate_Address,0,255;Review_Dup "Review Duplicate Address" true true false 4 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Review_Duplicate,0,4;Resolved_D "Resolved Duplicate" true true false 10 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Resolved_Duplicate,0,10;YEAR_BUILT "YEAR_BUILT" true true false 0 Long 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.YEAR_BUILT,-1,-1;GeoText "GeoText" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.GeoText,0,256;SubdivName "SubdivName" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.SubdivName,0,256;SubDivLotN "SubDivLotNum" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.SubDivLotNum,0,256;Siding "Siding" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Siding,0,256;Roof "Roof" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Roof,0,256;SendLetter "SendLetter" true true false 0 Long 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.SendLetter,-1,-1;LetterType "LetterType" true true false 0 Long 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LetterType,-1,-1;DDPsize "DDPsize" true true false 0 Long 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.DDPsize,-1,-1;LetterSent "LetterSent" true true false 0 Date 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LetterSent,-1,-1;InParcel "InParcel" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.InParcel,0,256;LetterTo "LetterTo" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LetterTo,0,256;StrucType1 "StrucType1" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.StrucType1,0,256;StrucType2 "StrucType2" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.StrucType2,0,256;StrucType3 "StrucType3" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.StrucType3,0,256;Comment_1 "Comment_1" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Comment_1,0,256;Comment_2 "Comment_2" true true false 256 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.Comment_2,0,256;AssesText "AssesText" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.AssesText,0,254;LegalDescr "LegalDescr" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.LegalDescr,0,254;SDivLotNum "SDivLotNum" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,L1SiteStructureAddressPoints.SDivLotNum,0,254;OID_ "OID" false true false 4 Long 0 9,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.OID,-1,-1;OBJECTID "OBJECTID" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.OBJECTID,-1,-1;Source_1 "Source" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Source,0,254;DateUpda_1 "DateUpdate" true true false 8 Date 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.DateUpdate,-1,-1;Effective_ "Effective" true true false 8 Date 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Effective,-1,-1;Expire_1 "Expire" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Expire,0,254;Country_1 "Country" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Country,0,254;State_1 "State" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.State,0,254;County_1 "County" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.County,0,254;AddCode_1 "AddCode" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.AddCode,0,254;AddDataU_1 "AddDataURI" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.AddDataURI,0,254;AddURI_2 "AddURI_2" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.AddURI_2,0,254;PlatDeed "PlatDeed" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.PlatDeed,0,254;Inc_Muni_1 "Inc_Muni" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Inc_Muni,0,254;Uninc_Co_1 "Uninc_Comm" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Uninc_Comm,0,254;Nbrhd_Co_1 "Nbrhd_Comm" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Nbrhd_Comm,0,254;FullAddr_3 "FullAddres" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.FullAddres,0,254;FULLADR "FULLADR" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.FULLADR,0,254;AddNum_P_1 "AddNum_Pre" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.AddNum_Pre,0,254;Add_Numb_1 "Add_Number" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Add_Number,-1,-1;AddNum_S_1 "AddNum_Suf" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.AddNum_Suf,0,254;St_PreMod_ "St_PreMod" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.St_PreMod,0,254;St_PreDir_ "St_PreDir" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.St_PreDir,0,254;St_PreTy_1 "St_PreType" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.St_PreType,0,254;St_PreSep_ "St_PreSep" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.St_PreSep,0,254;StreetName "StreetName" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.StreetName,0,254;St_PosTyp_ "St_PosTyp" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.St_PosTyp,0,254;St_PosDir_ "St_PosDir" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.St_PosDir,0,254;St_PosMod_ "St_PosMod" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.St_PosMod,0,254;ESN_1 "ESN" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.ESN,-1,-1;MSAGComm_1 "MSAGComm" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.MSAGComm,0,254;Post_Comm_ "Post_Comm" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Post_Comm,0,254;Post_Code_ "Post_Code" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Post_Code,-1,-1;Post_Cod_1 "Post_Code4" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Post_Code4,-1,-1;Building_1 "Building" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Building,0,254;Floor_1 "Floor" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Floor,0,254;Unit_1 "Unit" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Unit,0,254;Room_1 "Room" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Room,0,254;Seat_1 "Seat" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Seat,0,254;Addtl_Loc_ "Addtl_Loc" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Addtl_Loc,0,254;LandmkNa_1 "LandmkName" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.LandmkName,0,254;Mile_Post_ "Mile_Post" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Mile_Post,0,254;Place_Ty_1 "Place_Type" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Place_Type,0,254;Placement_ "Placement" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Placement,0,254;Longitude "Longitude" true true false 19 Double 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Longitude,-1,-1;Latitude "Latitude" true true false 19 Double 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Latitude,-1,-1;Elevation "Elevation" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Elevation,-1,-1;Distance "Distance" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Distance,-1,-1;YEAR_BUI_1 "YEAR_BUILT" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.YEAR_BUILT,-1,-1;MT_PlcTy_1 "MT_PlcType" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.MT_PlcType,0,254;GeoText_1 "GeoText" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.GeoText,0,254;AssesText_ "AssesText" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.AssesText,0,254;LegalDes_1 "LegalDescr" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.LegalDescr,0,254;SubdivNa_1 "SubdivName" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.SubdivName,0,254;SDivLotN_1 "SDivLotNum" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.SDivLotNum,0,254;Siding_1 "Siding" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Siding,0,254;Roof_1 "Roof" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Roof,0,254;StruType1 "StruType1" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.StruType1,0,254;StruType2 "StruType2" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.StruType2,0,254;StruType3 "StruType3" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.StruType3,0,254;CONDO "CONDO" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.CONDO,0,254;GROUP_QTRS "GROUP_QTRS" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.GROUP_QTRS,0,254;Comment_12 "Comment_1" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Comment_1,0,254;Comment_23 "Comment_2" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Comment_2,0,254;GlobalID_1 "GlobalID" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.GlobalID,0,254;LocalID_1 "LocalID" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.LocalID,0,254;LetterTo_1 "LetterTo" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.LetterTo,0,254;SendLett_1 "SendLetter" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.SendLetter,-1,-1;LetterTy_1 "LetterType" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.LetterType,-1,-1;DDPsize_1 "DDPsize" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.DDPsize,-1,-1;LetterSe_1 "LetterSent" true true false 8 Date 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.LetterSent,-1,-1;NOTIFIED "NOTIFIED" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.NOTIFIED,0,254;OLDADR "OLDADR" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.OLDADR,0,254;OLD_ADDRES "OLD_ADDRES" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.OLD_ADDRES,-1,-1;OLD_DIRPRE "OLD_DIRPRE" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.OLD_DIRPRE,0,254;OLD_ROADNA "OLD_ROADNA" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.OLD_ROADNA,0,254;OLD_ROADTY "OLD_ROADTY" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.OLD_ROADTY,0,254;OLD_DIRSUF "OLD_DIRSUF" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.OLD_DIRSUF,0,254;PUBLICVIEW "PUBLICVIEW" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.PUBLICVIEW,0,254;X_Text "X_Text" true true false 19 Double 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.X_Text,-1,-1;Y_Text "Y_Text" true true false 19 Double 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Y_Text,-1,-1;ProbExists "ProbExists" true true false 10 Long 0 10,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.ProbExists,-1,-1;InParcel_1 "InParcel" true true false 3 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.InParcel,0,3;PhoneNum "PhoneNum" true true false 50 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.PhoneNum,0,50;PlatUnitNu "PlatUnitNu" true true false 50 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.PlatUnitNu,0,50;PCSRcomp "PCSRcomp" true true false 8 Date 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.PCSRcomp,-1,-1;Site_NGU_1 "Site_NGUID" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Site_NGUID,0,254;Geodata_Fu "Geodata_Fu" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Geodata_Fu,0,254;Structures "Structures" true true false 254 Text 0 0,First,#,Online_MC_Layers\SiteStructureAddressPoints,StructuresTable.Structures,0,254', '')
##arcpy.management.CalculateField("PythonJoinedStructures", "OLDADR", "!FullAddr_3!", "PYTHON3", '', "TEXT")
##arcpy.management.CalculateField("PythonJoinedStructures", "FullAddr_3", "!FullAddres!", "PYTHON3", '', "TEXT")

#Add NG911_Structures file to map (map.addDataFromPath(r"E:\GIS\DailyData\Road_Struct\NG911_Structures.shp" is not working... :(
