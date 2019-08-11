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


scope = 'playlist-modify-public'
try:
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

#Create Spotipy Object
spotifyObject = spotipy.Spotify(auth=token)

spotifyObject.trace = True # turn on tracing
spotifyObject.trace_out = True # turn on trace out

temp = spotifyObject.current_user()['id']
spotifyObject.user_playlist_create(temp, 'Daily') 

#print(json.dumps(temp,sort_keys=True, indent=4))