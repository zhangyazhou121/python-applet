# -*- coding: utf-8 -*-
import urllib2
import urllib
import sys
import re
import json
import os
import time
import sqlite3


reload(sys)
sys.setdefaultencoding('utf-8')
conn = sqlite3.connect('movie.db')
conn.text_factory = lambda x:unicode(x,'utf-8','ignore')
curs = conn.cursor()

curs.execute('''
    create table movie (
        name    blob,
        rating  blob,
        image   blob,
        title   blob,
        summary blob,
        alt blob,
        attrs   blob,
        mobile_link blob,
        id  blob,
        tags    blob
    )
''')
f = open('/tmp/namelist')
namelist = f.readlines()
f.close()
for name in namelist:   
    time.sleep(2)
    url = 'https://movie.douban.com/subject_search?search_text=' + name 
    request = urllib2.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    content = urllib2.urlopen(request).read()
    pattern = re.compile('<div id="collect_form_\d*"></div>')
    items = re.findall(pattern,content)
    if items:
     aa = items[0]
     pattern1 = re.compile('[0-9]+')
     movie_number = re.findall(pattern1,aa)
     url_api = 'https://api.douban.com/v2/movie/' + str(movie_number[0])
     request_api = urllib2.Request(url_api,headers={'User-Agent':'Mozilla/5.0'})
     response_api = urllib2.urlopen(request_api)
     content_api = response_api.read()
     movie_info = json.loads(content_api)
     rating = str(movie_info['rating']['average'])
     image = str(movie_info['image'])
     title = str(movie_info['title'])
     summary = str(movie_info['summary'])
     alt = str(movie_info['alt'])
     attrs = str(movie_info['attrs'])
     mobile_link = str(movie_info['mobile_link'])
     ids = str(movie_info['id'])
     tags = str(movie_info['tags'])
     query = 'insert into movie values (?,?,?,?,?,?,?,?,?,?)'
     curs.execute(query,(name,rating,image,title,summary,alt,attrs,mobile_link,ids,tags,))
     print 'ok'

#     f = open('/home/zhangyazhou/movie_number','w')
#     f.write(movie_number[0])
#     f.close 
                                                                                                                                            

    else:   
     f = open('/home/zhangyazhou/namelist_unopen','w')
     f.write(name)
     f.close
conn.commit()
conn.close()
                                                                                                                                                                            


