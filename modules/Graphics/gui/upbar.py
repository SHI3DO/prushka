import os


def music_shower(screen, screensize, Font):
    if os.path.isfile("./resources/tmp/music_playing.txt"):
        f = open("./resources/tmp/music_playing.txt", 'r')
        musictitle = Font.render(f"now plaing - {f.read()}", True, (255, 255, 255))
        screen.blit(musictitle, (screensize.current_w * 0.99 - musictitle.get_width(), screensize.current_h / 90))


def fps_shower(screen, screensize, Font, clock):
    fps = Font.render(f"{round(clock.get_fps())}", True, (0, 255, 0))
    screen.blit(fps, (screensize.current_w / 128, screensize.current_h / 90))


def Optionscreenopener(pg, screen, screensize):
    OptionScreenopener = pg.Surface((screensize.current_w * 0.025, screensize.current_h))
    OptionScreenopener.set_alpha(30)
    OptionScreenopener.fill((255, 255, 255))
    screen.blit(OptionScreenopener, (screensize.current_w * 0.975, 0))
