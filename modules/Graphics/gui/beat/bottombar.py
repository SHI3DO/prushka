def bottomnews(pg, screen, screensize):
    Bottomlight = pg.Surface((screensize.current_w, screensize.current_h / 3))
    Bottomlight.set_alpha(100)
    Bottomlight.fill((0, 0, 0))
    screen.blit(Bottomlight, (0, screensize.current_h * 7 / 8))


def Fps_shower(screen, screensize, font, clock):
    fps = font.render(f"{round(clock.get_fps())} fps", True, (255, 255, 255))
    screen.blit(fps, (screensize.current_w / 90, screensize.current_h * 86 / 90))
