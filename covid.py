#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup
import lxml
import re
from termcolor import colored
import termtables as tt
import threading, sys, time


def animated_loading():
	for char in ('/-\|'):
		sys.stdout.write('\r' + 'gathering data...' + char)
		time.sleep(.1)
		sys.stdout.flush()

		
def parser(elem):
    line = "".join(elem.splitlines())
    dat = re.findall(r"\>(.*?)\<", line)
    return dat


def main():
    page = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data')
    soup = BeautifulSoup(page.content, 'lxml')
    tbody = soup.find('tbody')

    n = 0
    array = []
    for i in tbody:
        if n == 231:
            break
        else:
            data = []
            if i.find('<tr>') != -1:
                arr = parser(str(i))
                data = [i for i in arr if isinstance(i, str) and len(i) != 0 and i[0] != '[']
                n += 1
                array.append(data)

    arr = [i for i in array if len(i) == 4]

    table = tt.to_string(
		arr,
		header=['Country', colored('Infected', 'yellow'), colored('Deaths', 'red'), colored('Recovered', 'green')],
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
    
