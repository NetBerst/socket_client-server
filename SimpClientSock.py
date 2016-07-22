from socket import *
import threading

myHost = ''
myPort = 1233
portServ =1234 

sockListen = socket(AF_INET,SOCK_STREAM)
sockListen.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sockListen.bind((myHost,myPort))
sockListen.listen(1)

sockClient = socket(AF_INET,SOCK_STREAM)
sockClient.connect(('127.0.0.1',1234))
                   
                   
while True:
    
    conectionTelnet, address = sockListen.accept() 
    
    while True:
        data = conectionTelnet.recv(1024)         
        
        sockClient.send(b"Data from client to server "+data)
        
        dataFromServer = sockClient.recv(1024)
        
        conectionTelnet.send(b"Data from client and server " + dataFromServer)
