import os
import sys
import spotipy
import spotipy.util as util
import json
import webbrowser
from json.decoder import JSONDecodeError

#Get the username from terminal
username = '222lflk6h5pichsj4goxz64zi'
client_id = 'd92a8649deee4f2cb07d8f023647b829'
client_secret = '6d3e00471d1c4930b49f17b5847e17ec'
redirect_uri = 'http://google.com/'

#User ID: 222lflk6h5pichsj4goxz64zi


scope = 'user-library-read'
try:
    token = util.prompt_for_user_token(username, None, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, None, client_id, client_secret, redirect_uri)

#Create Spotipy Object
spotifyObject = spotipy.Spotify(auth=token)