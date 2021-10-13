import pygame as pg
from modules.Sounds import soundsplayer
from modules.Presence.RPC import discordrpc
import os

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
    pg.mixer.set_num_channels(512)
    sel = soundsplayer.bgm_selector()
    pg.mixer.music.load(sel[0])
    pg.mixer.music.play()


def music_shower():
    if os.path.isfile("./resources/tmp/music_playing.txt"):
        f = open("./resources/tmp/music_playing.txt", 'r')
        musictitle = RegularFont.render(f"now plaing - {f.read()}", True, (255, 255, 255))
        screen.blit(musictitle, (screensize.current_w * 0.99 - musictitle.get_width(), screensize.current_h / 90))


def fps_shower():
    fps = LightFont.render(f"{round(clock.get_fps())}", True, (0, 255, 0))
    screen.blit(fps, (screensize.current_w / 128, screensize.current_h / 90))


def Optionscreenopener():
    OptionScreenopener = pg.Surface((screensize.current_w * 0.025, screensize.current_h))
    OptionScreenopener.set_alpha(30)
    OptionScreenopener.fill((255, 255, 255))
    screen.blit(OptionScreenopener, (screensize.current_w * 0.975, 0))


BoldFont = pg.font.Font('./resources/Fonts/GmarketSansTTFBold.ttf', 20)
LightFont = pg.font.Font('./resources/Fonts/GmarketSansTTFLight.ttf', 20)
RegularFont = pg.font.Font('./resources/Fonts/GmarketSansTTFMedium.ttf', 20)

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

    # fps
    fps_shower()
    # OptionScreen
    Optionscreenopener()
    # playing_music
    music_shower()

    clock.tick(120)
    pg.display.update()

pg.quit()
