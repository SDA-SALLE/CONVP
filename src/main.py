# -*- coding: utf-8 -*-
#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
import sys
sys.path.append('core')
from clear import *
from emisions import *
from desagregation import *
from register import *
from speciation import *
from PMC import *

folder = os.path.join('..', 'data', 'out', '')
clear(folder)

#Archive CONVP in folder /data/in/CONVP.xlsx
archive = os.path.join('..', 'data', 'in', 'CONVP.xlsx')
emisionsconvp(archive)

#T/Year
archive = os.path.join('..', 'data', 'out', 'emisions', 'Emisions.csv')
emisionsTYear(archive)

#desagregation Hour
archive = os.path.join('..', 'data', 'out', 'emisions', 'Emisions.csv')
#final(archive)
desagregation(archive)


#unions
folderDesagregation = os.path.join('..', 'data', 'out', 'desagregation', '')
archives = listaCSV(folderDesagregation)
#print archives
for archive in archives:
    #print archive
    archive = folderDesagregation + archive
    final(archive)

print 'Start speciation CONVP'

#Speciation
archivespeciation = os.path.join ('..', 'data', 'in', 'PE', 'BLD_CONVP_SCP_PROF_PM25.xlsx')
folderCONVP = os.path.join('..','data', 'out', 'desagregation', '')
speciation(archivespeciation, folderCONVP)

#PMC
folderout = os.path.join('..','data', 'out', 'speciation', '')
folderPMC = os.path.join('..','data', 'out', 'desagregation', '')
pmc(folderPMC)
testingpmc(folderout)