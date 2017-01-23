import time
import os
import sysv_ipc
import threading
from colorama import Fore, Back


def provjeriVrijemeZadnjePoruke(redPoruka):
    while True:
        razmakIzmeduPoruka = (int(time.time()) - redPoruka.last_receive_time)
        if razmakIzmeduPoruka >= 2 and razmakIzmeduPoruka < 6 and redPoruka.last_receive_time != 0:
            print(Fore.RED + "Potrosac se gasi za (" + str(6 - razmakIzmeduPoruka) +  ")")
        elif razmakIzmeduPoruka >= 6 and redPoruka.last_receive_time != 0:
            print(Fore.RED + "Potrosac zavrsio!")
            redPoruka.remove()
            break
        time.sleep(1)
    return

try:
    MSG_KEY = int(os.environ["MSG_KEY"])
except:
    print("Nije moguce dohvatiti MSG_KEY!")
    exit()

spremnikPoruka = {}

redPoruka = sysv_ipc.MessageQueue(MSG_KEY)

dretva = threading.Thread(target=provjeriVrijemeZadnjePoruke, args=(redPoruka,))
dretva.daemon = True
dretva.start()

while True:
    try:
        s, _ = redPoruka.receive()
    except:
        break

    primljeno = s.rsplit(";")

    print (Fore.RED + "Potrosac od [" + primljeno[1] +  "] primio: " + primljeno[0])
    if primljeno[0] == "":
        print(Fore.RED + "Konacna poruka od [" + primljeno[1] + "]: " + spremnikPoruka[primljeno[1]])
    else:
        if primljeno[1] in spremnikPoruka.keys():
            spremnikPoruka[primljeno[1]] = spremnikPoruka[primljeno[1]] +  primljeno[0]
        else:
            spremnikPoruka[primljeno[1]] = primljeno[0]

    time.sleep(1)

dretva.join()
os._exit
