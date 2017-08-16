# -*- coding: utf-8 -*-

import os
import glob
import re

              
html_list = glob.glob(r'.\download4\*.html')
p_img = re.compile('<img id="[\w\s]+" class="thumbnail-item__img img-responsive" src="([^"]+)"[\s]*title="([^"]+)"')
p_ip = re.compile('[\d]+\.[\d]+\.[\d]+\.[\d]+')

i=1

f_output = open('output4.csv', 'w')
f_output.write('Index,IP,Web Address,Comment\n')

for html in html_list:
    f = open(html, 'rb')
    webpage = f.read().decode('utf-8')
    #print(webpage)
    m = p_img.findall(webpage)
    for item in m:
        web_address = item[0]
        comment = item[1]
        ip_address = p_ip.search(web_address)[0]
        print(str(i) + ',' + ip_address + ',' + web_address + ',' + comment)
        f_output.write(str(i) + ',"' + ip_address + '","' + web_address + '","' + comment + '"\n')
        i += 1
    f.close()

f_output.close()