# Name: annulus40.py  (Non Parallel)
# Description: runs neighborhood analysis using focal stats with 40 annuli around grid cells
# Need annulus calculations for input
# March 2013 by D Duriscoe NPS Night Sky Program and D Theobald
# Revised Nov 2015 for VIIRS day/night band input
# 2022 - 03 - 22 Run the final 2019 and 2020 CONUS files
# Revised May 2025 by Zach Vanderbosch (NPS Night Skies Program)

# to run open python command prompt from ArcGIS start menu
# example call:
# (arcgispro-py3) C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3>python 
#  d:/sAnderson/salr/annulus40_np_CONUS.py  -- one line

# Import system modules
import os
import sys
import json
import time
import arcpy

# Define directories for sALR modeling
salrBase = "C:/Users/zvanderbosch/data/sALR"
inputDir = f"{salrBase}/sALR_inputs"
outputDir = f"{salrBase}/sALR_outpus"

# Define year for analysis. 
# An empty string will analyze all years available.
year = "2024"

# Setup the arcpy environment
arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = f"{salrBase}/wksp"
arcpy.env.overwriteOutput = True
arcpy.env.rasterStatistics = 'STATISTICS 1 1 (-999)'

# Load in ring properties. Line format of dict is
# ring_number: [inner_radius, outer_radius, weight]
with open(f'{inputDir}/ring_params.json') as f:
    ring_params = json.load(f)
numrings = len(ring_params)
  
# Define raster for input, VIIRS day/night band
# values less than 0.5 nano-watts set to zero
# projected over to Albers USGS
file = f'{inputDir}/CONUS_{year}_viirs.tif'
if os.path.isfile(file):
    print(f"{file} does not exist!")
    sys.exit(1)
print(f'Processing {file}')

# Loop through all rings
print(f"Number of rings = {numrings}")
completed_rings = []
for ringnum in range(1,numrings+1):

    print(f'Ring Number = {ringnum:2d}, {time.strftime("%c")}')

    # Retrieve current ring parameters
    ringIn = ring_params[str(ringnum)][0]
    ringOut = ring_params[str(ringnum)][1]
    wfact = ring_params[str(ringnum)][2]
    if ringIn == 0.0:
        ringIn = 500.0

    # Skip over rings with undefined radii
    if ringIn == -999.0:
        continue

    # Run focal stats command with defined annulus region
    neighborhood = arcpy.sa.NbrAnnulus(ringIn, ringOut, "MAP")
    rann = arcpy.sa.FocalStatistics(file, neighborhood, "SUM", "DATA")

    # Multiply ring grid by weighting factor
    rannw = rann * wfact

    # Save in workspace folder
    ringName = f"r{ringnum}"
    rannw.save(ringName)
    completed_rings.append(ringName)


# Sum all ring grids
print("Running Sum...")
rA = sum([arcpy.sa.Raster(r) for r in completed_rings])

# Calibrate to ALR based upon southern california 
# Feb-2015 observations shown in 2015 sALR paper
rAc = rA * 0.00177708

# Save to file
sumFile = f"{outputDir}/salr_{year}.tif"
rAc.save(sumFile)
print( "Done - ALR Processing", sumFile, time.strftime("%c"))