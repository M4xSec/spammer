import pyautogui
from time import sleep
import random
import sys
import os
from platform import system

def banner():
    print('''\033[31m
    ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
  ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
  ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
    ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
  ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
  ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
  ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
        ░                 ░  ░       ░          ░      ░  ░   ░     
                                                                   \033[00m 

\033[00m           \033[01m\033[33m         >>> cOdEd By: Predator0x300 <<<\033[00m\033[00m\n
\033[01m\033[33m         >>>--- GitHub:\033[31m  https://github.com/Predator0x300 \033[00m\033[33m ---<<<\033[00m\033[00m\n''')

def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass

os.system("clear")
class Spammer_auto():
    def __init__(self, file_name):
        clear()
        banner()
        print("\n\t\033[01m\033[31m{+} Spamming Started!....... ;))\n\033[00m\033[00m")
        sleep(5)
        self.txt_file = open(file_name, 'r').read()
        self.split_file = self.txt_file.splitlines()
        for max in range(80):
            pyautogui.typewrite(random.choice(self.split_file))
            pyautogui.press("enter")
            sleep(0.5)

class Spammer_manual():
    def __init__(self, file_name, speed):
        print("{~} Enter the Spam_count: ")
        count = int(input(">>> "))
        clear()
        banner()
        print("\n\t{+} Spamming Started!....... ;))\n")
        sleep(6)
        self.txt_file = open(file_name, 'r').read()
        self.split_file = self.txt_file.splitlines()
        for max in range(count):
            pyautogui.typewrite(random.choice(self.split_file))
            pyautogui.press("enter")
            sleep(speed)

clear()
banner()
def usage():
    print("{+} Usage:\n")
    print("\tAuto: python3 spammer.py -a -f file_name")
    print("\tManual: python3 spammer.py -m -f file_name -i fast\n")
    print("{+} Help:\n\t{!} -a : auto | -m : manual\n\t{~} -c : count_spam (default: 80)")
    print("\t{~} -i : interval/slow:1/med:0.05/fast:0.0005 (default: med)\n")

if (len(sys.argv) == 4):
    if(sys.argv[1]== "-a" and sys.argv[2] == "-f"):
        Spammer_auto(sys.argv[3])
    else:
        usage()

elif (len(sys.argv) == 6):
    if(sys.argv[1]== "-m" and sys.argv[2] == "-f" and sys.argv[4]=="-i"):
        if(sys.argv[5] == "fast"):
            speed = 0.0005
            Spammer_manual(sys.argv[3],speed)

        elif(sys.argv[5] == "med"):
            speed = 0.05
            Spammer_manual(sys.argv[3],speed)
        elif(sys.argv[5] == "slow"):
            speed = 1
            Spammer_manual(sys.argv[3], speed)
        else:
            usage()
    else:
        usage()
else:
    usage()