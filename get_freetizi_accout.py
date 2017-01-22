# -*- coding: utf-8 -*-
import urllib2
import urllib
import os
import re

url = 'http://freetizi.xyz'
request = urllib2.Request(url,headers={'User-Agent':'Mozilla/5.0'})
content = urllib2.urlopen(request).read()
pattern = re.compile('<p>.*<code>.*</code></p>')
accout = re.findall(pattern,content)

server = accout[0].replace('<p>','').replace('</p>','').replace('<code>','').replace('</code>','').split('：')[1]
server_port = accout[1].replace('<p>','').replace('</p>','').replace('<code>','').replace('</code>','').split('：')[1]
password = accout[2].replace('<p>','').replace('</p>','').replace('<code>','').replace('</code>','').split('：')[1]
local_port = '1080'
#print server
#print server_port
#print password
#print local_port
if server == '****' :
	print 'The server is busy now! Please wait another minutes.'
elif server != '****' :
	f = open('/home/zyz/shadowsocks/freetizi.json','w')
	f.write('{')
	f.write("\n")
	f.write('\"server\"' + ':' + '\"' + server + '\"' + ',')
	f.write("\n")
	f.write('\"server_port\"' + ':' + server_port + ',')
	f.write("\n")
	f.write('\"password\"' + ':' + '\"' + password + '\"' + ',')
	f.write("\n")
	f.write('"local_port"' + ':' + local_port + ',')
	f.write("\n")
	f.write('"timeout"' + ':' + '600' + ',')
	f.write("\n")
	f.write('"method"' + ':' + '"aes-256-cfb"')
	f.write("\n")	
	f.write('}')
	f.close()
	os.system('sudo /usr/local/bin/sslocal -c /home/zyz/shadowsocks/freetizi.json -d restart')
	print 'Congratulations! You can surf the Internet now!'



