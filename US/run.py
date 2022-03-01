import requests, json,socket
from flask import Flask,request,abort

app = Flask(__name__)

@app.route('/fibonacci')
def US_func():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    num = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    #print(hostname,fs_port,num,as_ip,as_port)

    if hostname is None or fs_port is None or as_ip is None or as_port is None or num is None:
        abort(400)
   
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    US_dict= {
        'NAME': hostname,
        'TYPE': "A"
    }
    us_obj = json.dumps(US_dict)
    s.sendto(us_obj.encode(), (as_ip,int(as_port)))
    #print('Response Sent')
    response, clientaddress = s.recvfrom(2048)
    #print('Response received:',response)
    received_data = response.decode()
    received_data = json.loads(received_data)
   # print('Query response is: ',received_data)
    path = "http://" + received_data["VALUE"] + ":" + fs_port + "/fibonacci?" + "number=" + num
    answer=requests.get(path)
    txt = answer.text
    return txt

app.run(host='0.0.0.0',
        port=8080,
        debug=True)