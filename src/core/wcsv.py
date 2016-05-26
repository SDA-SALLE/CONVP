#created by @ceapalaciosal
#under code Creative Commons
# -*- encoding: utf-8 -*-

#! /usr/bin/env python
import csv
import os
import xlrd

def writeEmisions(data, folder): 
	
	csvsalida = open(folder + 'Emisions.csv', 'w')
	
	names = ['ID', 'FID_Grilla', 'ROW', 'COL', 'LAT', 'LON', 'AREA', 'Dias', 'Seg', 'PM25(g/proyecto)', 'PM25 (E(g/d))', 'PM25(g)', 'PM25(t)',  'PM10(g/proyecto)', 'PM10 (E(g/d))', 'PM10(g)', 'PM10(t)']
	for name in names: 
		if name == 'ID':
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	
	csvsalida.write('\n')
	keys = data.keys()
	for key in keys: 
		csvsalida.write(str(key))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['FID_Grilla'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['ROW'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['COL'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['LAT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['LON'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['AREA'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['General']['DAYS'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['SEG'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM25']['g/proyecto'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM25']['E'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM25']['g'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM25']['t'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM10']['g/proyecto'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM10']['E'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM10']['g'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['Emisions']['PM10']['t'][0]))
		csvsalida.write('\n')
	csvsalida.close()

def writeEmisionsTYear(ETYearPM25, ETYearPM10, folder):
	csvsalida = open(folder + 'EmisionsTYear.csv', 'w')
	names = ['ETYearPM25', 'ETYearPM10']
	for name in names: 
		if name == 'ETYearPM25':
			csvsalida.write(name)
		else: 
			csvsalida.write(',')
			csvsalida.write(name)
	csvsalida.write('\n')

	csvsalida.write(str(ETYearPM25))
	csvsalida.write(',')
	csvsalida.write(str(ETYearPM10))
	csvsalida.write('\n')
	csvsalida.close()

def writeDesagregation(data): 

	folder = os.path.join('..', 'data', 'out', 'desagregation', '')
	archives = ['PM25', 'PM10']

	names = ['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h']
	for archive in archives:
		csvsalida = open(folder + archive + '.csv', 'w')

		for name in names: 
			if name == 'ROW':
				csvsalida.write(name)
			else: 
				csvsalida.write(',')
				csvsalida.write(name)

		csvsalida.write('\n')
		keys = data.keys()
		for key in keys: 
			csvsalida.write(str(data[key]['General']['ROW'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['COL'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['LAT'][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key]['General']['LON'][0]))
			csvsalida.write(',')
			if 'PM25' in archive:
				csvsalida.write('PM25')
			elif 'PM10' in archive:
				csvsalida.write('PM10')
			csvsalida.write(',')
			csvsalida.write('g/h')
			hours = data[key][archive].keys()
			for hour in hours:
				csvsalida.write(',')
				csvsalida.write(str(data[key][archive][hour][0]))
			csvsalida.write(',')
			csvsalida.write(str(data[key][archive][0][0]))
			csvsalida.write('\n')

def PMC(data, noun, folder):

	folder = os.path.join('..', 'data', 'out','speciation', '')
	csvsalida = open(folder + noun, 'w')
	salida = csv.writer(csvsalida, delimiter=',')
	keys = data.keys()

	salida.writerow(["ROW", "COL", "LAT", "LON", "POLNAME", "UNIT", "E00h", "E01h", "E02h", "E03h", "E04h", "E05h", "E06h" ,"E07h", "E08h", "E09h", "E10h", "E11h", "E12h", "E13h", "E14h", "E15h", "E16h", "E17h", "E18h", "E19h", "E20h", "E21h", "E22h", "E23h", "E24h"])
	for key in keys: 
		csvsalida.write(str(int(data[key]['GENERAL']['ROW'][0])))
		csvsalida.write(',')
		csvsalida.write(str(int(data[key]['GENERAL']['COL'][0])))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['LAT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['LON'][0]))
		csvsalida.write(',')
		csvsalida.write('PMC')
		csvsalida.write(',')
		csvsalida.write('g/s')
		hours = data[key]['hours'].keys()
		for hour in hours:
			csvsalida.write(',')
			csvsalida.write(str(data[key]['hours'][hour][0]))
		csvsalida.write('\n')
			
	csvsalida.close()

def writespeciation(data, namearchive, namespecie):
	folder = os.path.join('..', 'data', 'out', 'speciation', '')
	csvsalida = open(folder + namespecie + '_' + namearchive, 'w')
	salida = csv.writer(csvsalida, delimiter=',')

	salida.writerow(['ROW', 'COL', 'LAT', 'LON', 'POLNAME', 'UNIT', 'E00h', 'E01h', 'E02h', 'E03h', 'E04h', 'E05h', 'E06h' ,'E07h', 'E08h', 'E09h', 'E10h', 'E11h', 'E12h', 'E13h', 'E14h', 'E15h', 'E16h', 'E17h', 'E18h', 'E19h', 'E20h', 'E21h', 'E22h', 'E23h', 'E24h'])

	keys = data.keys()
	for key in keys:
		csvsalida.write(str(data[key]['GENERAL']['ROW'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['COL'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['LAT'][0]))
		csvsalida.write(',')
		csvsalida.write(str(data[key]['GENERAL']['LON'][0]))
		csvsalida.write(',')
		csvsalida.write(namespecie)
		csvsalida.write(',')
		csvsalida.write('g/s')
		csvsalida.write(',')
		hours = data[key]['hours'].keys()
		for hour in hours:
			csvsalida.write(data[key]['hours'][hour][0])
			if hour != 24:
				csvsalida.write(',')
		csvsalida.write('\n')
	csvsalida.close()


