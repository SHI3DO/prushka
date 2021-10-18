from modules.Graphics.gui.main import bottombar, upbar, optionscreen


def play(pg, screen, screensize, clock, lightfont, regularfont, boldfont, play_img, pause_img, stop_img, next_img, prev_img,
         gear_img, circle_img, circlefilled_img):
    # option screen
    optionscreen.optionse(pg, screen, screensize, regularfont, boldfont, circle_img, circlefilled_img)
    # background
    bottombar.bottomnews(pg, screen, screensize)
    bottombar.optionbtn(pg, screen, screensize, gear_img)
    bottombar.bottom(pg, screen, screensize, regularfont)
    # fps
    upbar.Fps_shower(screen, screensize, lightfont, clock)
    # playing_music
    upbar.Music_shower(pg, screen, screensize, regularfont, play_img, pause_img, stop_img, next_img, prev_img)