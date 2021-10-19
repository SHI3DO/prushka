import pygame as pg
from modules.Sounds import soundsplayer
from pygame.locals import *
from modules.Presence.RPC import discordrpc
from modules.Control import clickhandler
from modules.Graphics.gui import background
from modules.Graphics.gui import mainscene

pg.init()
icon = pg.image.load("./resources/prushka/icon32.ico")
pg.display.set_icon(icon)
screensize = pg.display.Info()
screen = pg.display.set_mode((screensize.current_w, screensize.current_h), DOUBLEBUF)
pg.display.set_caption("prushka!")

END_MUSIC_EVENT = pg.USEREVENT + 0  # ID for music Event
pg.mixer.music.set_endevent(END_MUSIC_EVENT)

clock = pg.time.Clock()

f = open("./resources/tmp/music_list.txt", 'w', encoding='UTF-8')
f.close()

f = open("./resources/tmp/options_screen.txt", 'w', encoding='UTF-8')
f.write("0")
f.close()

f = open("./resources/tmp/chat_screen.txt", 'w', encoding='UTF-8')
f.write("0")
f.close()

f = open("./resources/tmp/options_motion.txt", 'w', encoding='UTF-8')
f.write("0")
f.close()

f = open("./resources/tmp/options_discordrpc.txt", 'r', encoding='UTF-8')
if f.read() == "1":
    discordrpc.discordrpc()

BoldFont = pg.font.Font('./resources/Fonts/GmarketSansTTFBold.ttf', int(screensize.current_h / 40))
LightFont = pg.font.Font('./resources/Fonts/GmarketSansTTFLight.ttf', int(screensize.current_h / 40))
RegularFont = pg.font.Font('./resources/Fonts/GmarketSansTTFMedium.ttf', int(screensize.current_h / 40))

play_img = pg.image.load("./resources/textures/play.png").convert_alpha()
pause_img = pg.image.load("./resources/textures/pause.png").convert_alpha()
stop_img = pg.image.load("./resources/textures/stop.png").convert_alpha()
next_img = pg.image.load("./resources/textures/next.png").convert_alpha()
prev_img = pg.image.load("./resources/textures/prev.png").convert_alpha()
gear_img = pg.image.load("./resources/textures/gear.png").convert_alpha()
circle_img = pg.image.load("./resources/textures/circle.png").convert_alpha()
circlefilled_img = pg.image.load("./resources/textures/circle_filled.png").convert_alpha()
chat_img = pg.image.load("./resources/textures/chat.png").convert_alpha()

glowright_img = pg.image.load("./resources/textures/glow_right.png").convert_alpha()
glowright_img = pg.transform.smoothscale(glowright_img, (screensize.current_w / 8, screensize.current_h))
glowleft_img = pg.image.load("./resources/textures/glow_left.png").convert_alpha()
glowleft_img = pg.transform.smoothscale(glowleft_img, (screensize.current_w / 8, screensize.current_h))

bg_img = pg.image.load("./resources/tmp/bg/a.png").convert_alpha()
bg_img = pg.transform.smoothscale(bg_img, (screensize.current_w, screensize.current_h))

pg.mixer.music.unload()
pg.mixer.music.load(soundsplayer.bgm_selector()[0])
pg.mixer.music.play()

mainLoop = True
while mainLoop:
    screen.fill((0, 0, 0))
    events = pg.event.get()

    if events:
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Mouse
                    clickhandler.LMB(event, screen, screensize, pg)
            if event.type == END_MUSIC_EVENT:
                pg.mixer.music.unload()
                pg.mixer.music.load(soundsplayer.bgm_selector()[0])
                pg.mixer.music.play()

    # GUI
    # background
    background.bg(screen, bg_img)

    # MainScene
    mainscene.play(pg, screen, screensize, clock, LightFont, RegularFont, BoldFont, play_img, pause_img, stop_img,
                   next_img, prev_img, gear_img, circle_img, circlefilled_img, chat_img, glowright_img, glowleft_img)

    dt = clock.tick(120)
    pg.display.update()

pg.quit()
