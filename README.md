# Last.fm-Discord-Status
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

Uses [pypresence](https://github.com/qwertyquerty/pypresence) and [pylast](https://github.com/pylast/pylast)

This script will set your Discord rich presence to whatever you're listening to on last.fm, like so:

![Screenshot](https://i.imgur.com/loHCQao.png)

You'll need the following:

## **1. Last.fm API key and Secret**
Head over to https://www.last.fm/api/account/create and create an API account. It doesn't matter what you put in the fields. Once you hit Submit, you should see something like this:

![Screenshot](https://i.imgur.com/mO4YkSk.png)

Copy and paste the API Key as well as the Shared secret value into info.ini in the `API_KEY =` line and `API_SECRET =` line.

## **2. Last.fm Account Information**
Enter your last.fm username and password in the `username = ` and `password = `  lines respectively in info.ini. This will be used to connect to the network.

## **3. Discord Client ID**
Then, go to https://discordapp.com/developers/ and press the New Application button. Take note that the name you set for the application will be the game you'll be "Playing".

Under the name of your application will be the client ID, put it into the `client_id =` line in info.ini.

## **4. Image**
Discord allows you to upload art assets for usage. From your app page in the Developer Portal, click on Rich Presence and then Art Assets. Upload the image you want to use, and then enter the filename of the asset in the `image = ` line in info.ini. 
