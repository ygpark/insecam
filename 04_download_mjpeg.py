# -*- coding: utf-8 -*-
import os
import datetime
import http
import requests
from urllib.request import Request, urlopen

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')

filename = '.\\output3.csv'
directory = '.\\img3\\'

# make DIRECTORY

try:
    os.stat(directory)
except:
    os.mkdir(directory)   


'''
remaining_download_tries = 15

while remaining_download_tries > 0 :
    try:
        req = Request("http://175.205.135.116:60001/cgi-bin/snapshot.cgi?chn=0&amp;u=admin&amp;p=&amp;q=0", headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/4261C3"})
        res = urlopen(req)
        time.sleep(0.1)
        
    except:
        print("error downloading on trial no: " + str(16 - remaining_download_tries))
        remaining_download_tries = remaining_download_tries - 1
        continue
    else:
        break


exit
'''
f = open(filename, 'r')
lines = f.readlines()

rownum = 1
for line in lines[rownum:] :
    rownum += 1
    listdata = line.split(',')
    webaddress = listdata[2].replace('"', '')
    ip = listdata[1].replace('"', '')
    
    
    
    data = b''
    
    try:
        
            
        if "http://175.205.135.116:60001/cgi-bin/snapshot.cgi?chn=0&amp;u=admin&amp;p=&amp;q=0" not in webaddress:
            continue
    
        print('[' + str(rownum) + ']' + webaddress )    
        
        req = Request(webaddress, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/4261C3"})
        res = urlopen(req)
        
        data += res.read(2)
        
        if b'\xff\xd8' in data:
            print("jpg")
            data += res.read()
        else:
            print("mjpg")
            while b'\xff\xd9' not in data:
                data += res.read(1)
    
        f_img = open(directory + ip + '__' + timestamp + '.jpg', 'wb')
        f_img.write(data)
        f_img.close()    


    except http.client.RemoteDisconnected as e:
        print(e)
