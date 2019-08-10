import os
import sys
import json
spotipy = sys.path.insert(0, './spotipy/util.py')
import webbrowser
from json.decoder import JSONDecodeError

#Get the username from terminal
username = sys.argv[1]

#User ID: 222lflk6h5pichsj4goxz64zi
try:
	token = util.prompt_for_user_token(username)
except:
	os.remove(f".cache-{username}")
	token = util.prompt_for_user_token(username)

#Create Spotipy Object
spotifyObject = spotipy.Spotify(auth=token)