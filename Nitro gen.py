import random
from colorama import Fore
import time

digits = "16"
service = "Nitro"

print (Fore.RED + """ _______        _        ____                              ___               __  
 |__   __|      | |      / __ \                            / (_)              \ \ 
    | | ___  ___| |__   | |  | |_      ___ __   ___ _ __  | | _  ___  _   _ ___| |
    | |/ _ \/ __| '_ \  | |  | \ \ /\ / / '_ \ / _ \ '__| | || |/ __|| | | / __| |
    | |  __/ (__| | | | | |__| |\ V  V /| | | |  __/ |    | || | (__ | |_| \__ \ |
    |_|\___|\___|_| |_|  \____/  \_/\_/ |_| |_|\___|_|    | ||_|\___(_)__, |___/ |
                                                           \_\         __/ |  /_/ 
                                                                      |___/       """)

chars = "ABCDEFJHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
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
print(rndc1 + """―――――――――――――――――――――――――――――――――――――――
[INFO] Discord Code Generator
[INFO] Discord Codes will be here.
[INFO] MOST CODES DO NOT WORK!
[INFO] CODES ARE TO BE CHECKED
―――――――――――――――――――――――――――――――――――――――""")
omak = input(red + "Select How Many Codes You Want To Generate:" + "\n")
timee = input(blue + "What's The Sleep Time Between Each Code:" + "\n")
for i in range(int(omak)):
    fs1 = ''.join(random.choice(chars) for i in range(int(digits)))
    all = f"http://discord.gift/{fs1}"
    time.sleep(int(timee))
    print (rndc1 + f"Your {service} Code :" + r + rndc8 + all)
    output = open(f"{service}.txt", "a")
    output.write(all + "\n")



