# Hillshade and Viewshed demos

# Created by: Ugochukwu Udonna Okonkwo
# Created on: 3-22-2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    elevation_file = r"C:\EsriPress\Python\Data\Colorado\Elevation"
    chap10_raster_data = r"C:\Geog_432\Chapter_10\Raster Data\Raster Data.gdb"

    # # SAMPLES ON SETTING ENVIRONMENT VARIABLES FOR RASTERS
    # arcpy.env.overwriteOutput = True
    # arcpy.env.snapRaster = elevation_file
    # arcpy.env.cellSize = elevation_file
    # arcpy.env.cellAlignment = "ALIGN_WITH_INPUT"

    # HILL SHADE TOOL
    # Hillshade (dem, {azimuth}, {altitude}, {z_factor}, {slope_type}, {ps_power}, {psz_factor}, {remove_edge_effect}, {hillshade_type})
    print ("Calling Hillshade function...")
    hill_raster = arcpy.sa.Hillshade(elevation_file)
    hill_raster.save(chap10_raster_data + r"\HillShade_fromPy")   # OUPUT RASTER
    print ("Hillshade process finished.\n")

    # VIEW SHED TOOL
    print ("Calling Viewshed function...")
    observer_fc = chap10_raster_data + r"\Observer"   # POINT FEATURE CLASS
    # Viewshed(in_raster, in_observer_features, {z_factor}, {curvature_correction}, {refractivity_coefficient}, {out_agl_raster})
    viewshed = arcpy.sa.Viewshed(elevation_file, observer_fc)
    viewshed.save(chap10_raster_data + r"\ViewShed_fromPy")   # OUPUT RASTER
    print ("Viewshed process finished.")

except:

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n     " + str(sys.exc_info()[1])

    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    arcpy.AddError(msgs)
    arcpy.AddError(pymsg)

    print (msgs)
    print (pymsg)

    arcpy.AddMessage(arcpy.GetMessages(1))
    print (arcpy.GetMessages(1))
