# -*- coding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import sys
import json
sys.path.append('core')
from matriz import *
from wcsv import *


def emisionsconvp(archive): 
	
	archiveConstants = os.path.join('..', 'data', 'in', 'constants', 'FE.xlsx')
	Mconstants = convertXLSX(archiveConstants)
	constants = {}
	for i in range(1, Mconstants.shape[0]):
		if constants.get(Mconstants[i][0]) is None:
			constants[Mconstants[i][0]] = round(Mconstants[i][1], 6)
	Mconstants = None

	for name in constants.keys():
		if 'PM25' in name:
			PM25 = name
		elif 'PM10' in name:
			PM10 = name

	matriz = convertXLSX(archive)
	head = matriz[0,:]
	index = 0
	for value in head: 
		if value == 'FID' or value == 'ID':
			colID = index
		if value == 'FID_Grilla':
			colGrid = index
		if value == 'ROW': 
			colROW = index
		if value == 'COL':
			colCOL = index
		if value == 'LAT': 
			colLAT = index
		if value == 'LON': 
			colLON = index
		if 'AREA' in value: 
			colAREA = index
		if value == 'Dias' or value == 'DIAS' or value == 'dias':
			colDAYS = index
		index += 1
	head = None

	data = {}
	for i in range(1, matriz.shape[0]): 
		key = int(float(matriz[i][colID]))
		if data.get(key) is None: 
			data[key] = {'General': {'COL': [], 'ROW': [], 'LAT': [], 'LON': [], 'FID_Grilla': [], 'AREA': [], 'DAYS': []}, 'Emisions': {'SEG': [], 'PM25':{'g/proyecto': [], 'E': [], 'g': [], 't': []}, 'PM10':{'g/proyecto': [], 'E': [], 'g': [], 't': []}}}

		if data[key]['General']['COL'] == []:
			data[key]['General']['COL'].append(int(float(matriz[i][colCOL])))
			data[key]['General']['ROW'].append(int(float(matriz[i][colROW])))
			data[key]['General']['LAT'].append(matriz[i][colLAT])
			data[key]['General']['LON'].append(matriz[i][colLON])
			data[key]['General']['FID_Grilla'].append(int(float(matriz[i][colGrid])))
			data[key]['General']['AREA'].append(float(matriz[i][colAREA]))
			data[key]['General']['DAYS'].append(int(float(matriz[i][colDAYS])))

		#Calculation SEG
	 	data[key]['Emisions']['SEG'].append(data[key]['General']['DAYS'][0] * 11 * 60 * 60)

	 	#g/proyect calculation 
	 	data[key]['Emisions']['PM25']['g/proyecto'].append(data[key]['General']['AREA'][0] * data[key]['Emisions']['SEG'][0] * constants[PM25])
	 	data[key]['Emisions']['PM10']['g/proyecto'].append(data[key]['General']['AREA'][0] * data[key]['Emisions']['SEG'][0] * constants[PM10])

	 	#Emisions
	 	data[key]['Emisions']['PM25']['E'].append(data[key]['Emisions']['PM25']['g/proyecto'][0] / data[key]['General']['DAYS'][0])
	 	data[key]['Emisions']['PM10']['E'].append(data[key]['Emisions']['PM10']['g/proyecto'][0] / data[key]['General']['DAYS'][0])

	 	#g/Year
	 	data[key]['Emisions']['PM25']['g'].append(data[key]['Emisions']['PM25']['E'][0] * data[key]['General']['DAYS'][0])
	 	data[key]['Emisions']['PM10']['g'].append(data[key]['Emisions']['PM10']['E'][0] * data[key]['General']['DAYS'][0])

	 	#T/Year
	 	data[key]['Emisions']['PM25']['t'].append(data[key]['Emisions']['PM25']['g'][0]/1000000)
	 	data[key]['Emisions']['PM10']['t'].append(data[key]['Emisions']['PM10']['g'][0]/1000000)

	folder = os.path.join('..', 'data', 'out', 'emisions', '')
	writeEmisions(data, folder)

def emisionsTYear(archive):

	MEmisions = convertCSV(archive)
	head = MEmisions[0,:]
	index = 0
	for value in head: 
		if value == 'PM25(t)': 
			colPM25 = index
		if value == 'PM10(t)':
			colPM10 = index
		index += 1

	head = None
	ETYearPM25 = 0
	ETYearPM10 = 0

	for i in range(1, MEmisions.shape[0]):
		ETYearPM25 += float(MEmisions[i][colPM25])
		ETYearPM10 += float(MEmisions[i][colPM10])

	folder = os.path.join('..', 'data', 'out', 'emisions', '')
	writeEmisionsTYear(ETYearPM25, ETYearPM10, folder)






