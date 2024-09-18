#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: Ross Unruh
    Description:  This code gives the length in miles of any river included inside a buffered ecoregion in Kansas.
    Date created: 09/17/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = r"C:\Users\runru\Desktop\Classes\Fall 2024\GEOG 728\Exercises\Exercise #5\firstpythonscript-RossUnruh\GitHub-FirstPythonScript\ExerciseData.gdb"

# Perform geoprocessing

# Use select by attributes tool to select the name of one of the ecoregions.
selectEcoregion = arcpy.management.SelectLayerByAttribute('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'High Plains'")

# Create a 10km buffer around the selected ecoregion.
arcpy.analysis.Buffer('ks_ecoregions', 'outBuffer', '10 kilometers')

# Clip the river(s) to the new buffer
arcpy.analysis.Clip('ks_major_rivers', 'outBuffer', 'outClip')

# Add a new column in the outClip shapefile which converts the contents of the Shape_Length column from feet to miles.
arcpy.management.AddGeometryAttributes('outClip', 'LENGTH', 'MILES_US')

# Copy the new outClip output and rename it totalMiles.
arcpy.management.CopyFeatures('outClip','totalMiles')



