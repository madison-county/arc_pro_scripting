# This repo contains multiple files for basic documentation of scripting in ArcGIS Pro

### Aforementioned files are contained within the `tutorials` directory

## Feature Class Creation || `fc_script.py`
* The Default `file_path` can be set automatically, or set via user input during runtime in ArcGIS Pro
  * Note: `file_path` will also name each feature class files with a subset of their respective type.
  * Be sure to enter the directory of a `GeoDataBase (.gdb)` in order to create a `Feature Class`
    * If a normal directory is chosen, a `shapefile` will be created instead
* After importing the script into ArcGIS Pro, the desired `feature_class_name` must be set to `parameter 0` as a string variable and `file_path` set as `parameter 1`
* There is a 13 character limit on `feature_class_name` due to limitations within ArcGIS Pro itself
* By default, the script will create 3 shapefiles in the respective directory with the entered `file_path`. They are as followed:
  * `Points`
  * `Polylines`
  * `Polygons`
* The user can change the default `fields` contained within each feature class by altering the `fields` data structure with corresponding information.

## Converting a `Layer file` to a `KML file`
### Documentation is outlined here:
#### https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/layer-to-kml.htm

* The only required user entry field is the input layer.
  * All other fields will default to values set internally via the script
  * However, it is possible to manually enter fields for a more customizable `.kml` file
  * The additional fields are listed below:
    * `composite` (String):
      * Default value is `COMPOSITE`
      * Can also be supplied with `NO_COMPOSITE`
    * `pixels` (Double): 
      * Default value is `8192`
      * No restrictions on keyword arguments
    * `dpi` (Double):
      * Default value is set to `96`
      * No restrictions on keyword arguments
    * `clamped` (String) || `ignore_zvalue`:
      * Default value is set to `CLAMPED_TO_GROUND`
      * Can also be supplied with `ABSOLUTE`