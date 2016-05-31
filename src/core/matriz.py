# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons


#List Library Import
import csv
import os
import xlrd
import unicodedata
import numpy as np



def convertXLSX(direccion):

	direccionexcel = direccion
	workbook = xlrd.open_workbook(direccionexcel)
	all_worksheets = workbook.sheet_names()

	data = workbook.sheet_by_index(0) #Numero de Sheet donde se encuentran los datos / Sheet data 
	direccioncsv = direccionexcel + '.csv'

	data_emissions = open(''.join([direccioncsv]), 'wb') #crea el csv datos Base / Created CSV data Base
	emissions = csv.writer(data_emissions, delimiter=',') #Abre el CSV para escritura de emsiones / Open CSV write emitions

 	for rownum in xrange(data.nrows):
 		emissions.writerow([entry for entry in data.row_values(rownum)])
 	
 	data_emissions.close()

 	matriz = convertCSV(direccioncsv)
 	return matriz


def convertCSV(direccioncsv):

	matriz = np.genfromtxt(direccioncsv, delimiter=',', dtype=None)
	return  matriz
