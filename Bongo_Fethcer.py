#!/usr/bin/env python3
# coding: utf-8

import urllib.request as req
import urllib.parse as par
from bs4 import BeautifulSoup

def AquireURL():
    Base_URL='https://www.kyoto-np.co.jp/category/bongo'
    Kyoto_Base_URL='https://www.kyoto-np.co.jp'

    with req.urlopen(Base_URL) as r:
        b = r.read()
        data = b.decode('utf-8')

    soup = BeautifulSoup(data, 'lxml')

    Top_Artcle = soup.select_one('#contents > main > div > div:nth-child(3) > article:nth-child(1) > a')

    return Kyoto_Base_URL + Top_Artcle.attrs['href']

if __name__ == "__main__":

    with req.urlopen(AquireURL()) as r:
        b = r.read()
        data = b.decode('utf-8')

    soup = BeautifulSoup(data, 'lxml')

    Title = soup.find('h1').string.replace('コラム凡語：','')
    Article = soup.find('p').string

    print("Title:", Title)
    print("Artcle:" + Article.replace('▼', '\n▼'))

