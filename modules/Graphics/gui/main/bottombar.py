from modules.Graphics.gui.main import footer


def bottom(pg, screen, screensize, font):
    footer.shi3do(screen, screensize, font)


def bottomnews(pg, screen, screensize):
    Bottomlight = pg.Surface((screensize.current_w, screensize.current_h / 3))
    Bottomlight.set_alpha(100)
    Bottomlight.fill((0, 0, 0))
    screen.blit(Bottomlight, (0, screensize.current_h * 4 / 5))


def optionbtn(pg, screen, screensize, gear_img):
    gear_img = pg.transform.smoothscale(gear_img, (screensize.current_h / 30, screensize.current_h / 30))
    screen.blit(gear_img, (screensize.current_w * 0.97, screensize.current_h * 19 / 20))
