#!/usr/bin/env python
# Copyright 2018 ...
#
#++
# Name
#    fileServer.py
#
# Purpose
#    Simple script on the server side for FilelServer
#
# References
#   https://www.youtube.com/watch?v=LJTaPaFGmM4
#
# Revision Dates
#    22-Aug-2018 (ABI) Creation
#--
#

#- imports
import socket
import threading
import os

os.chdir("server_files")

def retFile(conn):
    fname = conn.recv(1024)
    if os.path.isfile(fname):
        fsize = os.path.getsize(fname)
        conn.send(str(fsize))
        with open(fname, "rb") as f:
            while True:
                dataToSend = f.read(1024)
                if dataToSend == "":
                    break
                conn.send(dataToSend)
    else:
        conn.send("ERROR")
#- end retFile

def listAllFiles(conn):
    allFilesList = [f for f in os.listdir(os.getcwd()) if os.path.isfile(f)]
    conn.send(str(allFilesList))
#- end listAllFiles

def serverApp(conn):
    while True:
        clientReq = conn.recv(1024)
        if "list_all_files" == clientReq:
            listAllFiles(conn)
        elif "get_file" == clientReq:
            retFile(conn)
        elif "disconnect" == clientReq:
            break
#- end serverApp

def main():
    # host = "127.0.0.1"   # IP addr of localhost
    host = "10.21.10.1"   # IP addr of localhost
    port = 5000          # randomly selected port
    
    s = socket.socket()  # created default TCP socket
    s.bind((host, port)) # bind socket to address
    print "Server Started."
    
    s.listen(5)          # listen for connection, max num of connections = 5
    
    while True:
        conn, addr = s.accept() # accept a connection
        print "Client connected from address: " + str(addr)
        
        t = threading.Thread( target=serverApp, args=(conn,) ) # start thread
        t.start()
    
    s.close()
    print "Server Closed."
#- end main

if __name__ == "__main__":
    main()
    print ""
    print "This is The END :( !"
#- end __main__