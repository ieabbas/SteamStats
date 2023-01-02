#To access config api keys / other sensitive info use following format
#config.steam_api_key / config.steam_domain


import requests
import random
import config

steamApiKey = config.steam_api_key
steamID = config.steamID

#Steam API link formatting for "GetOwnedGames"
slink1 = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
slink2 = "&steamid=" + steamID + "&include_appinfo=1&format=json"
slink = slink1 + steamApiKey + slink2

#Sent API Get request and save respond to a variable
r = requests.get(slink)

#convert to JSON and save to another variable
steam = r.json()

#JSON output with information about each game owned
print(steam)
#https://developer.valvesoftware.com/wiki/Steam_Web_API#GetOwnedGames_.28v0001.29

#Getting integer value of total games owned
totalGames = str(steam["response"]["game_count"])

#Output total games owned
print(totalGames)

#Some logic for getting a random game from account with over 10 hours playtime
steamGame = ""
steamGames = []

for num,item in enumerate (steam["response"]["games"]):
    num+=1
    if item["playtime_forever"] > 0:
        steamGame = item["name"]
        steamGames.append(steamGame)
    
steamRec = "".join((random.sample(steamGames, k=1)))

print(steamRec)
