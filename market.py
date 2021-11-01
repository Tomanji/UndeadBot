# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 13:06:17 2021

@author: Dinde
"""

import datetime
import requests
import json 
import pandas as pd
import time
import webbrowser

bearer_token = None
try:
    bearer = open("token.txt", 'r')
    for line in bearer:
        if line.startswith('#'):
            pass
        else:
            bearer_token = line.replace('\n', '')
except:
    print('READ FAIL: The plants are write bad in bearer_token.txt')
    exit()

pd.options.display.float_format = '{:.2f}'.format

def get_plants(limit, type=1, save=False):
    headers = {'authorization':'Bearer Token: '+bearer_token,'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38'}
    marketplace = requests.get("https://backend-farm.plantvsundead.com/get-plants-filter-v2?sort=latest&offset=0&limit="+str(limit)+"&type="+str(type), headers=headers)
    marketplace2 = json.loads(marketplace.text)
    
    # full_market = np.array([])
    market_final = pd.DataFrame(columns = ['id','icon_id','le','PVU price'])
    
    for plant in marketplace2['data']:
        row = {}
        row['id']             = plant['id']
        row['icon_id']        = plant['iconUrl'].split('/')[-1].split('_')[0]
        row['le']             = plant['config']['farm']['le']
        row['PVU price']      = plant['startingPrice']
        market_final = market_final.append(row, ignore_index=True)
    # market_final.to_html('C:/Users/Dinde/PVU_Market/MarketHistory/templates/market.html', index= False)
    if save:
        market_final.to_csv('market.csv', index=False)
    return market_final

def verifer(results, plants):
    found = []
    for plant in plants:
        res = results
        filters = [results['icon_id'] == plant['icon_id'], results['le'] >= plant['le'], results['PVU price'] <= plant['PVU price'] ]
        for f in filters:
            res = res.loc[f].reset_index(drop=True)
        if len(res) != 0:
            for id in res['id']:
                found.append(id)
    if len(found) != 0:
        return True, found
    else:
        return False, found

