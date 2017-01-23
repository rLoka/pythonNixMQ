import os
import sys
import sysv_ipc
import subprocess
from colorama import Back

brojArgumenata = len(sys.argv)

if brojArgumenata <= 2:
    print("Nedovoljan broj argumenata!")
    exit()

os.environ["MSG_KEY"] = "1337"
MSG_KEY = int(os.environ["MSG_KEY"])

#temp = sysv_ipc.MessageQueue(MSG_KEY)
#temp.remove()

redPoruka = sysv_ipc.MessageQueue(MSG_KEY, sysv_ipc.IPC_CREX)

for i  in range(1, brojArgumenata, 2):
    subprocess.Popen(["python", "proizvodac.py", sys.argv[i], sys.argv[i+1]])

subprocess.Popen(["python", "potrosac.py"])
