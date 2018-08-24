import socket
import threading
import time

tLock = threading.Lock() # stop program to output at the same time
shutdown = False

def receiving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                data = str(data)
                print data
        except:
            pass
        finally:
            tLock.release()

host = "127.0.0.1"
port = 0 #any free port

server = (host, 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Thread(target=receiving, args=("RecvThread", s))
rT.start()

alias = raw_input("Name: ")
msg = raw_input(alias + ">> ")
while msg != "q":
    if msg != "":
        s.sendto(alias + ": " + msg, server)
    tLock.acquire()
    msg = raw_input(alias + ">> ")
    tLock.release()
    time.sleep(0.2)
shutdown = True
rT.join()
s.close()