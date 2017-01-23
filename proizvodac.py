import os
import time
import sys
import sysv_ipc
from colorama import Fore

brojArgumenata = len(sys.argv)

try:
    MSG_KEY = int(os.environ["MSG_KEY"])
except:
    print("Nije moguce dohvatiti MSG_KEY!")
    exit()

if brojArgumenata != 3:
    print("Nevaljan broj argumenata!")
    exit()

redPoruka = sysv_ipc.MessageQueue(MSG_KEY)

for i in range(0, len(sys.argv[1])):
    redPoruka.send(sys.argv[1][i] + ";" + sys.argv[2])
    print (Fore.BLUE + "Proizvodac [" + sys.argv[2] +  "] poslao: " + sys.argv[1][i])
    time.sleep(1)

redPoruka.send("" + ";" +  sys.argv[2])
print (Fore.BLUE + "Proizvodac [" + sys.argv[2] +  "] zavrsio!")