import random


def spectrum(pg, screen, screensize):
    for i in range(0, 96):
        h = random.randrange(10, 150)
        spbar = pg.Surface((screensize.current_w / 96, h))
        spbar.set_alpha(h)
        spbar.fill((255, 255, 255))
        screen.blit(spbar, (i*screensize.current_w / 96, screensize.current_h - h))
