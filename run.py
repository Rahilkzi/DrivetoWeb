  
#https://drv.tw/~[username]/[drive]/[path]
#copyright



import os


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
 *****    Mob-Droid   *****
 '''.format(orange, green, bold, end, cyan, red)
print(p1) 


p2='''{5}       
{2}Follow me :{3}
{1}•{3} GitHub : {4}https://github.com/rahilkaxi{3}
{1}•{3} YouTube: {4}soon{3}
{1}•{3} Website: {4}soon{3}
'''.format(orange, green, bold, end, cyan, red)

print(p2)







url ="https://drv.tw/~"

email = input("Type Your Email: ")   

drive ="gd"

path = input("Type Your File Path: ")

get = (url + email + "/" + drive + "/" + path)

print ("♨️this is your URL▶️ " + get)

