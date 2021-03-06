#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup
import lxml
import re
from termcolor import colored
import termtables as tt
import sys


north_america = ['Antigua and Barbuda', 'The Bahamas', 'Barbados', 'Canada', 'Cuba', 'Dominica', 'Dominican Republic',
                 'Grenada', 'Haiti', 'Jamaica', 'Mexico', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines',
                 'Trinidad and Tobago', 'United States', 'Anguilla', 'Saint Pierre and Miquelon', 'Montserrat', 'Greenland']

south_america = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay',
                 'Peru', 'Suriname', 'Uruguay', 'Venezuela', 'French Guiana', 'Falkland Islands']

central_america = ['Belize', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panama']

asia = ['Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei',
         'Cambodia', 'China', 'East Timor', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq',
         'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon',
         'Malaysia', 'Maldives', 'Mongolia', 'Myanmar', 'Nepal', 'North Korea', 'Oman',
         'Pakistan', 'Philippines', 'Palestine', 'Qatar', 'Saudi Arabia', 'Singapore', 'South Korea',
         'Sri Lanka', 'Syria', 'Tajikistan', 'Thailand', 'Turkey', 'Turkmenistan', 'Taiwan',
         'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen']

europe = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria',
           'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany',
           'Greece', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania',
           'Luxembourg', 'North Macedonia', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Norway',
           'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain',
           'Sweden', 'Switzerland', 'Ukraine', 'United Kingdom', 'Vatican City', 'Saba']

oceania = ['Australia', 'Federated States of Micronesia', 'Fiji', 'Kiribati', 'Marshall Islands',
            'Nauru', 'New Zealand', 'Palau', 'Papua New Guinea', 'Samoa', 'Solomon', 'Tonga', 'Tuvalu', 'Vanuatu']

africa = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde',
           'Central African Republic', 'Chad', 'Comoros', 'Republic of the Congo', 'Democratic Republic of the Congo',
           "Côte d'Ivoire", 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'The Gambia', 'Ghana',
           'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania',
           'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'São Tomé and Príncipe', 'Senegal',
           'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Swaziland', 'Tanzania', 'Togo',
           'Tunisia', 'Uganda', 'Western Sahara', 'Zambia', 'Zimbabwe']


def filter(arr, countries_array):
    main_arr = []
    pos = 1
    for i in arr:
        if i[0] in countries_array:
            i.insert(0, pos)
            main_arr.append(i)
            pos += 1

    return main_arr


def print_table(arr):
    table = tt.to_string(
		    arr,
		    header=['Pos', 'Country', colored('Infected', 'yellow'), colored('Deaths', 'red'), colored('Recovered', 'green')],
		    style=tt.styles.ascii_thin_double,
		    alignment="c"
	    )
    print(table)


def find_info(elem):
    line = "".join(elem.splitlines())
    dat = re.findall(r"\>(.*?)\<", line)
    return dat


def main():
    args = sys.argv

    try:
        page = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data')
    except (requests.ConnectionError, requests.Timeout) as exception:
        print('\nConnection Error')
        quit()
          
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
                arr = find_info(str(i))
                data = [i for i in arr if isinstance(i, str) and len(i) != 0 and i[0] != '[']
                n += 1
                array.append(data)
            

    arr = [i for i in array if len(i) == 4]
    
    if len(args) == 1:
        pos = 0
        for i in arr:
            if i[0] != 'World':
                i.insert(0, pos)
            else:
                i.insert(0, '-')                
            pos += 1

        print_table(arr)

    elif args[1] == 'north':
        data = filter(arr, north_america)
        print_table(data)

    elif args[1] == 'south':
        data = filter(arr, south_america)
        print_table(data)

    elif args[1] == 'central':
        data = filter(arr, central_america)
        print_table(data)
        
    elif args[1] == 'europe':
        data = filter(arr, europe)
        print_table(data)

    elif args[1] == 'oceania':
        data = filter(arr, oceania)
        print_table(data)

    elif args[1] == 'asia':
        data = filter(arr, asia)
        print_table(data)

    elif args[1] == 'africa':
        data = filter(arr, africa)
        print_table(data)
        
    else:
        print('Unknown Argument')
        quit()


if __name__ == '__main__':
    main()