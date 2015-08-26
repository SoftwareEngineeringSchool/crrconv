#!/usr/bin/python
import requests
import sys
import termcolor
from termcolor import colored
import colorama
from colorama import Back, Style
colorama.init()
start = "\033[3;5m"
end = "\033[0;0m"

a = sys.argv[1]
a = a.upper()

b = sys.argv[2]
b = b.upper()

c = float(sys.argv[3])

if  sys.argv[1] and sys.argv[2] in ('EUR','USD','CHF','GBP','RUB','TRY','RON','UAH','MDL'):
        url = ('https://currency-api.appspot.com/api/%s/%s.json') % (a, b)
	print termcolor.colored(Back.BLUE+start+url+end,'green')
	r = requests.get(url)
	print colored("The rate is:",'yellow')
	print colored(r.json()['rate'],'green')
	print colored("Result:",'yellow')
	print colored(c*float(r.json()['rate']),'green')
	urlalt = ('http://themoneyconverter.com/%s/%s.aspx') % (a, b)
	print termcolor.colored(Back.BLUE+start+urlalt+end,'red')
	split1 = ('>%s/%s =') % (b, a)
	strip1 = ('</textarea>')
	ralt = requests.get(urlalt)
	d = float(ralt.text.split(split1)[1].split(strip1)[0].strip())
	print colored("The rate is:",'yellow')
	print colored(d,'red')
	print colored("Result:",'yellow')
	print colored(c*d,'red')
        
elif sys.argv[1] and sys.argv[2] != ('EUR','USD','CHF','GBP','RUB','TRY','RON','UAH','MDL'):
        print termcolor.colored(Back.YELLOW +start+"Please enter the following format: convert.py {source} {target} {value}"+end,'red')
        print termcolor.colored(Back.WHITE +start+"Please enter the currency in the upper case format"+end,'green')
	print termcolor.colored(start+"!!! You can introduce only the following currencies: !!!"+end,'blue')
        print colored("EUR ---- EURO",'blue')
        print colored("USD ---- US Dollar",'blue')
        print colored("CHF ---- Swiss Franc",'blue')
        print colored("GBP ---- British Pound Sterling",'blue')
        print colored("RUB ---- Russian Ruble",'blue')
        print colored("TRY ---- Turkish Lira",'blue')
        print colored("RON ---- Romanian Leu",'blue')
        print colored("UAH ---- Ukraine Hryvnia",'blue')
        print colored("MDL ---- Moldovan Leu",'blue')
	print colored("-------------------------------------------------------------",'green')
	print colored("------------------------ERROR--------------------------------",'green')
	print colored("-------------------------------------------------------------",'green')
