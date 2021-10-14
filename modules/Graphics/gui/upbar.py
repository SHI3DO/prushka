import os

div_n = 4


def Music_shower(pg, screen, screensize, font, play_img, pause_img, stop_img, next_img):
    if os.path.isfile("./resources/tmp/music_playing.txt"):
        f = open("./resources/tmp/music_playing.txt", 'r')
        musictitle = font.render(f"now plaing - {f.read()}", True, (255, 255, 255))
        f.close()
        screen.blit(musictitle, (screensize.current_w * 0.99 - musictitle.get_width(), screensize.current_h / 90))

        play_img = pg.transform.smoothscale(play_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(play_img, (screensize.current_w * 0.99 - musictitle.get_width() / 2 -
                               1.5*musictitle.get_width() / div_n, screensize.current_h / 100 +
                               screensize.current_h / 90 + musictitle.get_height()))

        stop_img = pg.transform.smoothscale(stop_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(stop_img, (screensize.current_w * 0.99 - musictitle.get_width() / 2 -
                               0.5*musictitle.get_width() / div_n, screensize.current_h / 100 +
                               screensize.current_h / 90 + musictitle.get_height()))

        pause_img = pg.transform.smoothscale(pause_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(pause_img, (screensize.current_w * 0.99 - musictitle.get_width() / 2 +
                                0.5*musictitle.get_width() / div_n, screensize.current_h / 100 +
                                screensize.current_h / 90 + musictitle.get_height()))

        next_img = pg.transform.smoothscale(next_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(next_img, (screensize.current_w * 0.99 - musictitle.get_width() / 2 +
                               1.5*musictitle.get_width() / div_n, screensize.current_h / 100 +
                               screensize.current_h / 90 + musictitle.get_height()))


def Fps_shower(screen, screensize, font, clock):
    fps = font.render(f"{round(clock.get_fps())}", True, (0, 255, 0))
    screen.blit(fps, (screensize.current_w / 128, screensize.current_h / 90))


def Optionscreenopener(pg, screen, screensize):
    OptionScreenopener = pg.Surface((screensize.current_w * 0.025, screensize.current_h))
    OptionScreenopener.set_alpha(30)
    OptionScreenopener.fill((255, 255, 255))
    screen.blit(OptionScreenopener, (screensize.current_w * 0.975, 0))
