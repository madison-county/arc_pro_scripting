# This repo contains multiple files for basic documentation of scripting in ArcGIS Pro

### Aforementioned files are contained within the `tutorials` directory

## Feature Class Creation || `fc_script.py`
* The Default `file_path` can be set automatically, or set via user input during runtime in ArcGIS Pro
  * Note: `file_path` will also name each feature class files with a subset of their respective type.
  * Be sure to enter the directory of a `GeoDataBase (.gdb)` in order to create a `Feature Class`
    * If a normal directory is chosen, a `shapefile` will be created instead
* After importing the script into ArcGIS Pro, the desired `feature_class_name` must be set to `parameter 0` as a string variable and `file_path` set as a `string` variable for `parameter 1`.
* There is a 13 character limit on `feature_class_name` due to limitations within ArcGIS Pro itself.
* By default, the script will create 3 shapefiles in the respective directory with the entered `file_path`. They are as followed:
  * `Points`
  * `Polylines`
  * `Polygons`
* The user can change the default `fields` contained within each feature class by altering the `fields` data structure with corresponding information.
  * The default values are listed below:
  * `field_name`, `field_type`, `{field_precision}`, `{field_scale}`, `{field_length}`, `{field_alias}`, `{field_is_nullable}`, `{field_is_required}`, `{field_domain}`
    * `field_name`: Name of the field to be added to the input table
    * `field_type`: Specify the type of the new field
      * `TEXT`, `FLOAT`, `DOUBLE`, `SHORT`, `LONG`, `DATE`, `BLOB`, `RASTER`, `GUID`
    * `{field_precision}`: Total number of digits that can be stored in the field. 
      * Only applies to field types `FLOAT`, `DOUBLE`, `SHORT`, or `LONG`
    * `{field_scale}`: Total number of decimal places stored in the field.
      * Only applies to `FLOAT` or `DOUBLE`.
    * `{field_length}`: Length of field - Sets the maximum allowed characters.
      * Only applies to `TEXT`.
    * `{field_alias}`: Alternate name for a field - Can include spaces and various characters not normally allowed in `field_name`.
      * Only applies to `geodatabases`
    * `{field_is_nullable}`: Specifies whether the field can contain null values - which differ from zero or empty fields.
      * Only applies to `geodatabases`
      * Supports the argument `NON-NULLABLE` and `NULLABLE`.
    * `{field_is_required}`: Specifies whether the field will be required or not for the table.
      * Required fields are only supported in `geodatabases`
      * Supports `NON_REQUIRED` and `REQUIRED`
    * `field_domain`: Constraints the values allowed in any attribute for a table, feature class, or subtype in a `geodatabase`. The name of the pre-existing domain must be specified for it to be applicable.
    
    
## Converting a `Layer file` to a `KML file` || `layer_to_kml.py`
### Documentation is outlined here:
#### https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/layer-to-kml.htm

* The only required user entry field is the input layer.
  * All other fields will default to values set internally via the script
  * However, it is possible to manually enter fields for a more customizable `.kml` file
  * The additional fields are listed below:
    * `composite` (String) || `is_composite`:
      * `Parameter(2)`
      * Default value is `COMPOSITE`
      * Can also be supplied with `NO_COMPOSITE`
    * `pixels` (Double) || `image_size`:
      * `Parameter(3)`
      * Default value is `8192`
      * No restrictions on keyword arguments
    * `dpi` (Double) || `dpi_of_clients`:
      * `Parameter(4)`
      * Default value is set to `96`
      * No restrictions on keyword arguments
    * `clamped` (String) || `ignore_zvalue`:
      * `Parameter(5)`
      * Default value is set to `CLAMPED_TO_GROUND`
      * Can also be supplied with `ABSOLUTE`

## Exporting and Trimming a `.gdb` or `shapefile` || `modular_export.py`
* The overall scope of this script is to take a input `shapefile` or `.gdb`, trim fields down, concat `Township`, `T_Directio`, `Range`, `R_Directio`, and `Section_s_` into a newly created field called `Legal_Loc` and export a new `shapefile`.
* The `Legal_Loc` field will be present in the originally supplied `shapefile`/`.gdb` as well as the newly created `shapefile` from the export.
* Export fields are `Label`, `<supplied user parameter>` (as decribed below), `File_date`, `Legal_Loc` (described above), and `Subdivisio` (`Subdivision Name`).
* This script takes three input parameters that must be enabled upon bringing the script in ArcGIS Pro:
  - 1: The name of the `shapefile` or `.gdb` to be updated (in the current project directory) 
  - 2: The name of the field to make a selection on:
    * Examples in `Book`, `Road_Name`, or `District`
  - 3: The value of the field required to make the selection:
    * Examples: If `Book` is supplied for the above example, then `4` or `5` could be passed to this field to make a selection of all specified fields that contain `Book` == `4`. 
* Additionally, this script makes use of the `python-dotenv` package, which must be configured within a clone environment within ArcGIS Pro. 
  * Creation of a .env file in the script directory is required, after which the user can define `ARCGIS_PW=<your password>` in order to ping the ArcGIS Pro system online and retrieve corresponding files. 

## AGOL Backups || `dev_AGOL.py` and `AGOLBackup_01-19-2023.py`
* This script is designed to download and backup ArcGIS Pro datasets from various online web services and overwrite local locations to provide up to date and accurate information.
* Eventually, the script will also download respective files for the Weed Board and Dispatch offices.