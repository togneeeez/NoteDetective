# This file will be used to handle user's
# API requests.
import json, requests
from dep import tui_handler
from dep.tui_handler import Window

main_w = Window('main')

# Search for artist (name given by user).
def s_artist(api_url, a_name):

    # Request the DATA ('fmt=json' specified to get an API response in JSON format.
    req = requests.get(api_url + "artist/?fmt=json&query={}".format(a_name))
    cont = req.content

    # Load JSON content into a dictionary.
    res = json.loads(cont)

    artists = res["artists"]
    print("")

    # Print each artist found (if there are more than one).
    if len(artists) > 0:
        for i in range(len(artists)):
            a = artists[i]
            if ("country" in a.keys()):
                print(str(i+1) + ") " + a["name"] + " (Country: " + a["country"] + ")")
            else:
                print(str(i+1) + ") " + a["name"] + " (Country: None)")
    
        # User input.
        print("")
        scelta = int(input("——> Choose artist: ")) - 1
        print("")

        # Check input validity and print corresponding info.
        if scelta in range(len(artists)):
            a = artists[scelta]
            t = a["type"].capitalize()

            # Artist title.
            main_w.title(60, 1, a["name"] + " (" + t + ")")

            # Artist details.
            main_w.option(100, t + " Disambiguation (Description):" + "\"" + a["disambiguation"] + "\"")
            main_w.option(60, t + " Country: " + a["country"])
            main_w.option(60, t + " ID: " + a["id"])
            main_w.option(60, t + " Ended? " + str(a["life-span"]["ended"]) + "\n")
    else:
        print("No artists found with given name!\n")

# Search for songs (name given by user).
def s_song(api_url, s_name):

    # Request the DATA ('fmt=json' specified to get an API response in JSON format.
    req = requests.get(api_url + "release-group/?fmt=json&query={}".format(s_name))
    cont = req.content

    # Load JSON content into a dictionary.
    res = json.loads(cont)

    songs = res['release-groups']
    print("")

    # Print each song found (if there are more then one).
    if len(songs) > 0:
        for i in range(len(songs)):
            song = songs[i]
            artist = song["artist-credit"][0]["name"]
            print(str(i+1) + ") " + song["title"] + " (" + artist + ")")
    
        # User input.
        print("")
        scelta = int(input("——> Choose song: ")) - 1
        print("")

        if scelta in range(len(songs)):
            s = songs[scelta]
            t = s["title"]
            a = s["artist-credit"][0]["name"]

            # Song title.
            main_w.title(60, 1, t)

            # Song details.
            main_w.option(100, "Author: " + a)
            main_w.option(60, "Type: " + s["primary-type"])

            # Song genres string generation.
            g_string = ""
            g = "None"
            if "tags" in s.keys():
                g = s["tags"]
                for i in range(len(g)):
                    if i == 0 and i < len(g)-1:
                        g_string += g[i]["name"].capitalize() + ", "
                    elif i == 0 and i == len(g)-1:
                        g_string += g[i]["name"].capitalize()
                    elif i < len(g)-1:
                        g_string += g[i]["name"] + ", "
                    else:
                        g_string += g[i]["name"]
            else:
                g_string += g

            main_w.option(60, "Genre: " + g_string)
            main_w.option(60, "ID: " + s["id"])
            main_w.option(60, "Release Date: " + s["first-release-date"])

            yt_url = "https://www.youtube.com/results?search_query="
            t_plus = t.replace(" ", "+")
            main_w.option(100, "YouTube URL: " + yt_url + t_plus + "+-+" + a + "\n")
    else:
        print("No songs found with given name!\n")

# Test connection to API_URL (MusicBrainz's API main URL), check for HTTP 200 Response (OK).
def test_conn(t_url):
    print("Testing API connection...")
    test = requests.get(t_url)
    if test.status_code == 200:
        print("Connection succeded!\n")

# Handle API requests, ask for search type and query:
# - type: MusicBrainz's type of entity to search for;
# - query: User's input to send to the API.
def api_req(api_b_url):
    # Describe main window.
    print("")
    main_w.title(60, 3, "NoteDetective: API requests")
    main_w.option(25, "1) Search by: Artist")
    main_w.option(25, "2) Search by: Song")
    main_w.option(25, "3) Search by: Album")  
    main_w.option(25, "0) Back\n")

    # Try to get input from user and handle exceptions.
    try:
        ERR_TEXT = "INPUT_ERR: Choice not available or invalid input!"
        avail_choices = [0, 1, 2, 3]
        scelta = int(input("——> Choose filter: "))
        if (scelta not in avail_choices):
            print("")
            raise ValueError(ERR_TEXT)
    except Exception as e:
        main_w.title(60, 1, ERR_TEXT)
        scelta = ""

    # Choose next steps.
    # Scelta = 1 --> Ask for artist name.
    # Scelta = 2 --> Ask for song name.
    # Scelta = 3 --> Ask for album name.
    if scelta == 1:
        scelta = input("——> Type artist name: ")
        s_artist(api_b_url, scelta)
    elif scelta == 2:
        scelta = input("——> Type song name: ")
        s_song(api_b_url, scelta)
    elif scelta == 3:
        scelta = input("——> Type album name: ")
        s_album(scelta)
