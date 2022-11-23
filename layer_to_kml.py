# https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/layer-to-kml.htm

import arcpy
import os

arcpy.env.workspace = "C:/Users/jboyk/map_stuff/test_project_2"

layer_path = (r"C:/Users/jboyk/code_stuff/python/arc_pro_scripting/Montana_PublicLands.gdb")
layer_file = "Montana_PublicLands_Layer"
KML_OUT_PATH = (r"C:/Users/jboyk/map_stuff/test_project_2")

layer_input = arcpy.GetParameterAsText(0)
layer_output_path = arcpy.GetParameterAsText(1)
composite = arcpy.GetParameterAsText(2) or 'COMPOSITE'
pixels = arcpy.GetParameterAsText(3) or 8192
dpi = arcpy.GetParameterAsText(4) or 96
clamped = arcpy.GetParameterAsText(5) or 'CLAMPED_TO_GROUND'

for scale in range(10000, 30001, 10000):
    arcpy.conversion.LayerToKML("Montana_PublicLands_Layer.lyrx", 'out_kml.kmz', scale, composite,
                                '', pixels, dpi, clamped)
