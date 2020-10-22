#!/usr/bin/env python3

import glob
import requests
import random

def fileListe(strPath='/usr/share/nginx/html/cern/**/*.html'):
    lstFiles = glob.glob(strPath,recursive=True)
    return lstFiles

def callUrl(lstFiles=''):
    user_agent_list = [
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]
    for element in lstFiles:
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}
        url = element.replace('/usr/share/nginx/html','http://192.168.34.32')
        response = requests.get(url,headers=headers)

    for i in range (1,100000):
        url = random.choice(lstFiles)
        headers = {'User-Agent': user_agent}
        url = url.replace('/usr/share/nginx/html','http://192.168.34.32')
        response = requests.get(url,headers=headers)

def main():
    lstFiles = fileListe()
    callUrl(lstFiles=lstFiles)

if __name__ == ('__main__'):
    main()
