import os


def Music_shower(pg, screen, screensize, font, play_img, pause_img, stop_img, next_img, prev_img):
    if os.path.isfile("./resources/tmp/music_playing.txt"):
        f = open("./resources/tmp/music_playing.txt", 'r')
        musictitle = font.render(f"now playing - {f.read()}", True, (255, 255, 255))
        f.close()
        screen.blit(musictitle, (screensize.current_w * 0.99 - musictitle.get_width(), screensize.current_h / 90))

        prev_img = pg.transform.smoothscale(prev_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(prev_img, (screensize.current_w * 0.85, screensize.current_h / 20))

        play_img = pg.transform.smoothscale(play_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(play_img, (screensize.current_w * 0.88, screensize.current_h / 20))

        pause_img = pg.transform.smoothscale(pause_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(pause_img, (screensize.current_w * 0.91, screensize.current_h / 20))

        stop_img = pg.transform.smoothscale(stop_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(stop_img, (screensize.current_w * 0.94, screensize.current_h / 20))

        next_img = pg.transform.smoothscale(next_img, (screensize.current_h / 40, screensize.current_h / 40))
        screen.blit(next_img, (screensize.current_w * 0.97, screensize.current_h / 20))


def Fps_shower(screen, screensize, font, clock):
    fps = font.render(f"{round(clock.get_fps())}", True, (255, 255, 255))
    screen.blit(fps, (screensize.current_w / 128, screensize.current_h / 90))


def upg(pg, screen, screensize):
    upbar = pg.Surface((screensize.current_w, screensize.current_h / 8))
    upbar.set_alpha(100)
    upbar.fill((0, 0, 0))
    screen.blit(upbar, (0, 0))


def playerpfp(screen, screensize, avatar, font):
    screen.blit(avatar, (0, 0))
    name = font.render(f"STR바보STR바보STR바보STR바보STR바보STR바보STR바보STR바보", True, (255, 255, 255))
    screen.blit(name, (avatar.get_width() + screensize.current_w / 100, screensize.current_h / 90))

