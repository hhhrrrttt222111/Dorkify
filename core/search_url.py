#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib
from bs4 import BeautifulSoup

import core.colors as colors


def url_search(q):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    # MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
    query = q
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"
    headers = {"user-agent": USER_AGENT}
    res = requests.get(URL, headers=headers)

    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        links = []
        titles = []

        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                links.append(link)
                titles.append(title)

        dorks = dict(zip(links, titles))
        for key, value in dorks.items():
            print(f'[*]  {key}  -  {colors.bcolors.RED}{value}{colors.bcolors.ENDC}')

        if len(dorks) == 0:
            print('Ooops...No results found')

