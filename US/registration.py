#The code is written by Qifeng Zeng

import requests
import json
#192.168.1.206
#172.17.0.1

def http_put():
    url = 'http://192.168.1.206:9090/register' #This is the url for registration
    values = {'hostname': 'fibonacci.com',
              'ip': '192.168.1.206',          #replace it with the ip of the hostname
              'as_ip': '172.18.0.1',          #replace it with the ip of the authorized server
              'as_port': '30001'}             #replace it with the port of the authorized server
    headers = {"Content-Type": "application/json"}
    values = json.dumps(values)
    r = requests.put(url,data = values,headers= headers)
    return  # 获取服务器返回的页面信息

http_put()    #run this program to regist on the authorized server
