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

    discordrpc_btn = pg.Rect(screensize.current_w * 23 / 24,
                             screensize.current_h / 7,
                             screensize.current_h / 20,
                             screensize.current_h / 20)

    fps_btn = pg.Rect(screensize.current_w * 23 / 24,
                      screensize.current_h * 2 / 7,
                      screensize.current_h / 20,
                      screensize.current_h / 20)

    chat_btn = pg.Rect(screensize.current_w * 0.94,
                       screensize.current_h * 19 / 20,
                       screensize.current_h / 30,
                       screensize.current_h / 30)

    if prev_btn.collidepoint(lmb.pos):
        soundsplayer.btn01(pg)
        pg.mixer.music.unload()
        f = open("./resources/runtime/music_list.txt", 'r', encoding='UTF-8')
        li = f.readlines()
        if len(li) > 0:
            f.close()
            fr = open("./resources/runtime/music_pnum.txt", 'r', encoding='UTF-8')
            frr = fr.read()
            if int(frr) > 1:
                k = int(frr) - 1
                fr.close()
                fr = open("./resources/runtime/music_pnum.txt", 'w', encoding='UTF-8')
                fr.write(str(k))
            else:
                k = len(li)
                fr.close()
                fr = open("./resources/runtime/music_pnum.txt", 'w', encoding='UTF-8')
                fr.write(str(k))

            fr = open("./resources/runtime/music_pnum.txt", 'r', encoding='UTF-8')
            k = int(fr.read())
            fr.close()
            print(k)
            soundsplayer.nowplaying(li[k-1].replace("\n", ''))
            pg.mixer.music.load(li[k-1].replace("\n", ''))
            pg.mixer.music.play()

        else:
            f.close()
            pg.mixer.music.load(soundsplayer.bgm_selector()[0])
            pg.mixer.music.play()

    if play_btn.collidepoint(lmb.pos):
        soundsplayer.btn01(pg)
        pg.mixer.music.unpause()

    if pause_btn.collidepoint(lmb.pos):
        soundsplayer.btn01(pg)
        pg.mixer.music.pause()

    if stop_btn.collidepoint(lmb.pos):
        soundsplayer.btn01(pg)
        pg.mixer.music.unload()
        f = open("./resources/runtime/music_list.txt", 'r', encoding='UTF-8')
        li = f.readlines()
        if len(li) > 0:
            print(li[len(li) - 1].replace("\n", ''))
            pg.mixer.music.load(li[len(li) - 1].replace("\n", ''))
            pg.mixer.music.play()
            pg.mixer.music.pause()
        f.close()

    if next_btn.collidepoint(lmb.pos):
        soundsplayer.btn01(pg)
        pg.mixer.music.unload()
        f = open("./resources/runtime/music_list.txt", 'r', encoding='UTF-8')
        li = f.readlines()
        if len(li) > 0:
            f.close()
            fr = open("./resources/runtime/music_pnum.txt", 'r', encoding='UTF-8')
            frr = fr.read()
            k = int(frr) + 1
            fr.close()
            fr = open("./resources/runtime/music_pnum.txt", 'w', encoding='UTF-8')
            fr.write(str(k))

            print(li[len(li) - 1].replace("\n", ''))
            pg.mixer.music.load(soundsplayer.bgm_selector()[0])
            pg.mixer.music.play()

        else:
            pg.mixer.music.load(soundsplayer.bgm_selector()[0])
            pg.mixer.music.play()
        f.close()

    if gear_btn.collidepoint(lmb.pos):
        soundsplayer.btn01(pg)
        f = open("./resources/runtime/options_screen.txt", 'r', encoding='UTF-8')
        if f.read() == "0":
            f.close()
            f = open("./resources/runtime/options_screen.txt", 'w', encoding='UTF-8')
            f.write("1")
        else:
            f.close()
            f = open("./resources/runtime/options_screen.txt", 'w', encoding='UTF-8')
            f.write("0")

        f.close()

    if discordrpc_btn.collidepoint(lmb.pos):
        f = open("./resources/runtime/options_screen.txt", 'r', encoding='UTF-8')
        if f.read() == "1":
            f.close()
            fr = open("./resources/runtime/options_discordrpc.txt", 'r', encoding='UTF-8')
            if fr.read() == "0":
                fr.close()
                fr = open("./resources/runtime/options_discordrpc.txt", 'w', encoding='UTF-8')
                fr.write("1")
            else:
                fr.close()
                fr = open("./resources/runtime/options_discordrpc.txt", 'w', encoding='UTF-8')
                fr.write("0")
            fr.close()
        else:
            f.close()

    if fps_btn.collidepoint(lmb.pos):
        f = open("./resources/runtime/options_screen.txt", 'r', encoding='UTF-8')
        if f.read() == "1":
            f.close()
            fr = open("./resources/runtime/options_fps.txt", 'r', encoding='UTF-8')
            if fr.read() == "0":
                fr.close()
                fr = open("./resources/runtime/options_fps.txt", 'w', encoding='UTF-8')
                fr.write("1")
            else:
                fr.close()
                fr = open("./resources/runtime/options_fps.txt", 'w', encoding='UTF-8')
                fr.write("0")
            fr.close()
        else:
            f.close()

    if chat_btn.collidepoint(lmb.pos):
        soundsplayer.btn01(pg)
        f = open("./resources/runtime/chat_screen.txt", 'r', encoding='UTF-8')
        if f.read() == "0":
            f.close()
            f = open("./resources/runtime/chat_screen.txt", 'w', encoding='UTF-8')
            f.write("1")
        else:
            f.close()
            f = open("./resources/runtime/chat_screen.txt", 'w', encoding='UTF-8')
            f.write("0")

        f.close()
