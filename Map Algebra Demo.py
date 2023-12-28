# Map Algebra Demo

# Created by: Alyssa
# Created on: 3-37-23

print ("Importing modules...")
import sys, arcpy, traceback
try:
    arcpy.env.overwriteOutput = True
    if arcpy.CheckExtension('Spatial') == 'Available':
        input_raster = r'C:\EsriPress\Python\Data\Colorado\elevation'
        arcpy.CheckOutExtension('Spatial')
        raster_out = arcpy.sa.Raster(input_raster)
         #3.2808399
        raster_out = raster_out * 3.2808399
        raster_out.save(r'c:\temp\math.tif')
        arcpy.CheckInExtension('Spatial')
    else:
        print ('Spatial Analyst not present.')
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
