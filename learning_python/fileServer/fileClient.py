#!/usr/bin/env python
# Copyright 2018 ...
#
#++
# Name
#    fileClient.py
#
# Purpose
#    Simple script on the client side for FilelServer
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
import time
import sys
import os

os.chdir("client_files")

#- globals
# HOST = "127.0.0.1"
HOST = "10.21.10.20"
PORT = 5000
COUNT = 10 # number of retries trying to connect

def connectToServer():
    s = socket.socket()
    count = COUNT
    while count:
        try:
            m = s.connect((HOST, PORT))
            print m
            return s
        except socket.error as err:
            count -= 1
            print "Error:", err
            time.sleep(3)
    print "Error while connecting to server!"
    exit(1)
#- end connectToServer

def mainApp():
    all_files = {}
    conn = connectToServer()
    
    while True:
        options = {1:"Quit", 2:"List file from server", 3:"Download file from server"}
        print ""
        print "Options:", options
        cmd = None
        while True:
            userCmd = int(raw_input("Select from options >> "))
            if userCmd in list(options.keys()):
                cmd = userCmd
                break
        print ""
        if cmd == 1:
            conn.send("disconnect")
            print "End of mainApp"
            break
        elif cmd == 2:
            conn.send("list_all_files")
            all_files_str = conn.recv(1024)
            print all_files_str
            all_files_str = all_files_str[1:-1].split(" ")
            for i, file in enumerate(all_files_str):
                if file[-1] == ",":
                    file = file[1:-2]
                else:
                    file = file[1:-1]
                print i, file
                all_files[i] = file
        elif cmd == 3:
            conn.send("list_all_files")
            all_files_str = conn.recv(1024)
            all_files_str = all_files_str[1:-1].split(" ")
            for i, file in enumerate(all_files_str):
                if file[-1] == ",":
                    file = file[1:-2]
                else:
                    file = file[1:-1]
                print i, file
                all_files[i] = file
            fileIdx = None
            while True:
                userCmd = int(raw_input("Which file you want to download (enter appropriate number) >> "))
                if userCmd in all_files.keys():
                    fileIdx = userCmd
                    break
                else:
                    print "wrong index, try again!"
            fname = all_files[fileIdx]
            conn.send("get_file")
            time.sleep(0.5)
            conn.send(fname)
            recData = conn.recv(1024)
            fsize = 0
            if "ERROR" in recData:
                print "File '"+fname+"' does not exist on server!"
                continue # next while loop
            else:
                fsize = long(recData)
            f = open("new_"+fname, "wb")
            received = 0
            print "Downloading..."
            while received < fsize:
                recFile = conn.recv(1024)
                f.write(recFile)
                received += len(recFile)
            print "Download Completed!"
    conn.close()
            
#- end mainApp

if __name__ == "__main__":
    try:
        mainApp()
    except KeyboardInterrupt:
        print "Ctrl+C"
    print ""
    print "This is The END :( !"
#- end __main__