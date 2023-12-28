# Elevation Grid Homework Script

# Created by: Ugochukwu Udonna Okonkwo
# Created on: 4/2/2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = r"C:\Geog_432\EsriPress\Python\Data\Colorado"
    elevation_grid = r"C:\Geog_432\EsriPress\Python\Data\Colorado\Elevation"
    if arcpy.CheckExtension('spatial') == 'Available':
        arcpy.CheckOutExtension('spatial')
        # Slope(in_raster, {output_measurement}, {z_factor}, {method}, {z_unit}, {analysis_target_device})
        slope_raster = arcpy.sa.Slope(elevation_grid,"DEGREE")
    # Reclassify Demo
    if arcpy.CheckExtension('spatial') == 'Available':
        arcpy.CheckOutExtension('spatial')
        # RemapRange (remapTable)
        remap_range = arcpy.sa.RemapRange([[0,5,1], [5,90,0]])
        # Reclassify(in_raster, reclass_field, remap, {missing_values})
        out_raster = arcpy.sa.Reclassify(slope_raster, 'Value', remap_range)
        print ('Saving raster object...')
        out_raster.save(r'c:\temp\reclass_demo.img')
        arcpy.CheckInExtension('spatial')
    else:
        print ('Spatial Analyst extension not present.')





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
