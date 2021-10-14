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

    if play_btn.collidepoint(lmb.pos):
        pg.mixer.music.unpause()

    if pause_btn.collidepoint(lmb.pos):
        pg.mixer.music.pause()
