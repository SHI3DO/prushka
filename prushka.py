import pygame as pg
from modules.Sounds import soundsplayer
from modules.Presence.RPC import discordrpc
from modules.Graphics.gui import upbar

pg.init()
icon = pg.image.load("./resources/prushka/icon32.ico")
pg.display.set_icon(icon)
screensize = pg.display.Info()
screen = pg.display.set_mode((screensize.current_w, screensize.current_h))
pg.display.set_caption("prushka!")

END_MUSIC_EVENT = pg.USEREVENT + 0  # ID for music Event
pg.mixer.music.set_endevent(END_MUSIC_EVENT)
discordrpc.discordrpc()

clock = pg.time.Clock()


def bgm_play():
    pg.mixer.music.unload()
    sel = soundsplayer.bgm_selector()
    pg.mixer.music.load(sel[0])
    pg.mixer.music.play()


BoldFont = pg.font.Font('./resources/Fonts/GmarketSansTTFBold.ttf', int(screensize.current_h/40))
LightFont = pg.font.Font('./resources/Fonts/GmarketSansTTFLight.ttf', int(screensize.current_h/40))
RegularFont = pg.font.Font('./resources/Fonts/GmarketSansTTFMedium.ttf', int(screensize.current_h/40))

bgm_play()
mainLoop = True
while mainLoop:
    screen.fill((0, 0, 0))
    events = pg.event.get()
    if events:
        for event in events:
            if event.type == END_MUSIC_EVENT:
                bgm_play()
                print("bgm looped")

    # GUI
    # fps
    upbar.fps_shower(screen, screensize, LightFont, clock)
    # OptionScreen
    upbar.Optionscreenopener(pg, screen, screensize)
    # playing_music
    upbar.music_shower(pg, screen, screensize, RegularFont)

    clock.tick(60)
    pg.display.update()

pg.quit()
