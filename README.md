# CherrySteam
A tool to pull user and game information from Valve's Steam platform. 

<b><u>References</u></b>
<br>
<a href="https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0001.29">Steam User API</a>

Required: SteamID and Steam Web API Key

Initial Use Case:
- Pull list of owned games + number of hours each game has been played
- Convert to JSON --> CSV to manually populate a Google Sheet

v0.1
- Tool prints total games owned to console
- Tool prints name of game and playtime converted into hours

v0.2
- Tool outputs total games name where user has above 0 seconds of playtime in game to local CSV file
- Tool outputs total game playtime where where user has above 0 seconds of playtime to local CSV file
