#!/usr/bin/env python
# -*- coding: utf-8 -*-

 ######  ######## ######## ##     ## ########
##    ## ##          ##    ##     ## ##     ##
##       ##          ##    ##     ## ##     ##
 ######  ######      ##    ##     ## ########
      ## ##          ##    ##     ## ##
##    ## ##          ##    ##     ## ##
 ######  ########    ##     #######  ##
import pandas as pd
from subprocess import Popen
SALOME_ROOT='/home/camille/salome_meca/appli_V2016/salome/' # Salome directory
ASTER_ROOT='/opt/aster/bin/' # Aster directory
WORKING_DIR='/media/Calculs/aster-calc-section/' # Working directory
INPUT_FILE='SectionAuto.input' # Filename of the input file
OUTPUT_FILE='SectionAuto.output' # Filename of the output file
TEMP_FILE='Temp.input' # Filename of the temp file (from input to processing)
PROC_FILE='GenPro.py' # Filename of the geometry and meshing script
EXPORT_FILE='SectionAuto.export' # Filename of aster settings
HEADER='NAME,LIEU,A,IY,IZ,AY,AZ,EY,EZ,JX,JG,IYR2,IZR2,RY,RZ,RT' # Header of the output file
HEADER_TEMP='NAME,H,B,Tw,Tf,R' # Header of the temp file
fileInput =  WORKING_DIR + INPUT_FILE # Define input file
fileOutput = WORKING_DIR + OUTPUT_FILE # Define output file
fileTemp = WORKING_DIR + TEMP_FILE # Define temporary file
data = pd.read_csv(fileInput) # Import input data
index = data.index.get_values() # Number of different sections
f = open(fileOutput,"w") # Open output file in write mode
f.write(HEADER + '\n') # Write header for the output file
f.close() # Close output file
##        #######   #######  ########
##       ##     ## ##     ## ##     ##
##       ##     ## ##     ## ##     ##
##       ##     ## ##     ## ########
##       ##     ## ##     ## ##
##       ##     ## ##     ## ##
########  #######   #######  ##
for i in index: # Loop on all sections defined in input file
    f = open(fileTemp,'w') # Open temporary file
    f.write(HEADER_TEMP+'\n') # Write header for the tempory file
    # Write data in the tempory file
    f.write(data['NAME'][i]+','+repr(data['H'][i])+','+repr(data['B'][i])+','+repr(data['Tw'][i])+','+repr(data['Tf'][i])+','+repr(data['R'][i]))
    f.close() # Close tempory file
    ##     ## ########  ######  ##     ##
    ###   ### ##       ##    ## ##     ##
    #### #### ##       ##       ##     ##
    ## ### ## ######    ######  #########
    ##     ## ##             ## ##     ##
    ##     ## ##       ##    ## ##     ##
    ##     ## ########  ######  ##     ##
    # Launch geometry and mesh processing
    salome_run = Popen(SALOME_ROOT + ' -t ' + WORKING_DIR + PROC_FILE, shell='False')
    salome_run.wait()
       ###     ######  ######## ######## ########
      ## ##   ##    ##    ##    ##       ##     ##
     ##   ##  ##          ##    ##       ##     ##
    ##     ##  ######     ##    ######   ########
    #########       ##    ##    ##       ##   ##
    ##     ## ##    ##    ##    ##       ##    ##
    ##     ##  ######     ##    ######## ##     ##
    f = open(fileOutput,"a") # Open output file in append mode
    f.write(data['NAME'][i]+',') # Write name of the next section
    f.close() # Close output file
    # Launch aster calculation
    aster_run = Popen(ASTER_ROOT + 'as_run ' + EXPORT_FILE, shell='False')
    aster_run.wait()
