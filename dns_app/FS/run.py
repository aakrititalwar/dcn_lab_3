import requests, json,socket
from flask import Flask,request

app = Flask(__name__)

@app.route('/fibonacci')
def fun_fib():
    numX = int(request.args.get('number'))
    result = fib(numX)
    return str(result)

def fib(n):
   
    if n == 0:
        return 0
 
    elif n == 1 :
        return 1
 
    else:
        return fib(n-1) + fib(n-2)

@app.route('/register', methods = ['GET','PUT'])
def reg_func():
    hostname = request.args.get('hostname') 
    ip = request.args.get('ip')
    as_ip = request.args.get('as_ip')
    as_port =request.args.get('as_port') 
    print(ip , as_ip)
    out_dict = {
        "TYPE": "A",
        "NAME": hostname,
        "VALUE":ip,
        "TTL": 10        
    }
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    fs_obj = json.dumps(out_dict)
    s.sendto(fs_obj.encode(),(as_ip,int(as_port)))
    return_code , clientaddress = s.recvfrom(2048)
    code = return_code.decode('utf-8')       # recvfrom returns result of type byte. Hence decoding required
    if code == '201':
        return str(201),201
    else:
        return ('Error')

app.run(host='0.0.0.0',
        port=9090,
        debug=True)