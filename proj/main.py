# The API root URL is 'https://musicbrainz.org/ws/2/'
# (from MusicBrainz's offical docs)

API_ROOT_URL = "https://musicbrainz.org/ws/2/"

# MusicBrainz's API is made up of 13 resources:
# area, artist, event, genre, instrument, label, place, recording,
# release, release-group, series, work, url.
# And other non-core resources:
# rating, tag, collection.

# MusicBrainz's API allows us to use three different GET
# requests:
# - lookup: /<ENTITY_TYPE>/<MBID>?inc=<INC>;
# - browse: /<RESULT_ENTITY_TYPE>?<BROWSING_ENTITY_TYPE>=<MBID>&limit=<LIMIT>&offset=<OFFSET>&inc=<INC>;
# - search: /<ENTITY_TYPE>?query=<QUERY>&limit=<LIMIT>&offset=<OFFSET>.

# We're also given unique identifiers such as:
# discid, isrc, iswc.
# Let's provide a TUI to check connection to the API.

from dep import tui_handler
from dep.tui_handler import Window

# We'll also need a way to handle user's API requests.
from dep import req_handler
from dep.req_handler import test_conn, api_req

main_w = Window('main')

scelta = ""
while scelta == "":
    # Describe window parameters.
    main_w.title(60, 3, 'NoteDetective')
    main_w.option(25, '1) Test API connection')
    main_w.option(25, '2) API requests')
    main_w.option(25, '0) Exit\n')

    # Catch input exceptions.
    try:
        ERR_TEXT = "INPUT_ERR: Choice not available or invalid input!"
        avail_choices = [0, 1, 2]
        scelta = int(input("——> Choose operation: "))
        if (scelta not in avail_choices):
            print("")
            raise ValueError(ERR_TEXT)
    except Exception as e:
        main_w.title(60, 1, ERR_TEXT)
        scelta = ""

    # Choose next steps.
    if scelta == 1:
        test_conn(API_ROOT_URL)
        scelta = ""
    elif scelta == 2:
        api_req(API_ROOT_URL)
        scelta = ""
    else:
        print("Goodbye!\n")
