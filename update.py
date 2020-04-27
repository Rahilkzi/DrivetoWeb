import os
from time import sleep
from sys import exit


red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'


os.system('clear')
p1='''{5}
           ▀▄   ▄▀
          ▄█▀███▀█▄
         █▀███████▀█
         █─█▀▀▀▀▀█─█
            ▀▀─▀▀
 *****    DrivetoWeb   *****
 '''.format(orange, green, bold, end, cyan, red)
print(p1) 


p2='''{5}       
{2}Follow me :{3}
{1}•{3} GitHub : {4}https://github.com/rahilkaxi{3}
{1}•{3} YouTube: {4}soon{3}
{1}•{3} Website: {4}soon{3}
'''.format(orange, green, bold, end, cyan, red)

print(p2)


hello = input("[?] Do you want to update? (y/n): ")
print("================================")
if hello == "y":
    print("========================================================")
    print("[+] Please wait...")
    print("========================================================")
    os.system("pkg install git")
    os.system("cd /data/data/com.termux/files/home && rm -rf DrivetoWeb")
    os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Rahilkaxi/DrivetoWeb.git")
    os.system("clear")
    sys.exit()
    os.system("cd /$HOME")
    # os.system()
    # os.system()
    # os.system()
    
    
