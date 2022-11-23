# https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/layer-to-kml.htm

import arcpy
import os

arcpy.env.workspace = "C:/Users/jboyk/map_stuff/test_project_2"

layer_path = (r"C:/Users/jboyk/code_stuff/python/arc_pro_scripting/Montana_PublicLands.gdb")
LAYER_FILE = "cemetery_layer"
KML_OUT_PATH = (r"C:/Users/jboyk/map_stuff/test_project_2/")

layer_input = arcpy.GetParameterAsText(0) or LAYER_FILE
layer_output_path = arcpy.GetParameterAsText(1) or KML_OUT_PATH
composite = arcpy.GetParameterAsText(2) or 'COMPOSITE'
pixels = arcpy.GetParameterAsText(3) or 4096
dpi = arcpy.GetParameterAsText(4) or 96
clamped = arcpy.GetParameterAsText(5) or 'CLAMPED_TO_GROUND'

# Export a .kml file with all default values for parameters
arcpy.conversion.LayerToKML(layer_input+".lyrx", layer_output_path+layer_input+'_simple_.kmz')

# Export a kml file with a set scale and specified values for each parameter
for scale in range(10000, 30001, 10000):
    arcpy.conversion.LayerToKML(layer_input+".lyrx", layer_output_path+layer_input+'_detailed_.kmz', scale, composite,
                                '', pixels, dpi, clamped)
