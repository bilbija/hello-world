import socket

def Main():
    host = "127.0.0.1"
    port = 5000
    
    s = socket.socket()
    s.connect((host, port))
    
    msg = raw_input(">> ")
    while msg != "q":
        s.send(msg)
        data = s.recv(1024)
        print "Received from server: " + str(data)
        msg = raw_input(">> ")
        
    s.close()
    
if __name__ == "__main__":
    Main()