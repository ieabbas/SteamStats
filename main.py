#To access config api keys / other sensitive info use following format
#config.steam_api_key / config.steam_domain

import json
import requests
import random
import config as con
import csvfile
import csv

#To gather information about the achievements a user has for any given game, need to hit GetOwnedGames(v0001)
#Steam API link formatting for "GetOwnedGames"
#https://developer.valvesoftware.com/wiki/Steam_Web_API#GetOwnedGames_.28v0001.29
def getOwnedGames():
    #Steam API link formatting for "GetOwnedGames"
    slink1 = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink2 = "&steamid=" + con.steamID + "&include_appinfo=1&format=json"
    slink = slink1 + con.steam_api_key + slink2

    #Sent API Get request and save respond to a variable
    r = requests.get(slink)

    #Convert to JSON and save to another variable
    steam = r.json()

    #Getting integer value of total games owned
    totalGames = str(steam["response"]["game_count"])

    #Output total games owned
    print("Cherrius owns a total of " + totalGames + " games")

    #Some logic for retrieving games from user account with over 0 seconds of playtime
    steamGame = ""
    steamGames = []

    for num,item in enumerate (steam["response"]["games"]):
        num+=1
        if item["playtime_forever"] > 0:
            #Establishes the steamGame object as a DICTIONARY {} and not a list of strings
            steamGame = {
                "name": item["name"],
                "playtime_forever": item["playtime_forever"]
            }
            steamGames.append(steamGame)
    return steamGames

def writeOwnedGameStats(steam_games):
    # Open a CSV file for writing
    with open("CherrySteamOutput.csv", "w", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(["GameName", "TotalPlaytime"])

        # Write the rows for each game
        for game in steam_games:
            game_name = game["name"]
            total_playtime = round(float(game["playtime_forever"]) / 60, 2)
            writer.writerow([game_name, total_playtime])

#Main function to:
    # a) get all owned games that have a playtime_forever above 0 seconds 
    # b) write the records to a CSV file
def main():
    my_Games = getOwnedGames()
    writeOwnedGameStats(my_Games)

if __name__ == "__main__":
    main()
