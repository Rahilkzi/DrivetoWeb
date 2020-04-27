#importing os module  
import os 
 


 hm = input("[?] Do you want to update? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Please wait...")
            print("========================================================")
            os.system("pkg install git")
            os.system("cd /data/data/com.termux/files/home && rm -rf drivetoWeb")
            os.system("/data/data/com.termux/files/home && https://github.com/Rahilkaxi/DrivetoWeb.git")
            os.system("cd DrivetoWeb")
            os.system("python run.py")
