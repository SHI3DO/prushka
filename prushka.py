import pygame as pg
from modules.Sounds import soundsplayer
from modules.Presence.RPC import discordrpc

pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
END_MUSIC_EVENT = pg.USEREVENT + 0  # ID for music Event
pg.mixer.music.set_endevent(END_MUSIC_EVENT)
discordrpc.discordrpc()


def bgm_play():
    pg.mixer.set_num_channels(512)
    pg.mixer.music.load(soundsplayer.bgm_selector())
    pg.mixer.music.play()


bgm_play()

mainLoop = True
while mainLoop:
    events = pg.event.get()
    if events:
        for event in events:
            if event.type == END_MUSIC_EVENT:
                bgm_play()
                print("bgm looped")

    pg.display.update()

pg.quit()
