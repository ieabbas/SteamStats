#To access config api keys / other sensitive info use following format
#config.steam_api_key / config.steam_domain

import json
import requests
import random
#Con = config.p ignored byt gitignore
import config as con
import csvfile
import csv

steamApiKey = con.steam_api_key
steamID = con.steamID

#To gather information about the achievements a user has for any given game, need to hit GetOwnedGames(v0001)
#Steam API link formatting for "GetOwnedGames"
#https://developer.valvesoftware.com/wiki/Steam_Web_API#GetOwnedGames_.28v0001.29
def printSteamUserOwnedGames():
    #Steam API link formatting for "GetOwnedGames"
    slink1 = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink2 = "&steamid=" + steamID + "&include_appinfo=1&format=json"
    slink = slink1 + steamApiKey + slink2

    #Sent API Get request and save respond to a variable
    r = requests.get(slink)

    #Convert to JSON and save to another variable
    steam = r.json()

    #Getting integer value of total games owned
    totalGames = str(steam["response"]["game_count"])

    #Output total games owned
    print("Cherrius owns a total of " + totalGames + " games")

    #Some logic for getting a random game from account with over 0 seconds of playtime
    steamGame = ""
    steamGames = []

    for num,item in enumerate (steam["response"]["games"]):
        num+=1
        if item["playtime_forever"] > 0:
            steamGame = item["name"]
            steamGames.append(steamGame)
            steamPlayTimeSeconds = item["playtime_forever"]
            achievements_earned = item["achievements"]["total"]
            achievements_possible = item["achievements"]["possible"]
            print("Cherrius has played the game " + item["name"] + " for " + str(round(float(steamPlayTimeSeconds)/60, 2)) + " hours total.")


#To gather information about the achievements a user has for any given game, need to hit GetUserStats(v0001)
#Steam API link formatting for "GetUserStats"
#https://developer.valvesoftware.com/wiki/Steam_Web_API#GetUserStatsForGame_.28v0001.29
def writeOwnedGameStats():
    #Steam API link formatting for "GetOwnedGames"
   # Set the API endpoint URL
    endpoint = "https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/"

    # Set the API parameters
    params = {"key": "YOUR_API_KEY", "steamid": steamID, "appid": "appid", "format": "json"}

    # Open a CSV file for writing
    with open("CherrySteamOutput.csv", "w", newline="") as csvfile:
        # Create a CSV writer
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow(["GameName", "TotalPlaytime", "AchievementsEarned", "AchievementsPossible", "100 Percented Game?"])
        
        #Establish the initial response and make sure a JSON object is actually returned
        try:
            response = requests.get(endpoint, params=params)
            steam = response.json()
        except json.decoder.JSONDecodeError as e:
            print(f'Error decoding json: {e}')
            print(response.status_code)

        # Get the list of games from the response
        games = steam["response"]["games"]
        
        for game in steam:
            appid = game["appid"]
            playtime = game["playtime_forever"]
            params["appid"] = appid
            # Make the API request
            response = requests.get(endpoint, params=params)
            data = response.json()
            if playtime > 0:
                game_name = data["playerstats"]["gameName"]
                total_playtime = round(float(playtime) / 60 / 60, 2)
                achievements = data["playerstats"]["achievements"]
                achievements_earned = 0
                achievements_possible = 0
                fullyComplete = "No"
                for achievement in achievements:
                    if achievement["achieved"]:
                        achievements_earned += 1
                    achievements_possible += 1
                if achievements_earned == achievements_possible:
                    fullyComplete = "Yes"
                writer.writerow([game_name, total_playtime, achievements_earned, achievements_possible, fullyComplete])


def main():
    printSteamUserOwnedGames()
    #writeOwnedGameStats()

if __name__ == "__main__":
    main()