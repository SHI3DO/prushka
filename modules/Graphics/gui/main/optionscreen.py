def optionse(pg, screen, screensize):
    f = open("./resources/tmp/options_screen.txt", 'r', encoding='UTF-8')
    if f.read() == "1":
        optionscreen = pg.Surface((screensize.current_w / 2, screensize.current_h))
        optionscreen.set_alpha(100)
        optionscreen.fill((0, 0, 0))
        screen.blit(optionscreen, (screensize.current_w * 2/3, 0))

