#!/usr/bin/env python
""" A script to read in the CMT information and output a mineos file 

created by: Adam Ringler
updated: Kimberly Schramm
T
his code gets CMTs from Lamont and sets up a directory structure.
The code pulls ndk format CMTs and switches them to CMTSOLUTION and 
mineos format.

This script has dependencies that may require updating of
your .bashrc $PATH variable. 
 
Additionally, it will be creating ~/synInfo/croncode/qcmt.ndk.  If 
you want this in a different location you will need to edit the code.
You will also need to update the maksynCMT.py code with your desired path.
"""

import os
import sys
import datetime
import math

<<<<<<< HEAD
#Debug flag for verbose output during run
debug = True

# this is the path where the synthetics will be created.
cmtdirpath = '/home/kschramm/SYNTHETICS'
# this is the path where it will output information about all of the data it is 
# getting. at the moment it is set to a directory in the user's home
codepath = os.getenv('HOME')+'/synInfo'

=======
debug = True

# this is the path where the synthetics will be created.
cmtdirpath = '/home/aringler/synthetics/SYNTHETICS'
# this is the path where it will output information about all of the data it is 
# getting. at the moment it is set to a directory in the user's home
codepath = '/home/aringler/synthetics/syncomppython/synInfo'
>>>>>>> origin/master
minmag= 6.5

#Download the latest CMT files and place them in the croncode location
currdir = os.getcwd()
if not os.path.exists(codepath + '/croncode'):
    os.mkdir(codepath + '/croncode')
os.chdir(codepath + '/croncode')
#This only gets the most recent quick CMTs for the older CMTS you need to backfill
if backfill:
	os.system('wget -N http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/jan76_dec10.ndk')
else:
	os.system('wget -N http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/NEW_QUICK/qcmt.ndk')
os.chdir(currdir)

#Read in the CMT file
if backfill:
	qcmt = open(codepath + '/croncode/jan76_dec10.ndk','r')
else:
	qcmt = open(codepath + '/croncode/qcmt.ndk','r')

#Lets loop through the code reading 5 lines at a time and pull apart the ndk event info
while True:
<<<<<<< HEAD
	line1 = qcmt.readline()
	line2 = qcmt.readline()
	line3 = qcmt.readline() 
	line4 = qcmt.readline()
	line5 = qcmt.readline()

#If we dont have a line 2 then we are done with the file
	if not line2: break
	mag1 = float(line1[49:51])	
	mag2 = float(line1[52:55])
	mag = max(mag1,mag2)

#Lets only look at CMTs with a certain magnitude
	if mag >= minmag:
		if debug:
			print 'Magnitude:' + str(mag)

#Transform into MINEOS format		
		CMTdate = datetime.datetime(int(line1[5:9]), int(line1[10:12]), int(line1[13:16]),0,0,0)
		if debug:
			print 'Here is the day of year ' + str(CMTdate.timetuple()[7])

#Now we format the lines from the line info
#This should probably be split.  However it is such a messy format we will stick to this
		line1CMT = line2[0:14].strip() +  ' ' + line1[5:9] + ' ' + str(CMTdate.timetuple()[7]) + ' '
		line1CMT = line1CMT + line1[16:18] + ' ' + line1[19:21] + ' ' + line1[22:26].ljust(5,'0') + ' '
		line1CMT = line1CMT + line1[26:33] + ' ' + line1[34:41] + ' ' + line1[42:47].strip() + ' 1.0 '
		line1CMT = line1CMT + line2[75:80].strip()
		line4 = line4.split()
		line3 = line3.split()
		CMTexp = line4[0]
		if debug:
			print 'CMTexp:' + CMTexp
#Pull out the CMT components
		Mrr = float(line4[1])
		Mtt = float(line4[3])
		Mpp = float(line4[5])
		Mrt = float(line4[7])
		Mrp = float(line4[9])
		Mtp = float(line4[11])
#Lets get the moment magnitude and split this out
		M0 = math.sqrt(Mrr**2 + Mtt**2 + Mpp**2 + 2*(Mrp**2 + Mtp**2 + Mrt**2))/math.sqrt(2)
		M0 = str('{0:.3f}'.format(M0)) + 'e' + CMTexp
		if debug:
			print line1CMT 
			print 'M0=' + M0
		line5 = line5.split()
		line1CMT = line1CMT + ' ' + M0 + ' ' + str(Mrr) + ' ' + str(Mtt) + ' ' + str(Mpp) + ' ' + str(Mrt)
		line1CMT = line1CMT + ' ' + str(Mrp) + ' ' + str(Mtp) + ' 1.0e' + CMTexp + ' ' + line5[11] + ' '
		line1CMT = line1CMT + line5[12] + ' ' + line5[13] + ' ' + line5[14] + ' ' + line5[15] + ' ' + line5[16]	+ '\n'
=======
    line1 = qcmt.readline()
    line2 = qcmt.readline()
    line3 = qcmt.readline() 
    line4 = qcmt.readline()
    line5 = qcmt.readline()
    if not line2: break
    mag1 = float(line1[49:51])    
    mag2 = float(line1[52:55])
    mag = max(mag1,mag2)
#Lets only look at CMTs with a certain magnitude
    if mag >= minmag:
        if debug:
            print 'Magnitude:' + str(mag)
#Transform into MINEOS format        
        CMTdate = datetime.datetime(int(line1[5:9]), int(line1[10:12]), int(line1[13:16]),0,0,0)
        if debug:
            print 'Here is the day of year ' + str(CMTdate.timetuple()[7])
        line1CMT = line2[0:14].strip() +  ' ' + line1[5:9] + ' ' + str(CMTdate.timetuple()[7]) + ' '
        line1CMT = line1CMT + line1[16:18] + ' ' + line1[19:21] + ' ' + line1[22:26].ljust(5,'0') + ' '
        line1CMT = line1CMT + line1[26:33] + ' ' + line1[34:41] + ' ' + line1[42:47].strip() + ' 1.0 '
        line1CMT = line1CMT + line2[75:80].strip()
        line4 = line4.split()
        line3 = line3.split()
        CMTexp = line4[0]
        if debug:
            print 'CMTexp:' + CMTexp
        Mrr = float(line4[1])
        Mtt = float(line4[3])
        Mpp = float(line4[5])
        Mrt = float(line4[7])
        Mrp = float(line4[9])
        Mtp = float(line4[11])
        M0 = math.sqrt(Mrr**2 + Mtt**2 + Mpp**2 + 2*(Mrp**2 + Mtp**2 + Mrt**2))/math.sqrt(2)
        M0 = str('{0:.3f}'.format(M0)) + 'e' + CMTexp
        if debug:
            print line1CMT 
            print 'M0=' + M0
        line5 = line5.split()
        line1CMT = line1CMT + ' ' + M0 + ' ' + str(Mrr) + ' ' + str(Mtt) + ' ' + str(Mpp) + ' ' + str(Mrt)
        line1CMT = line1CMT + ' ' + str(Mrp) + ' ' + str(Mtp) + ' 1.0e' + CMTexp + ' ' + line5[11] + ' '
        line1CMT = line1CMT + line5[12] + ' ' + line5[13] + ' ' + line5[14] + ' ' + line5[15] + ' ' + line5[16]    + '\n'
>>>>>>> origin/master
# kas - added a \n to the end of line1CMT.  Mineos needs to have an EOL or you 
# get a fortran runtime error.

        
#Put in event directory
        if not os.path.exists(cmtdirpath + '/' + line1[5:9]):
            os.mkdir(cmtdirpath + '/' + line1[5:9])
        cmtdire = cmtdirpath + '/' + line1[5:9] + '/' + line2[0:14]
        cmtdire = cmtdire.strip()
        if not os.path.exists(cmtdire):
            os.mkdir(cmtdire)

<<<<<<< HEAD
#Here we write the Mineos solution and close the file
		CMTmineos = open(cmtdire  + '/currCMTmineos','w')
		CMTmineos.write(line1CMT)
		CMTmineos.close()

#Lets also open the CMTSOLUTION and get ready to write this result
		CMTSol = open(cmtdire + '/CMTSOLUTION','w')
		line1CMTSol = line1[0:3] + ' ' + str(int(line1[5:9])) + ' ' + line1[10:12]+ ' ' + line1[13:16] + ' '
		line1CMTSol = line1CMTSol + line1[16:18] + ' ' + line1[19:21] + ' ' + line1[22:26].ljust(5,'0')
		line1CMTSol = line1CMTSol + ' ' + line1[27:33] + ' ' + line1[34:41] + ' ' + line1[42:47] + ' '
		line1CMTSol = line1CMTSol + str(format(mag1,'1.1f')) + ' ' + str(format(mag2,'1.1f'))+ '\n'

#Here we writ the CMTSOLUTION format
		CMTSol.write(line1CMTSol)
		CMTSol.write('event name:' + line2[1:14].rjust(18,' ') + '\n')
		CMTSol.write('time shift:' + (line3[1].rjust(9,' ')).ljust(12,'0') + '\n')
		CMTSol.write('half duration:' + line2[75:80].strip().ljust(7,'0').rjust(9,' ') + '\n')
		CMTSol.write('latitude:' + line1[27:33].rjust(14, ' ') + '\n')
		CMTSol.write('longitude:' + line1[34:41].strip().rjust(13, ' ') + '\n')
		CMTSol.write('depth:' + ((line1[43:47]).strip().ljust(7,'0')).rjust(17,' ') + '\n')
		CMTSol.write('Mrr:' + str(format(Mrr*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
		CMTSol.write('Mtt:' + str(format(Mtt*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
		CMTSol.write('Mpp:' + str(format(Mpp*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
		CMTSol.write('Mrt:' + str(format(Mrt*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
		CMTSol.write('Mrp:' + str(format(Mrp*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
		CMTSol.write('Mtp:' + str(format(Mtp*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
		CMTSol.write('\n')
		CMTSol.close()
=======
        CMTmineos = open(cmtdire  + '/currCMTmineos','w')
        CMTSol = open(cmtdire + '/CMTSOLUTION','w')
        CMTmineos.write(line1CMT)
        CMTmineos.close()
        line1CMTSol = line1[0:3] + ' ' + str(int(line1[5:9])) + ' ' + line1[10:12]+ ' ' + line1[13:16] + ' '
        line1CMTSol = line1CMTSol + line1[16:18] + ' ' + line1[19:21] + ' ' + line1[22:26].ljust(5,'0')
        line1CMTSol = line1CMTSol + ' ' + line1[27:33] + ' ' + line1[34:41] + ' ' + line1[42:47] + ' '
        line1CMTSol = line1CMTSol + str(format(mag1,'1.1f')) + ' ' + str(format(mag2,'1.1f'))+ '\n'
        CMTSol.write(line1CMTSol)
        CMTSol.write('event name:' + line2[1:14].rjust(18,' ') + '\n')
        CMTSol.write('time shift:' + (line3[1].rjust(9,' ')).ljust(12,'0') + '\n')
        CMTSol.write('half duration:' + line2[75:80].strip().ljust(7,'0').rjust(9,' ') + '\n')
        CMTSol.write('latitude:' + line1[27:33].rjust(14, ' ') + '\n')
        CMTSol.write('longitude:' + line1[34:41].strip().rjust(13, ' ') + '\n')
        CMTSol.write('depth:' + ((line1[43:47]).strip().ljust(7,'0')).rjust(17,' ') + '\n')
        CMTSol.write('Mrr:' + str(format(Mrr*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
        CMTSol.write('Mtt:' + str(format(Mtt*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
        CMTSol.write('Mpp:' + str(format(Mpp*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
        CMTSol.write('Mrt:' + str(format(Mrt*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
        CMTSol.write('Mrp:' + str(format(Mrp*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
        CMTSol.write('Mtp:' + str(format(Mtp*10**int(CMTexp),'1.6e')).rjust(19,' ') + '\n')
        CMTSol.write('\n')
        CMTSol.close()
>>>>>>> origin/master
qcmt.close()

