import os
import random


def bgm_selector():
    file_list = os.listdir("./resources/Sounds/ES")
    toplay = random.randrange(0, len(file_list))
    print(f"now playing - {file_list[toplay]}")
    return f"./resources/Sounds/ES/{file_list[toplay]}"
