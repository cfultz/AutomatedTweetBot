### This file is esientially a copy of the one found in the Mastodon.py 
# documentation. Will work to clean this up and make it a bit better

### secure way to deliever the goods

import sys, time
from mastodon import Mastodon

# Register app - only once!
'''
Mastodon.create_app(
     'pytooterapp',
     api_base_url = 'https://mastodon.social',
     to_file = 'pytooter_clientcred.secret'
)
'''

# Log in - either every time, or use persisted
'''
mastodon = Mastodon(
    client_id = 'CLIENT_SECRET',
    api_base_url = 'https://mastodon.cloud'
)
mastodon.log_in(
   'YOUR_EMAIL',
    'YOUR_PASSWORD',
    to_file = 'pytooter_usercred.secret'
)
'''

# Create actual API instance
mastodon = Mastodon(
    access_token = 'ACCESS_TOKEN_SECRET',
    api_base_url = 'https://mastodon.cloud'
)
