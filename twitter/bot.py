#/*
# * ------------------------------------------------------------
# * "THE BEERWARE LICENSE" (Revision 42):
# * cfultz (Caleb Fultz) wrote this code. As long as you retain this 
# * notice, you can do whatever you want with this stuff. If we
# * meet someday, and you think this stuff is worth it, you can
# * buy me a beer in return.
# * ------------------------------------------------------------
#*/
# bot.py

import tweepy
import time
import sys
import keyring

def set_auth():
    """
    Purpose: 
        Create an OAuthHandler instance sicne Twitter requires all requests
        to use OAuth for authentication. If it fails (because the auth info
        is not stored in the user's keyring), it returns False.
    Inputs: 
        None
    Outputs:
        The auth instance. If it fails, a boolean "False" is returned instead.
    """
    try:
        auth = tweepy.OAuthHandler(keying.get_password('consumer','key'),
                keyring.get_password('consumer','secret'))
        auth.set_access_token(keyring.get_password('access','token'),
                keyring.get_password('access','secret'))
        return auth
    except:
        return False

# This allows for you to pass a text file of your choosing to tweet each line
argfile = str(sys.argv[1]) 
if not argfile:
    print('Expected input file as system argument, exiting')
    SystemExit

auth = set_auth()
# If you haven't run this before or have not set the valid info, you will be
# prompted to enter the information.
if not auth:
    import getpass
    keyring.set_password('consumer','key',
            getpass.getpass(prompt='Please provide the consumer key: '))
    keyring.set_password('consumer','secret',
            getpass.getpass(prompt='Please provide the consumer password: '))
    keyring.set_password('access','token',
            getpass.getpass(prompt='Please provide the access token: '))
    keyring.set_password('access','secret',
            getpass.getpass(prompt='Please provide the access password: '))
    auth = set_auth()

#Construct the API instance
api = tweepy.API(auth) 

# Parse the given file
with open(argfile,'r') as f1:
    f=f1.readlines()

# For every line in the file, process it as a status update.
for line in f:
    api.update_status(status=line)
    time.sleep(3600) # Tweet every 1 hour for rate limiting.
### Note that the time can be shortened significantly lower, however
### you need to follow the Twitter guidelines
### or you'll have your bot and account banned.
