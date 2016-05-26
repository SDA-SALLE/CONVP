# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import os
from matriz import *
from wcsv import *
import json
from register import *

def pmc(folder): 
	listEmitions = listaCSV(folder)	

	listEmitionsPM25 = []
	listEmitionsPM10 = []



	for name in listEmitions:
		if 'PM25' in name: 
			listEmitionsPM25.append(name)
		if 'PM10' in name: 
			listEmitionsPM10.append(name)

	
	for i in range (0, len(listEmitionsPM25)):
		archivePM25 = folder + listEmitionsPM25[i]
		archivePM10 = folder + listEmitionsPM10[i]

		MPM25 = convertCSV(archivePM25)
		MPM10 = convertCSV(archivePM10)

		dataMPM25 = {}
		data = {}

		head = MPM25[0,:]

		index = 0
		for value in head: 
			if value == 'ROW': 
				colROW = index
			if value == 'COL':
				colCOL = index
			if value == 'LAT': 
				colLAT = index
			if value == 'LON': 
				colLON = index
			if value == 'POLNAME': 
				colPOL = index
			index += 1 

		for y in range(1, MPM25.shape[0]):
			key = MPM25[y][colROW] + MPM25[y][colCOL]

			if dataMPM25.get(key) is None: 
				dataMPM25[key] = {}
				dataMPM25[key]['GENERAL'] = {'COL': [], 'ROW': [], 'LAT': [], 'LON': [], 'POLNAME': []}
				dataMPM25[key]['hours'] = {}


			if dataMPM25[key]['GENERAL']['COL'] == []:
				dataMPM25[key]['GENERAL']['COL'].append(MPM10[y][colCOL])
				dataMPM25[key]['GENERAL']['ROW'].append(MPM10[y][colROW])
				dataMPM25[key]['GENERAL']['LAT'].append(MPM10[y][colLAT])
				dataMPM25[key]['GENERAL']['LON'].append(MPM10[y][colLON])
				dataMPM25[key]['GENERAL']['POLNAME'].append(MPM10[y][colPOL])

			entryhours = dataMPM25[key]['hours']
			for hour in range(0, 25):
				if entryhours.get(hour) is None: 
					entryhours[hour] = []
			

			hour = 0
			for x in range(6, MPM25.shape[1]): 
				dataMPM25[key]['hours'][hour].append(float(MPM25[y][x])/3600)
				hour += 1

		for y in range(1, MPM10.shape[0]):
			key = MPM10[y][colROW] + MPM10[y][colCOL]

			if data.get(key) is None: 
				data[key] = {}
				data[key]['GENERAL'] = {'COL': [], 'ROW': [], 'LAT': [], 'LON': [], 'POLNAME': []}
				data[key]['hours'] = {}


			if data[key]['GENERAL']['COL'] == []:
				data[key]['GENERAL']['COL'].append(MPM10[y][colCOL])
				data[key]['GENERAL']['ROW'].append(MPM10[y][colROW])
				data[key]['GENERAL']['LAT'].append(MPM10[y][colLAT])
				data[key]['GENERAL']['LON'].append(MPM10[y][colLON])
				data[key]['GENERAL']['POLNAME'].append(MPM10[y][colPOL])

			entryhours = data[key]['hours']
			for hour in range(0, 25):
				if entryhours.get(hour) is None: 
					entryhours[hour] = []
			

			hour = 0
			for x in range(6, MPM10.shape[1]): 
				data[key]['hours'][hour].append(float(MPM10[y][x])/3600)
				hour += 1

		keys = data.keys()
		for key in keys: 
			hours = data[key]['hours'].keys()
			for hour in hours: 
				rest = data[key]['hours'][hour][0] - dataMPM25[key]['hours'][hour][0]
				data[key]['hours'][hour] = []
				data[key]['hours'][hour].append(rest)

		dataMPM25 = None
		noun = 'PM25.csv'
		noun = 'PMC_' + noun 
		PMC(data, noun, folder)

def testingpmc(folder):
	List = listaCSV(folder)
	listPMC = []
	for archive in List:
		if 'PMC' in archive:
			listPMC.append(archive)

	for name in listPMC: 

		MPMC = convertCSV(folder + name)

		for  i in range(1, MPMC.shape[0]):
			for x in range(6, MPMC.shape[1]):

				#print 0 > float(MPMC[i][x])

				if 0 > float(MPMC[i][x]) or 0.0 > float(MPMC[i][x]): 
					print 'Review process number < 0'
				else:
					pass 
					#print 'OK'
