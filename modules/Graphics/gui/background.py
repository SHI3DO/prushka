def bg(pg, screen, screensize):
    Bottomlight = pg.Surface((screensize.current_w, screensize.current_h/6))
    Bottomlight.set_alpha(10)
    Bottomlight.fill((255, 255, 255))
    screen.blit(Bottomlight, (0, screensize.current_h*5/6))
