import requests
from time import time
import json

# Paste your client ID and client secret here
CLIENT_ID = 'YOUR CLIENT ID'
CLIENT_SECRET = 'YOUR CLIENT SECRET'
AUTH_URL = 'https://accounts.spotify.com/api/token'


# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

# header for GET requests
headers = {
    'Authorization': 'Bearer {token}'.format(token = access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# --------------------------------------------------- #

# pull any user data given their ID
user_ID = input("Paste/Enter Valid User ID: ")

userInfo = requests.get(BASE_URL + 'users/' + user_ID, headers=headers)
userInfo = userInfo.json()

userDisplayName = userInfo['display_name']

userPlaylists = requests.get(BASE_URL + 'users/' + user_ID + '/playlists', headers=headers)
userPlaylists = userPlaylists.json()

compiledPlaylistDict = {}

print(f"Compiling {userDisplayName}'s Playlists Into New Text File.....")
try:
    numOfUserPlaylists = len(userPlaylists)
    for playlistNum in range(numOfUserPlaylists):

        playlistJson = userPlaylists['items'][playlistNum]
        playList_ID = playlistJson['id']
        playList_name = playlistJson['name']

        playlistTracks = requests.get(BASE_URL + 'playlists/' + playList_ID + '/tracks', headers=headers)
        playlistTracks = playlistTracks.json()

        print(f"Compiling Playlist {playlistNum + 1} / {numOfUserPlaylists}...")
        trackDictForCurrentPlaylist = {}

        for j in range(len(playlistTracks['items'])):
            try:
                trackName = str(playlistTracks['items'][j]['track']['name'])
                trackID = str(playlistTracks['items'][j]['track']['id'])

                trackFeatures = requests.get(BASE_URL + 'audio-features/' + trackID, headers=headers)
                trackFeatures = trackFeatures.json()

                trackValence = trackFeatures['valence']
                trackTempo = trackFeatures['tempo']
                trackEnergy = trackFeatures['energy']


                trackDictForCurrentPlaylist.update({
                    trackID: {
                        'track_name': trackName,
                        'track_valence': trackValence,
                        'track_tempo': trackTempo,
                        'track_energy': trackEnergy
                    }
                })
            except Exception as e:
                print('\nAn error occurred with one of the tracks: \n' + str(e))
                pass

        compiledPlaylistDict[playList_ID] = trackDictForCurrentPlaylist

        print('Compiled.')

except Exception as e:
    print('\nAn error occurred with a playlist: \n' + str(e))


newFileName = userDisplayName + '-(' + user_ID + ')' + '--' + str(round(time() * 1000))

# Make sure you are in the 'Spotify-API-Mini-Project' directory (or whatever directory all files/folders are in).
with open('Compiled Playlists JSON Files/' + newFileName + '.json', 'w') as outfile:
    json.dump(compiledPlaylistDict, outfile)
print("Completed!")

 







