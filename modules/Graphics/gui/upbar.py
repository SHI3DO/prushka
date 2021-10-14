import os


def music_shower(pg, screen, screensize, Font):
    if os.path.isfile("./resources/tmp/music_playing.txt"):
        f = open("./resources/tmp/music_playing.txt", 'r')
        musictitle = Font.render(f"now plaing - {f.read()}", True, (255, 255, 255))
        screen.blit(musictitle, (screensize.current_w * 0.99 - musictitle.get_width(), screensize.current_h / 90))

        play_img = pg.image.load("./resources/textures/play.png")
        play_img = pg.transform.smoothscale(play_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(play_img, (screensize.current_w * 0.99 - musictitle.get_width() / 2,
                               screensize.current_h / 100 + screensize.current_h / 90 + musictitle.get_height()))

        pause_img = pg.image.load("./resources/textures/pause.png")
        pause_img = pg.transform.smoothscale(pause_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(pause_img, (screensize.current_w * 0.99 - musictitle.get_width() / 2 + musictitle.get_width() / 4,
                                screensize.current_h / 100 + screensize.current_h / 90 + musictitle.get_height()))

        stop_img = pg.image.load("./resources/textures/stop.png")
        stop_img = pg.transform.smoothscale(stop_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(stop_img, (screensize.current_w * 0.99 - musictitle.get_width() / 2 - musictitle.get_width() / 4,
                                screensize.current_h / 100 + screensize.current_h / 90 + musictitle.get_height()))


def fps_shower(screen, screensize, Font, clock):
    fps = Font.render(f"{round(clock.get_fps())}", True, (0, 255, 0))
    screen.blit(fps, (screensize.current_w / 128, screensize.current_h / 90))


def Optionscreenopener(pg, screen, screensize):
    OptionScreenopener = pg.Surface((screensize.current_w * 0.025, screensize.current_h))
    OptionScreenopener.set_alpha(30)
    OptionScreenopener.fill((255, 255, 255))
    screen.blit(OptionScreenopener, (screensize.current_w * 0.975, 0))
