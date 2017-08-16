# -*- coding: utf-8 -*-
import os
import urllib.request


directory = '.\\download4\\'

try:
    os.stat(directory)
except:
    os.mkdir(directory)   



for i in range(1, 91+1):
    print(i)
    
    req = urllib.request.Request('http://www.insecam.org/cam/bycountry/KR/?page='+str(i), headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    #webpage = webpage.decode('utf8')
    print(webpage)
    f = open(directory+'page'+str(i)+'.html', 'wb')
    f.write(webpage)
    f.close()
    
