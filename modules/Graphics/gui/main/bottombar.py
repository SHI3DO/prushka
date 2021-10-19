def bottomnews(pg, screen, screensize, glowdown_img):
    Bottomlight = pg.Surface((screensize.current_w, screensize.current_h / 3))
    Bottomlight.set_alpha(100)
    Bottomlight.fill((0, 0, 0))
    screen.blit(Bottomlight, (0, screensize.current_h * 4 / 5))

    glowdown_img.set_alpha(100)
    screen.blit(glowdown_img, (0, screensize.current_h * 4 / 5))


def optionbtn(pg, screen, screensize, gear_img):
    gear_img = pg.transform.smoothscale(gear_img, (screensize.current_h / 30, screensize.current_h / 30))
    screen.blit(gear_img, (screensize.current_w * 0.97, screensize.current_h * 19 / 20))


def chatbtn(pg, screen, screensize, chat_img):
    chat_img = pg.transform.smoothscale(chat_img, (screensize.current_h / 30, screensize.current_h / 30))
    screen.blit(chat_img, (screensize.current_w * 0.94, screensize.current_h * 19 / 20))


def bottomlight(screen, screensize, glowdown_img):
    glowdown_img.set_alpha(10)
    screen.blit(glowdown_img, (0, screensize.current_h * 4 / 5))

