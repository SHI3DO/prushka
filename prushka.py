import pygame as pg
from modules.Sounds import soundsplayer
from pygame.locals import *
from modules.Presence.RPC import discordrpc
from modules.Control import clickhandler
from modules.Graphics.gui import background
from modules.Graphics.gui import mainscene
from modules.Sounds.audioanalyzer import *

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

f = open("./resources/tmp/options_screen.txt", 'w', encoding='UTF-8')
f.write("0")
f.close()


audiot = pg.time.get_ticks()
audiotimecount = 0
audiobars = []
audiotmp_bars = []
min_radius = 100
max_radius = 150
min_decibel = -80
max_decibel = 80
radius = min_radius
bass_trigger = -30
bass_trigger_started = 0
bass = {"start": 50, "stop": 100, "count": 12}
heavy_area = {"start": 120, "stop": 250, "count": 40}
low_mids = {"start": 251, "stop": 2000, "count": 50}
high_mids = {"start": 2001, "stop": 6000, "count": 20}
freq_groups = [bass, heavy_area, low_mids, high_mids]

length = 0

for group in freq_groups:
    g = []
    s = group["stop"] - group["start"]
    count = group["count"]
    reminder = s%count
    step = int(s/count)
    rng = group["start"]
    for i in range(count):
        arr = None
        if reminder > 0:
            reminder -= 1
            arr = np.arange(start=rng, stop=rng + step + 2)
            rng += step + 3
        else:
            arr = np.arange(start=rng, stop=rng + step + 1)
            rng += step + 2
        g.append(arr)
        length += 1
    audiotmp_bars.append(g)

angle_dt = 360/length
ang = 0
for g in audiotmp_bars:
    gr = []
    for c in g:
        gr.append(
            RotatedAverageAudioBar(int(screensize.current_w)+radius*math.cos(math.radians(ang - 90)),
                                   int(screensize.current_h)+radius*math.sin(math.radians(ang - 90)),
                                   c, (255, 0, 255), angle=ang, width=8, max_height=370))
        ang += angle_dt


analyzer = AudioAnalyzer()


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
gear_img = pg.image.load("./resources/textures/gear.png").convert_alpha()

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
                    clickhandler.LMB(event, screen, screensize, pg)
            if event.type == END_MUSIC_EVENT:
                bgm_play()

    # GUI
    # background
    background.bg(screen, bg_img)

    # MainScene
    mainscene.play(pg, screen, screensize, clock, LightFont, RegularFont, play_img, pause_img, stop_img, next_img,
                   prev_img, gear_img, audiot, audiotimecount, audiobars, analyzer, min_radius, max_radius, radius,
                   min_decibel, max_decibel, bass_trigger, bass_trigger_started)

    dt = clock.tick(120)
    pg.display.update()

pg.quit()
