# This repo contains multiple files for basic documentation of scripting in ArcGIS Pro

### Aforementioned files are contained within the `tutorials` directory

## Feature Class Creation || `fc_script.py`
* The Default `file_path` can be set automatically, or set via user input during runtime in ArcGIS Pro
* After importing the script into ArcGIS Pro, the desired `feature_class_name` must be set to `parameter 1` as a string variable and `file_path` set as `parameter 2`
* There is a 13 character limit on `feature_class_name` due to limitations within ArcGIS Pro itself
* By default, the script will create 3 shapefiles in the respective directory. They are as followed:
  * `Points`
  * `Polylines`
  * `Polygons`
* The user can change the default `fields` contained within each feature class by altering the `fields` data structure with corresponding information.