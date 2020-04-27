  
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








import os


red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'



url ="https://drv.tw/~"

email = input(("{2}Type Your Email: ").format(orange, green, bold, end, cyan, red))

drive ="gd"

path = input(("{2}Type Your File Path: ").format(orange, green, bold, end, cyan, red))

get = (url + email + "/" + drive + "/" + path)

print('\n')

print(('{5}This is your URL: {4}'+ get).format(orange, green, bold, end, cyan, red))
