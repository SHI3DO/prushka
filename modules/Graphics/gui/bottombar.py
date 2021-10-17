from modules.Graphics.gui import footer


def bottom(pg, screen, screensize, font):
    footer.shi3do(screen, screensize, font)


def bottomnews(pg, screen, screensize):
    Bottomlight = pg.Surface((screensize.current_w, screensize.current_h / 6))
    Bottomlight.set_alpha(100)
    Bottomlight.fill((0, 0, 0))
    screen.blit(Bottomlight, (0, screensize.current_h * 5 / 6))
