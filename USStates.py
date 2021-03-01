from urllib.request import urlopen
import urllib.request
import csv
from bs4 import BeautifulSoup
from pip._vendor import requests

url = "https://www.50states.com/tools/thelist.htm"
page = requests.get(url)
page.status_code
page.content

states = BeautifulSoup(page.content, "html.parser")
statesA = states.find('table', {'class': "thelist states-table table table-hover"})
statesB = states.find('table', {'class': "thelist table table-hover"})
stateA_rows = statesA.find_all('tr')
capitals = dict()
for tr in stateA_rows:
    td = tr.find_all('td')
    capitals[str(td[1].text).strip()] = str(td[0].text).strip()

stateB_rows = statesB.find_all('tr')
for tr in stateB_rows:
    td = tr.find_all('td')
    capitals[str(td[1].text).strip()] = str(td[0].text).strip()

f = open("usa.states.txt", "r")
list = [i.rstrip() for i in f.readlines()]

result_list = [[i,capitals[i]] for i in list]

with open('usStates+Capitals.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result_list)








