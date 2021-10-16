import os
import random
from modules.utils import jsonreader
from modules.utils import meipath


def bgm_selector():
    bgm_list = os.listdir(meipath.meipass("resources/Sounds/ES"))
    bgm_list = [file for file in bgm_list if file.endswith(".json")]
    for i in range(0, len(bgm_list)):
        bgm_list[i] = meipath.meipass("resources/Sounds/ES/" + bgm_list[i])

    print(f"Indexing Songs - {bgm_list}")

    bgm_location_list = []
    bgm_title_list = []
    bgm_artist_list = []

    for i in range(0, len(bgm_list)):
        info = jsonreader.get(bgm_list[i])
        bgm_location_list.append(f"{info.location}")
        bgm_title_list.append(f"{info.title}")
        bgm_artist_list.append(f"{info.artist}")

    toplay = random.randrange(0, len(bgm_location_list))
    print(toplay)

    returnval = [bgm_location_list[toplay], bgm_title_list[toplay], bgm_artist_list[toplay]]
    f = open(meipath.meipass("resources/tmp/music_playing.txt"), 'w', encoding='UTF-8')
    f.write(str(returnval[1]))
    f.close()
    f = open(meipath.meipass("resources/tmp/music_list.txt"), 'a', encoding='UTF-8')
    f.write(str(returnval[0]) + "\n")
    f.close()
    print(f"now playing - {returnval[1]}")
    return returnval

