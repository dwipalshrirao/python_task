
import os
hostname = "www.kite.com"
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')
cmd = 'code .'
  
# Using os.system() method 
os.system(cmd) 