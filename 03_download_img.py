# -*- coding: utf-8 -*-
import os
import datetime
from urllib.request import Request, urlopen

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')

filename = '.\\output4.csv'
directory = '.\\img4\\'

try:
    os.stat(directory)
except:
    os.mkdir(directory)   

f = open(filename, 'r')
lines = f.readlines()



rownum = 1
for line in lines[rownum:] :
    rownum += 1
    listdata = line.split(',')
    webaddress = listdata[2]
    ip = listdata[1]
    
    print('[' + str(rownum) + ']' + webaddress.replace("\"", ""))
    
    data = b''
    
    try:
        
        req = Request(webaddress, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/4261C3"})
        res = urlopen(req, timeout=300)
        
        data += res.read(2)
        if b'\xff\xd8' in data:
            print("jpg")
            data += res.read()
        else:
            print("mjpg")
            while b'\xff\xd9' not in data:
                data += res.read(1)
    
        #print(data)
        #print(directory + str(rownum) + timestamp + '.jpg')
        f_img = open(directory + ip + '__' + timestamp + '.jpg', 'wb')
        f_img.write(data)
        f_img.close()


    except:
        
        print('error')    
