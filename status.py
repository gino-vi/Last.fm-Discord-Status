from pypresence import Presence, Activity
import logging
import pylast
import time
import random
import json
from configparser import ConfigParser

import asyncio
import discord

#read values from info.ini
config = ConfigParser()
config.read('info.ini')
config.get('last.fm', 'API_KEY')
config.get('last.fm', 'API_SECRET')
config.get('last.fm', 'username')
config.get('last.fm', 'password')
config.get('discord', 'client_id')

#last.fm information
API_KEY = config['last.fm']['API_KEY']
API_SECRET = config['last.fm']['API_SECRET']
username = config['last.fm']['username']
password = config['last.fm']['password']
password_hash = pylast.md5(password)
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

# discord information
image = config['discord']['image'] # fetches image from your rich presence assets
client_id = config['discord']['client_id']
RPC = Presence(client_id) 
RPC.connect() 

logging.basicConfig(level=logging.DEBUG)
seconds_ago = int(time.time())
started_at = seconds_ago

track = network.get_user(username).get_now_playing()
playcount = network.get_user(username).get_playcount()
recent = network.get_user(username).get_recent_tracks(limit=1)

print(RPC.update(state=f"{playcount} plays on {username}", details=f"Playing 🎵 {track} 🎵", large_image = image, start = started_at))  # Sets the presence
time.sleep(20) # Wait 20 seconds

while True:  # The presence will stay on as long as the program is running
    track = network.get_user(username).get_now_playing()
    print("Updating status...")
    print(RPC.update(state=f"{playcount} plays on {username}", details=f"Playing 🎵 {track} 🎵", large_image = image, start = started_at))
    time.sleep(20) # Will update rich presence every x seconds
