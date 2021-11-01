# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 13:08:46 2021

@author: Dinde
"""

import market as mkt
import webbrowser
import datetime
import time
import os

plants = []
try:
    for line in open('config.txt','r'):
        if line.startswith('#'):
            pass
        else:
            config = line.replace('\n', '').split(',')
            plants.append({'icon_id':int(config[0]),'le':int(config[1]),'PVU price':float(config[2])})
except:
    print('READ FAIL: The plants are write bad in config.txt')
    exit()
            
time_elapsed = time.time()
captured = False
while not captured:
    results = mkt.get_plants(8)
    os.system('cls')
    print('PVU Bot started')
    print(len(plants), 'plants set, searching results...')
    print(str(datetime.timedelta(seconds=int(time.time() - time_elapsed))))
    print(results)
    v = mkt.verifer(results, plants)
    if v[0]:
        for id in v[1]:
            webbrowser.open('https://marketplace.plantvsundead.com/farm#/plant/' + str(id))
        captured = True
    time.sleep(0.5)



    