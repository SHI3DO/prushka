from modules.Sounds import soundsplayer


def LMB(lmb, screen, screensize, pg):
    # Music Handling
    prev_btn = pg.Rect(screensize.current_w * 0.85,
                       screensize.current_h / 20,
                       screensize.current_h / 40,
                       screensize.current_h / 40)

    play_btn = pg.Rect(screensize.current_w * 0.88,
                       screensize.current_h / 20,
                       screensize.current_h / 40,
                       screensize.current_h / 40)

    pause_btn = pg.Rect(screensize.current_w * 0.91,
                        screensize.current_h / 20,
                        screensize.current_h / 40,
                        screensize.current_h / 40)

    stop_btn = pg.Rect(screensize.current_w * 0.94,
                       screensize.current_h / 20,
                       screensize.current_h / 40,
                       screensize.current_h / 40)

    next_btn = pg.Rect(screensize.current_w * 0.97,
                       screensize.current_h / 20,
                       screensize.current_h / 40,
                       screensize.current_h / 40)

    gear_btn = pg.Rect(screensize.current_w * 0.97,
                       screensize.current_h * 19 / 20,
                       screensize.current_h / 30,
                       screensize.current_h / 30)

    circle_btn = pg.Rect(screensize.current_w * 23/24,
                         screensize.current_h / 7,
                         screensize.current_h / 20,
                         screensize.current_h / 20)

    if prev_btn.collidepoint(lmb.pos):
        pg.mixer.music.unload()
        f = open("./resources/tmp/music_list.txt", 'r', encoding='UTF-8')
        li = f.readlines()
        if len(li) > 0:
            print(li[len(li) - 1].replace("\n", ''))
            pg.mixer.music.load(soundsplayer.bgm_selector()[0])
            pg.mixer.music.play()

        else:
            pg.mixer.music.load(soundsplayer.bgm_selector()[0])
            pg.mixer.music.play()
        f.close()
    if play_btn.collidepoint(lmb.pos):
        pg.mixer.music.unpause()

    if pause_btn.collidepoint(lmb.pos):
        pg.mixer.music.pause()

    if stop_btn.collidepoint(lmb.pos):
        pg.mixer.music.unload()
        f = open("./resources/tmp/music_list.txt", 'r', encoding='UTF-8')
        li = f.readlines()
        if len(li) > 0:
            print(li[len(li) - 1].replace("\n", ''))
            pg.mixer.music.load(li[len(li) - 1].replace("\n", ''))
            pg.mixer.music.play()
            pg.mixer.music.pause()
        f.close()

    if next_btn.collidepoint(lmb.pos):
        pg.mixer.music.unload()
        f = open("./resources/tmp/music_list.txt", 'r', encoding='UTF-8')
        li = f.readlines()
        if len(li) > 0:
            print(li[len(li) - 1].replace("\n", ''))
            pg.mixer.music.load(soundsplayer.bgm_selector()[0])
            pg.mixer.music.play()

        else:
            pg.mixer.music.load(soundsplayer.bgm_selector()[0])
            pg.mixer.music.play()
        f.close()

    if gear_btn.collidepoint(lmb.pos):
        f = open("./resources/tmp/options_screen.txt", 'r', encoding='UTF-8')
        if f.read() == "0":
            f.close()
            f = open("./resources/tmp/options_screen.txt", 'w', encoding='UTF-8')
            f.write("1")
        else:
            f.close()
            f = open("./resources/tmp/options_screen.txt", 'w', encoding='UTF-8')
            f.write("0")

        f.close()

    if circle_btn.collidepoint(lmb.pos):
        f = open("./resources/tmp/options_screen.txt", 'r', encoding='UTF-8')
        if f.read() == "1":
            f.close()
            fr = open("./resources/tmp/options_discordrpc.txt", 'r', encoding='UTF-8')
            if fr.read() == "0":
                fr.close()
                fr = open("./resources/tmp/options_discordrpc.txt", 'w', encoding='UTF-8')
                fr.write("1")
            else:
                fr.close()
                fr = open("./resources/tmp/options_discordrpc.txt", 'w', encoding='UTF-8')
                fr.write("0")
            fr.close()
        else:
            f.close()
