import pygame as pg
from modules.Sounds import soundsplayer
from pygame.locals import *
from modules.Presence.RPC import discordrpc
from modules.Graphics.gui import upbar
from modules.Control import clickhandler
from modules.Graphics.gui import background
from modules.Graphics.gui import bottombar

pg.init()
icon = pg.image.load("./resources/prushka/icon32.ico")
pg.display.set_icon(icon)
screensize = pg.display.Info()
screen = pg.display.set_mode((screensize.current_w, screensize.current_h), DOUBLEBUF)
pg.display.set_caption("prushka!")

END_MUSIC_EVENT = pg.USEREVENT + 0  # ID for music Event
pg.mixer.music.set_endevent(END_MUSIC_EVENT)
# discordrpc.discordrpc()

clock = pg.time.Clock()

f = open("./resources/tmp/music_list.txt", 'w', encoding='UTF-8')
f.close()


def bgm_play():
    pg.mixer.music.unload()
    pg.mixer.music.load(soundsplayer.bgm_selector()[0])
    pg.mixer.music.play()


BoldFont = pg.font.Font('./resources/Fonts/GmarketSansTTFBold.ttf', int(screensize.current_h / 40))
LightFont = pg.font.Font('./resources/Fonts/GmarketSansTTFLight.ttf', int(screensize.current_h / 40))
RegularFont = pg.font.Font('./resources/Fonts/GmarketSansTTFMedium.ttf', int(screensize.current_h / 40))

play_img = pg.image.load("./resources/textures/play.png").convert_alpha()
pause_img = pg.image.load("./resources/textures/pause.png").convert_alpha()
stop_img = pg.image.load("./resources/textures/stop.png").convert_alpha()
next_img = pg.image.load("./resources/textures/next.png").convert_alpha()
prev_img = pg.image.load("./resources/textures/prev.png").convert_alpha()

bg_img = pg.image.load("./resources/tmp/bg/a.png").convert_alpha()
bg_img = pg.transform.smoothscale(bg_img, (screensize.current_w, screensize.current_h))

bgm_play()
mainLoop = True
while mainLoop:
    screen.fill((0, 0, 0))
    events = pg.event.get()

    if events:
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Mouse
                    clickhandler.LMB(event, screensize, pg)
            if event.type == END_MUSIC_EVENT:
                bgm_play()
                print("bgm looped")

    # GUI
    # background
    background.bg(screen, bg_img)
    bottombar.bottom(pg, screen, screensize, RegularFont)
    bottombar.bottomnews(pg, screen, screensize)
    # fps
    upbar.Fps_shower(screen, screensize, LightFont, clock)
    # OptionScreen
    upbar.Optionscreenopener(pg, screen, screensize)
    # playing_music
    upbar.Music_shower(pg, screen, screensize, RegularFont, play_img, pause_img, stop_img, next_img, prev_img)

    dt = clock.tick(120)
    pg.display.update()

pg.quit()
