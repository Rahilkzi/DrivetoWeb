#importing os module  
import os 
 

hello = input("[?] Do you want to update? (y/n): ")
print("================================")
if hello == "y":
    print("========================================================")
    print("[+] Please wait...")
    print("========================================================")
    os.system("pkg install git")
    os.system("cd /data/data/com.termux/files/home")
    os.system("rm -rf DrivetoWeb")
    os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Rahilkaxi/DrivetoWeb.git")
    os.system("cd DrivetoWeb")
    os.system("python run.py")
