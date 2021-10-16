def LMB(lmb, screensize, pg):
    # Music Handling
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
