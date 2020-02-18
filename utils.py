#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:27:31 2020

@author: lucasabdalah
"""

import urllib.request as req
from bs4 import BeautifulSoup as bs
import csv

def getPiciBenfica():
    horario = 15 #primeiro
    horario -= 1
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRzFS-ijp1-zPq7rwgiwELaSCHvVRURNYkwiIcErIjeFxrI-jLmFomXpByc1LJ5As0afwiVDG6cHpER/pubhtml"
    site = req.urlopen(url).read()
    html = bs(site,"html.parser")
    valor = html.find_all("td",{"class":"s25"})[horario]
    valor = (str(valor))
    valor = valor[1:-2] # Exclude the markers of html < >
    start = valor.find('>') + 1
    end = valor.find('<', start)

    return valor[start:end]

# Retorna a tabela de Horarios de acordo com um arquivo.csv
def getTimeTable(name):
    with open(name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        a = []
        for row in spamreader:
            a.append((' '.join(row)) )

    N = len(a)
    txt = ''
    for line in range(0,N):
        pos = str(a[line]).find(',')
        if pos != -1:
            txt += str(a[line][0:pos]) + '\t|\t' + str(a[line][pos+1:len(a[line])+1]) + '\n'
        else:
            txt += str(a[line]) + '\n'
    return(txt)
