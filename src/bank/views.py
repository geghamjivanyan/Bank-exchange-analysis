import requests


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Bank

from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
from datetime import date

def welcome(request):
    return render(request, 'welcome.html')



def scrap(request):

    URL = 'https://rate.am/'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="rb")
    bank_list = results.find_all("tr")
 
    for bank in bank_list[2:18]:

        tds = bank.find_all('td')
        b = Bank(name=tds[1].text,
                usd_buy=tds[5].text,
                usd_sell=tds[6].text)
        b.save()


    return HttpResponse('Ok')


def graphic(request):

    banks = Bank.objects.filter(date=date.today())
    
    x = []
    y = []
    for b in banks:
        x.append(b.name)
        y.append(b.usd_sell)

    plt.scatter(x, y)
    plt.savefig('static/bank.svg')

    return render(request, 'graphic.html')
