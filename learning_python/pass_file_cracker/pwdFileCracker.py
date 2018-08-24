import sys
import os.path
import zipfile
import time
from itertools import product


def the_end(exit_val):
    print ""
    print "The End"
    exit(exit_val)
# end the_end

def open_dict_file():
    file_name = ""
    while 1:
        file_name = raw_input("Enter dictionary file name: ")
        if file_name == "q":
            the_end(1)
        if os.path.isfile(file_name):
            break
    file_hdl = open(file_name, "rb")
    return file_hdl
# end open_dict_file

def open_zip_file():
    zip_name = ""
    while 1:
        zip_name = raw_input("Enter zip file name: ")
        if zip_name == "q":
            the_end(1)
        if os.path.isfile(zip_name):
            break
    zip_hdl = zipfile.ZipFile(zip_name)
    return zip_hdl
# end open_zip_file

def brute_force_attack(zip_file):
    for r in (1,2,3,4,5,6):
        for item in product("abcdefghijklmnopqrstuvwxyz", repeat=r):
            password = "".join(item)
            try:
                zip_file.extractall(pwd=password.encode())
                print password
                return True
            except:
                continue
    return False
# end brute_force_attack

def dictionary_attack(zip_file, dict_file):
    while 1:
        password = dict_file.readline()
        password = password.rstrip()
        if not password:
            break
        try:
            zip_file.extractall( pwd=password.encode() )
            print "YUPIIII, pasword is =", password
            return True
        except:
            continue
    return False
# end dictionary_attack

def dictionary_cracking():
    print ""
    print "Dictionary Cracking"
    zip_pointer = open_zip_file()
    dict_pointer = open_dict_file()
    start = time.time()
    ret = dictionary_attack(zip_pointer, dict_pointer)
    time_v = time.time() - start
    print time_v
    zip_pointer.close()
    dict_pointer.close()
    return ret
# end dictionary_cracking

def brute_force_cracking():
    print ""
    print "Brute Force Cracking"
    zip_pointer = open_zip_file()
    start = time.time()
    ret = brute_force_attack(zip_pointer)
    time_v = time.time() - start
    print time_v
    zip_pointer.close()
    return ret
# end brute_force_cracking

def main_app():
    while 1:
        resp = raw_input("What type of cracking ( 1 = brute force, 2 = dictionary, 3 = both, q = quit ): ")
        if resp == "q":
            break
        elif resp == "1":
            brute_force_cracking()
            break
        elif resp == "2":
            if dictionary_cracking():
                print "Cracking Ok"
            else:
                print "Cracking Failed"
            break
        elif resp == "3":
            if not dictionary_cracking():
                brute_force_cracking()
            break
    the_end(0)
# end main_app

def test_zip():
    zhdl = zipfile.ZipFile("text1.zip")
    try:
        zhdl.extractall( pwd="pwd333" )
        print "pwd333"
    except:
        print "no"
    zhdl.close()
# end test_zip

def test_iter():
    f = open("d2.txt", "wb")
    for r in ( 6, ):
        print ""
        print "All passwords with %d char:" %r
        start = time.time()
        for item in product("abcdefghijklmnopqrstuvwxyz", repeat=r):
            password = "".join(item)
            f.write(password+"\n")
        print "Time = %.4f" %(time.time()-start)
    f.close()

if __name__ == "__main__" :
    # main_app()
    # test_zip()
    print "start"
    test_iter()
    print "stop"