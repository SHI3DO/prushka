import pygame as pg
from modules.Sounds import soundsplayer
from modules.Presence.RPC import discordrpc
from modules.Control import clickhandler
from modules.Graphics.gui import background
from modules.Graphics.gui import mainscene
from modules.utils import downloader
from modules.Control import keycontrol
from modules.utils import reqdir


pg.init()
icon = pg.image.load("./resources/prushka/icon32.ico")
pg.display.set_icon(icon)
screensize = pg.display.Info()
screen = pg.display.set_mode((screensize.current_w, screensize.current_h))
pg.display.set_caption("prushka!")

END_MUSIC_EVENT = pg.USEREVENT + 0  # ID for music Event
pg.mixer.music.set_endevent(END_MUSIC_EVENT)
pg.mixer.set_num_channels(64)

clock = pg.time.Clock()

reqdir.make()

downloader.download("http://parfaitgds.kro.kr/p/test.png", "./resources/runtime/info/info.png")
downloader.download("http://parfaitgds.kro.kr/p/testavtr.png", "./resources/runtime/info/avatar.png")

f = open("./resources/runtime/options_discordrpc.txt", 'r', encoding='UTF-8')
if f.read() == "1":
    discordrpc.discordrpc()

BoldFont = pg.font.Font('./resources/Fonts/GmarketSansTTFBold.ttf', int(screensize.current_h / 40))
LightFont = pg.font.Font('./resources/Fonts/GmarketSansTTFLight.ttf', int(screensize.current_h / 40))
RegularFont = pg.font.Font('./resources/Fonts/GmarketSansTTFMedium.ttf', int(screensize.current_h / 40))

BigBoldFont = pg.font.Font('./resources/Fonts/GmarketSansTTFBold.ttf', int(screensize.current_h / 30))
BigLightFont = pg.font.Font('./resources/Fonts/GmarketSansTTFLight.ttf', int(screensize.current_h / 30))
BigRegularFont = pg.font.Font('./resources/Fonts/GmarketSansTTFMedium.ttf', int(screensize.current_h / 30))

SBigBoldFont = pg.font.Font('./resources/Fonts/GmarketSansTTFBold.ttf', int(screensize.current_h / 15))
SBigLightFont = pg.font.Font('./resources/Fonts/GmarketSansTTFLight.ttf', int(screensize.current_h / 15))
SBigRegularFont = pg.font.Font('./resources/Fonts/GmarketSansTTFMedium.ttf', int(screensize.current_h / 15))

play_img = pg.image.load("./resources/textures/play.png").convert_alpha()
pause_img = pg.image.load("./resources/textures/pause.png").convert_alpha()
stop_img = pg.image.load("./resources/textures/stop.png").convert_alpha()
next_img = pg.image.load("./resources/textures/next.png").convert_alpha()
prev_img = pg.image.load("./resources/textures/prev.png").convert_alpha()
gear_img = pg.image.load("./resources/textures/gear.png").convert_alpha()
circle_img = pg.image.load("./resources/textures/circle.png").convert_alpha()
circlefilled_img = pg.image.load("./resources/textures/circle_filled.png").convert_alpha()
chat_img = pg.image.load("./resources/textures/chat.png").convert_alpha()
beat_img = pg.image.load("./resources/textures/beat.png").convert_alpha()


maininfo_img = pg.image.load("./resources/runtime/info/info.png").convert_alpha()
avatar_img = pg.image.load("./resources/runtime/info/avatar.png").convert_alpha()
avatar_img = pg.transform.smoothscale(avatar_img, (screensize.current_h / 8, screensize.current_h / 8))

glowright_img = pg.image.load("./resources/textures/glow_right.png").convert_alpha()
glowright_img = pg.transform.smoothscale(glowright_img, (screensize.current_w / 8, screensize.current_h))
glowleft_img = pg.image.load("./resources/textures/glow_left.png").convert_alpha()
glowleft_img = pg.transform.smoothscale(glowleft_img, (screensize.current_w / 8, screensize.current_h))

bg_img = pg.image.load("./resources/runtime/bg/a.png").convert_alpha()
bg_img = pg.transform.smoothscale(bg_img, (screensize.current_w, screensize.current_h))

pg.mixer.music.unload()
pg.mixer.music.load(soundsplayer.bgm_selector()[0])
pg.mixer.music.play()

mainLoop = True
while mainLoop:
    screen.fill((0, 0, 0))
    events = pg.event.get()
    dt = clock.tick(120)

    if events:
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Mouse
                    clickhandler.LMB(event, screen, screensize, pg)

            if event.type == pg.KEYDOWN:
                if event.key == pg.key.key_code("a"):
                    keycontrol.inputkey("a", pg)
                if event.key == pg.key.key_code("b"):
                    keycontrol.inputkey("b", pg)
                if event.key == pg.key.key_code("c"):
                    keycontrol.inputkey("c", pg)
                if event.key == pg.key.key_code("d"):
                    keycontrol.inputkey("d", pg)
                if event.key == pg.key.key_code("e"):
                    keycontrol.inputkey("e", pg)
                if event.key == pg.key.key_code("f"):
                    keycontrol.inputkey("f", pg)
                if event.key == pg.key.key_code("g"):
                    keycontrol.inputkey("g", pg)
                if event.key == pg.key.key_code("h"):
                    keycontrol.inputkey("h", pg)
                if event.key == pg.key.key_code("i"):
                    keycontrol.inputkey("i", pg)
                if event.key == pg.key.key_code("j"):
                    keycontrol.inputkey("j", pg)
                if event.key == pg.key.key_code("k"):
                    keycontrol.inputkey("k", pg)
                if event.key == pg.key.key_code("l"):
                    keycontrol.inputkey("l", pg)
                if event.key == pg.key.key_code("m"):
                    keycontrol.inputkey("m", pg)
                if event.key == pg.key.key_code("n"):
                    keycontrol.inputkey("n", pg)
                if event.key == pg.key.key_code("o"):
                    keycontrol.inputkey("o", pg)
                if event.key == pg.key.key_code("p"):
                    keycontrol.inputkey("p", pg)
                if event.key == pg.key.key_code("q"):
                    keycontrol.inputkey("q", pg)
                if event.key == pg.key.key_code("r"):
                    keycontrol.inputkey("r", pg)
                if event.key == pg.key.key_code("s"):
                    keycontrol.inputkey("s", pg)
                if event.key == pg.key.key_code("t"):
                    keycontrol.inputkey("t", pg)
                if event.key == pg.key.key_code("u"):
                    keycontrol.inputkey("u", pg)
                if event.key == pg.key.key_code("v"):
                    keycontrol.inputkey("v", pg)
                if event.key == pg.key.key_code("w"):
                    keycontrol.inputkey("w", pg)
                if event.key == pg.key.key_code("x"):
                    keycontrol.inputkey("x", pg)
                if event.key == pg.key.key_code("y"):
                    keycontrol.inputkey("y", pg)
                if event.key == pg.key.key_code("z"):
                    keycontrol.inputkey("z", pg)
            if event.type == END_MUSIC_EVENT:
                pg.mixer.music.unload()
                pg.mixer.music.load(soundsplayer.bgm_selector()[0])
                pg.mixer.music.play()

    # GUI
    # background
    background.bg(screen, bg_img)

    # MainScene
    mainscene.play(pg, screen, screensize, clock, LightFont, RegularFont, BoldFont, BigLightFont, BigRegularFont,
                   BigBoldFont, SBigRegularFont, SBigLightFont, SBigBoldFont, play_img, pause_img, stop_img,
                   next_img, prev_img, gear_img, circle_img, circlefilled_img, chat_img, glowright_img, glowleft_img,
                   maininfo_img, avatar_img, beat_img)

    pg.display.update()

pg.quit()
