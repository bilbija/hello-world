import socket

def Main():
    host = "127.0.0.1" # this PC
    port = 5000
    
    s = socket.socket() # new socket object
    s.bind((host, port))
    
    s.listen(1) # listen for only one connection
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + data
        c.send(data)
        
    c.close()
    
if __name__ == "__main__":
    Main()