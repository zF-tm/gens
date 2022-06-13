from ast import For
import random
from colorama import Fore
import time
print (Fore.RED + """ _______        _        ____                              ___               __  
 |__   __|      | |      / __ \                            / (_)              \ \ 
    | | ___  ___| |__   | |  | |_      ___ __   ___ _ __  | | _  ___  _   _ ___| |
    | |/ _ \/ __| '_ \  | |  | \ \ /\ / / '_ \ / _ \ '__| | || |/ __|| | | / __| |
    | |  __/ (__| | | | | |__| |\ V  V /| | | |  __/ |    | || | (__ | |_| \__ \ |
    |_|\___|\___|_| |_|  \____/  \_/\_/ |_| |_|\___|_|    | ||_|\___(_)__, |___/ |
                                                           \_\         __/ |  /_/ 
                                                                      |___/       """)

chars = "ABCDEFJHIJKLMNOPQRSTUVWXYZ1234567890"

service = "xbox"
digit = "5"

time.sleep(1)
blue = Fore.BLUE
red = Fore.RED
pink = Fore.MAGENTA
lightwhite = Fore.LIGHTWHITE_EX
all = [blue , red , pink , Fore.GREEN , Fore.CYAN , Fore.LIGHTGREEN_EX , Fore.YELLOW]
rndc1 = random.choice(all)
rndc2 = random.choice(all)
rndc3 = random.choice(all)
rndc4 = random.choice(all)
rndc5 = random.choice(all)
rndc6 = random.choice(all)
rndc7 = random.choice(all)
rndc8 = random.choice(all)
r = Fore.RESET
print(rndc1 + "Welcome " + r + rndc2 + "To " + r + rndc3 + "The " + r + rndc4 + f"{service} " + r + rndc5 + "Code " + r + rndc6 + "Gen ")
omak = input("Select How Many Codes You Want To Generate:" + "\n")
for i in range(int(omak)):
    fs1 = ''.join(random.choice(chars) for i in range (int(digit)))
    fs2 = ''.join(random.choice(chars) for i in range (int(digit)))
    fs3 = ''.join(random.choice(chars) for i in range (int(digit)))
    fs4 = ''.join(random.choice(chars) for i in range (int(digit)))
    fs5 = ''.join(random.choice(chars) for i in range (int(digit)))
    all = fs1 + "-" + fs2 + "-" + fs3 + "-" + fs4 + "-" + fs5
    time.sleep(0.15)
    print (rndc1 + f"Your {service} Code :" + r + rndc8 + all)
    output = open(f"{service}.txt", "a")
    output.write(all + "\n")