def bottomnews(pg, screen, screensize, maininfo_img):
    Bottomlight = pg.Surface((screensize.current_w, screensize.current_h / 3))
    Bottomlight.set_alpha(100)
    Bottomlight.fill((0, 0, 0))
    screen.blit(Bottomlight, (0, screensize.current_h * 4 / 5))

    maininfo_img = pg.transform.smoothscale(maininfo_img, (screensize.current_w / 2, screensize.current_h / 6))
    screen.blit(maininfo_img, ((screensize.current_w - maininfo_img.get_width()) / 2,
                               screensize.current_h - maininfo_img.get_height() * 1.1))


def optionbtn(pg, screen, screensize, gear_img):
    gear_img = pg.transform.smoothscale(gear_img, (screensize.current_h / 30, screensize.current_h / 30))
    screen.blit(gear_img, (screensize.current_w * 0.97, screensize.current_h * 19 / 20))


def chatbtn(pg, screen, screensize, chat_img):
    chat_img = pg.transform.smoothscale(chat_img, (screensize.current_h / 30, screensize.current_h / 30))
    screen.blit(chat_img, (screensize.current_w * 0.94, screensize.current_h * 19 / 20))


def Fps_shower(screen, screensize, font, clock):
    fps = font.render(f"{round(clock.get_fps())} fps", True, (255, 255, 255))
    screen.blit(fps, (screensize.current_w / 90, screensize.current_h * 83 / 90))
