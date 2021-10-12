#The code is written by Qifeng Zeng

from flask import Flask,abort
app = Flask(__name__)
from flask import request
import socket
import requests


@app.route('/')

def hello_world():
    return 'Welcome'

@app.route('/fibonacci')
def userserver():
    arg = request.args
    if not arg.get('hostname') or not arg.get('fs_port') or not arg.get('number') or not arg.get('as_ip') or not arg.get('as_port'):
        abort(400)
    else:
        hostname = arg.get('hostname')
        as_ip = arg.get('as_ip')
        x = arg.get('number')
        dnsmessage = 'TYPE=A\n'+'NAME='+hostname
        skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (as_ip, 53533)
        skt.sendto(dnsmessage.encode(), addr)
        rst = None
        while (not rst):
            rst,addr = skt.recvfrom(1024)
        rst = rst.decode()
        rst = rst.split('\n')
        for line in rst:
            name, value = line.split('=')
            if name == 'VALUE':
                ipfs = value
        url = 'http://'+ipfs+':9090/fibonacci?number='+x
        r = requests.get(url)
        return r.text


app.run(host='0.0.0.0',
        port=8080,
        debug=True
        )

