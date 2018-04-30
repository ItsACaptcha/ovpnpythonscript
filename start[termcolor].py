
#simple python script by ItsACaptcha ; Yes i know its shit
#place this script in the same directory as your config files
import os
import sys
import subprocess
import random
import time
from termcolor import cprint
files =[]
cprint ('getting current script name...','red')
file_name =  os.path.basename(sys.argv[0])
cprint ('scriptname = '+file_name, 'green')
cprint ('getting current dir...', 'red')
current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
cprint ('dir = '+current_dir,'green')
cprint ('getting all files...','red')
files = os.listdir(current_dir)
cprint ('ok','green')
#files.remove('vpn.crt')  
files.remove(file_name)
#files.remove('auth.txt')  if you have an auth file uncomment this and rename auth.txt to the authfile
cprint ('available config pool:','red')
print('')
print (files)
randomNumber = random.randint(0, len(files))		
cprint ('pseudo-random number: '+ str(randomNumber),'red')
cprint ('starting openvpn with configuration: '+ files[randomNumber],'red')
print ('')
print ('')
cprint ('STARTING VPN IN:','green')
for i in xrange(6):   #wait for 6 seconds before starting opvpn
	cprint(5-i,'red')
	time.sleep(1)
openvpn_cmd = ['sudo', 'openvpn', '--config', files[randomNumber]]   # add ,'--auth-user-pass', yourauthfile if  it wont be used automatically
prog = subprocess.Popen(openvpn_cmd)
