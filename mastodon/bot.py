#/*
# * ------------------------------------------------------------
# * "THE BEERWARE LICENSE" (Revision 42):
# * cfultz (Caleb Fultz) wrote this code. As long as you retain this 
# * notice, you can do whatever you want with this stuff. If we
# * meet someday, and you think this stuff is worth it, you can
# * buy me a beer in return.
# * ------------------------------------------------------------
#*/


# masbot

import time, sys
from mastodon import Mastodon
from secrets import *

argfile = str(sys.argv[1]) # You will need to pass a .txt file as an argument

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
	mastodon.toot(line)
	time.sleep(3600) #Toot every 1 hour for rate limiting
  
#### Confirm with Mastodon node of choice what
#### what their rate limit is and what they 
#### consider abuse when it comes to automated bots
