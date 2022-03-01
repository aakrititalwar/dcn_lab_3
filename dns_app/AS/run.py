import requests,socket
import json

port   = 53533

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))

while True:
    print ('Server Running.....')
    msg, clientaddress = s.recvfrom(2048)
    
    msg = msg.decode()
    msg = json.loads(msg)
    #print('Load:',msg)

    if len(msg) == 2:                            
        with open("out.json", "r") as outfile:
            dictionary = json.load(outfile)
        DNS_response = dictionary[msg["NAME"]]
        dns_obj = json.dumps(DNS_response)
        s.sendto(dns_obj.encode(),clientaddress)

    else:
        db = {msg["NAME"]: msg}         
        as_object = json.dumps(db)
        with open("out.json", "w") as outfile:
            outfile.write(as_object)
        s.sendto(str(201).encode(), clientaddress)


       


      