#!/usr/bin/python2.7
#!-*- coding:utf8 -*-


import requests
import time
import json
import os
import socket

def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

if __name__ == '__main__':
    cmd = "/usr/local/bin/netlook -c|head -n 1|awk -F '%' '{print $1}'"
    result = execCmd(cmd)
    a = float(result)
    print a
    hostname = socket.gethostname()
    print hostname
    ts = int(time.time())
    payload = [
        {
            "endpoint": hostname,
            "metric": "usage",
            "timestamp": ts,
            "step": 60,
            "value": a,
            "counterType": "GAUGE",
            "tags": "service=ali,id=beijing",
        },

    ]

    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))

    print r.text

