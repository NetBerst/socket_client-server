from socket import *
import threading
myHost = ''
myPort1 = 10001
myPort2 = 10002
port1 = socket(AF_INET, SOCK_STREAM)
port1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
port2 = socket(AF_INET, SOCK_STREAM)
port2.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

port1.bind((myHost,myPort1))
port2.bind((myHost,myPort2))

port1.listen(1)
port2.listen(1)

def send2port2():
    while True:
        data1 = conection_p1.recv(1024)
        conection_p2.send(b"Echo from port1: " + data1)
    
def send2port1():
    while True:
        data2 = conection_p2.recv(1024)
        conection_p1.send(b"Echo from port2: " + data2)
    
while True:
    
    conection_p1,address_p1 = port1.accept()
    conection_p2,address_p2 = port2.accept()
    
    if conection_p1 and conection_p2 :
        
        threading.Thread(target=send2port2).start()
        threading.Thread(target=send2port1).start()
        
