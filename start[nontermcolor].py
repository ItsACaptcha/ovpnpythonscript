
#simple python script by ItsACaptcha ; Yes i know its shit
#place this script in the same directory as your config files
import os
import sys
import subprocess
import random
import time
from termcolor import print
files =[]
print ('getting current script name...')
file_name =  os.path.basename(sys.argv[0])
print ('scriptname = '+file_name)
print ('getting current dir...')
current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
print ('dir = '+current_dir)
print ('getting all files...')
files = os.listdir(current_dir)
print ('ok')
#files.remove('vpn.crt')   uncomment this if your certificate is stored locally
files.remove(file_name)
#files.remove('auth.txt')  if you have an auth file uncomment this and rename auth.txt to the authfile
print ('available config pool:')
print('')
print (files)
randomNumber = random.randint(0, len(files)
print ('pseudo-random number: '+ str(randomNumber))
print ('starting openvpn with configuration: '+ files[randomNumber])
print ('')
print ('')
print ('STARTING VPN IN:')
for i in xrange(6):   #wait for 6 seconds before starting opvpn
	print(5-i)
	time.sleep(1)
openvpn_cmd = ['sudo', 'openvpn', '--config', files[randomNumber]] # add ,'--auth-user-pass', yourauthfile  if it wont be used automatically 
prog = subprocess.Popen(openvpn_cmd)
