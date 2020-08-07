#!/usr/bin/env python3

# web scraping
import urllib.request
from bs4 import BeautifulSoup

# color
from termcolor import colored

# regex
import re

# table
import termtables as tt

# other
import threading, sys, time


def sort_infected(elem):
	return elem[1]


def animated_loading():
	for char in ('/-\|'):
		sys.stdout.write('\r' + 'gathering data...' + char)
		time.sleep(.1)
		sys.stdout.flush()


def find_string(elem):
	line = re.findall(r"\>(.*?)\<", elem)
	for i in line:
		if i in ('Confirmed cases', 'Recovered', 'Deaths'):
			return line
		

def main():
	lista = sys.argv
	countries = []
	if len(lista) == 1:
		print('Unknown Argument')
		quit()

	elif lista[1] == 'south':
		countries = ['Argentina', 'Bolivia', 'Brazil',
				          'Colombia', 'Ecuador', 'Guyana',
				          'Paraguay', 'Peru', 'Suriname',
				          'Uruguay', 'Venezuela', 'French_Guiana']

	elif lista[1] == 'central':
		 countries = ['El_Salvador', 'Costa_Rica', 'Belize',
		                   'Guatemala', 'Honduras', 'Nicaragua', 'Panama']

	elif lista[1] == 'north':
		pass

	elif lista[1] == 'europe':
		countries = ['Austria', 'Italy', 'Belgium', 'Latvia',
                          'Bulgaria', 'Lithuania', 'Croatia', 'Luxembourg',
						  'Cyprus',	'Malta', 'Czechia', 'Netherlands',
 						  'Denmark', 'Poland', 'Estonia', 'Portugal',
						  'Finland', 'Romania', 'France', 'Slovakia'
						  'Germany', 'Slovenia', 'Greece', 'Spain'
						  'Hungary', 'Sweden', 'Ireland']

	elif lista[1] == 'asia':
		pass

	elif lista[1] == 'ocean':
		pass

	else:
		print('Unknown Argument')
		quit()

	data = []

	for i in countries:
		datos = urllib.request.urlopen('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_' + i)
		soup = BeautifulSoup(datos, features="html.parser")
		tags = soup('tr')
		lista = []

		for tag in tags:
			string = str(tag)
			if string.find('Confirmed cases') != -1:
				lista.append(string)
			elif string.find('Recovered') != -1:
				lista.append(string)
			elif string.find('Deaths') != -1:
				lista.append(string)
				break

		final = list(map(find_string, lista))
		numbers = []
		for n in final:
			if n is not None:
				for j in n:
					if len(j) != 0 and j[0].isnumeric():
						numbers.append(int(j.replace(',', '')))

		numbers.insert(0, i)
		data.append(numbers)

	# sort by infected
	data.sort(key=sort_infected, reverse=True)

	table = tt.to_string(
		data,
		header=['Country', colored('Infected', 'yellow'), colored('Recovered', 'green'), colored('Deaths', 'red')],
		style=tt.styles.ascii_thin_double,
		alignment="c"
	)

	print('\n', table)


if __name__ == '__main__':
	the_process = threading.Thread(name='process', target=main)
	the_process.start()
	while the_process.is_alive():
		animated_loading()
	print()
