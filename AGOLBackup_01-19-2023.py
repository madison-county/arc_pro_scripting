from arcgis.gis import *
from arcgis.gis import GIS
import os, datetime, time, arcpy, shutil
from datetime import datetime, timedelta
#import Notification
from dotenv import load_dotenv
from zipfile import ZipFile 

load_dotenv()
ARCGIS_PASSWORD = os.getenv("ARCGIS_PW")

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
if WorkingLocation == "2": # Annex
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
if WorkingLocation == "3": # Old Server
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
if WorkingLocation == "4": # Testing 
    print("Testing directory selected: {}".format(WorkingLocation))
    # Linux Pathing
    #TempsG = r'mnt/c/Users/jboyk/code_stuff/online_backups'
    #structuresFolder = r'mnt/c/Users/jboyk/code_stuff/online_backups/Road_Struct'
    # TODO newRoadStructureLocation
    #backupFolder = r'mnt/c/Users/jboyk/code_stuff/online_backups/backups_test'
    # TODO outWorkSpace
    #newTempLocation = r'mnt/c/Users/jboyk/code_stuff/online_backups/Temps_Local'
    # TODO TempName = 'Temp'
    # TODO temporaryOutWorkspace 
    # TODO copyLocation
    #originalRoadStructureLocation = r'mnt/c/Users/jboyk/code_stuff/online_backups/Roads'
    # TODO newRoadStructureLocation
    #originalRouteLocation = r'mnt/c/Users/jboyk/code_stuff/online_backups/Routing'
    # TODO newRouteLocation

    # Windows Pathing
    TempsG = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/temps/'
    structuresFolder = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/structures/'
    # TODO newRoadStructureLocation
    backupFolder = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/backup/'
    # TODO outWorkspace
    newTempLocation = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/temps_local/'
    # TODO TempName
    # TODO temporaryOutWorkspace
    # TODO copyLocation
    originalRoadStructureLocation = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/routing/'
    originalRouteLocation = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/original_routing/'
    newRouteLocation = r'T:/01-Working_Data/03-Work_In_Progress/03-Jacob/AGOL/new_routes/'

else:
    print("Exiting match/case")
    exit()

def TimeCalculation(initialStartTime):    ## This is the time tracking code function.
    # printing initial_date  
    runTime = datetime.now() - initialStartTime
    #print('Process Run Time is:  ' + str(runTime))
    return runTime 

## Placeholder portion of the script.
def MakePath(backupFolder, label, initialStartTime):    #Makes the Geodata Backup Folder.
    path = os.path.join(backupFolder + os.path.sep + 'Backup-'+ label + '-Geodata')
    if not os.path.exists(path):
        os.makedirs(path)
    print('MakePath Complete: ' + path)
    TimeCalculation(initialStartTime)
    return path

## Placeholder portion of the script.
def downloadFromAGOL(backupFolder, initialStartTime, ARCGIS_PASSWORD):    # Downloads the data from AGOL to the backup folder location; calls the extraction process.
    # Get the current date and time-----------------------------------------------------------------------------------------
    date_time = time.strftime('%m%d%Y%H%M')
    print('Download Process started:   \t\t\t\t\t\t L__41 \t' + time.ctime())

    # Login to ArcGIS Online------------------------------------------------------------------------------------------------
    #cred_gis = GIS(username="GeodataMadison",password="1141_DAHLIA_dog")

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
    #Copy Temps to E drive.
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

#Notification.notificationSound(text)
path = MakePath(backupFolder, label, initialStartTime)
print("The save path is: " + path)
text = 'aa' #    input('What Code? \n\t')
input_file_name, output_file_name, FGDB_name = downloadFromAGOL(path, initialStartTime, ARCGIS_PASSWORD)
print('\nCompleted\t\t\t\t\t\t\t\t\t L_298 \t' + str(time.ctime()))
print('\nOutput folder location is: \n\t  ' + output_file_name + '\n')
text = 'tt' #    input('What Code? \n\t')
featureTransfer(output_file_name, FGDB_name, structuresFolder, label, initialStartTime)
time.sleep(1)

copyPasteOverwrite(structuresFolder, copyLocation, initialStartTime)

#Notification.notificationSound('MovingOn')
print('L_348')

##                 New Code 8-12-20
CopyStucturesTempsToBackupFolder_G(label, outWorkspace, TempsG, temporaryOutWorkspace, initialStartTime, structuresFolder)
prompt = "Are you Connected to the server?"
connectedToServer =  ask_user(prompt)
if connectedToServer == 'y':
    TempsToE(TempsG, newTempLocation, TempName, initialStartTime)
    RoadStructuresToG(originalRoadStructureLocation, newRoadStructureLocation, initialStartTime)
    wavName = 'Alarm06.wav'
    #Notification.endTone(wavName)
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

#Notification.notificationSound('Complete')
runTime = TimeCalculation(initialStartTime)
print('\n \n \nThe entire backup and file transfer process has completed with a Run Time of: \n\t\t\t\t\t' + str(runTime) + '\n')
print('\t\t\tAt:  ' + str(datetime.now()) + '\nCompared to estimated time of: ' + str(estCompletedTime))
print(str(estCompletedTime-initialStartTime))
wavName = 'Ring08.wav'
#Notification.endTone(wavName)