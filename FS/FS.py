#The code is written by Qifeng Zeng
from flask import Flask,abort,Response
import socket
import requests
import json
app = Flask(__name__)
from flask import request

@app.route('/register',methods = ["PUT"],endpoint="register")
def fibonacciserver():
    hostname = request.json.get('hostname')
    ip = request.json.get('ip')
    as_ip = request.json.get('as_ip')
    as_port = request.json.get('as_port')
    dnsmessage = 'TYPE=A\n'+'NAME='+hostname+'\nVALUE='+ip+'\nTTL=10'
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = (as_ip,53533)
    skt.sendto(dnsmessage.encode(),addr)
    rst = None
    while(not rst):
        rst = skt.recvfrom(1024)
    return Response("Registration Finished",status=201)

@app.route('/fibonacci',endpoint="fibonacci")
def fibonacciserver():
    arg = request.args
    if not arg.get('number'):
        abort(400,'Parameter Missing')
    number = arg.get('number')

    for ch in number:
        if ch not in [str(i) for i in range(10)]:
            abort(400, 'Parameter Type Wrong')
    number = int(number)
    def fibonacci_num(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            minus1 = 1
            minus2 = 0
            for i in range(2,x+1):
                new = minus1+minus2
                minus2 = minus1
                minus1 = new
            return minus1
    return str(fibonacci_num(number))

app.run(host='0.0.0.0',
        port=9090,
        debug=True
        )
