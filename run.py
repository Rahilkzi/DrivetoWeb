  
#https://drv.tw/~[username]/[drive]/[path]
#copyright

url ="https://drv.tw/~"

email = input("Type Your Email: ")   

drive ="gd"

path = input("Type Your File Path: ")

get = (url + email + "/" + drive + "/" + path)

print ("♨️this is your URL▶️ " + get)


inp=input("\033[1;33m Do you want to install Tool-X [Y/n]> \033[00m")
if inp=="y" or inp=="Y":
    print("apt install git")
