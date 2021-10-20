from modules.Graphics.gui.main import bottombar, upbar, rightbar, leftbar, footer


def play(pg, screen, screensize, clock, lightfont, regularfont, boldfont, play_img, pause_img, stop_img, next_img,
         prev_img, gear_img, circle_img, circlefilled_img, chat_img, glowright_img, glowleft_img, maininfo_img):
    # option screen
    # background
    bottombar.bottomnews(pg, screen, screensize, maininfo_img)
    upbar.upg(pg, screen, screensize)

    rightbar.optionse(pg, screen, screensize, regularfont, boldfont, circle_img, circlefilled_img)
    leftbar.chat_screen(pg, screen, screensize, regularfont, boldfont)

    bottombar.optionbtn(pg, screen, screensize, gear_img)
    bottombar.chatbtn(pg, screen, screensize, chat_img)
    footer.shi3do(screen, screensize, regularfont)

    # fps
    fpsf = open("./resources/tmp/options_fps.txt", 'r', encoding='UTF-8')
    if fpsf.read() == "1":
        upbar.Fps_shower(screen, screensize, lightfont, clock)
    # playing_music
    upbar.Music_shower(pg, screen, screensize, regularfont, play_img, pause_img, stop_img, next_img, prev_img)
    rightbar.rightlight(screen, screensize, glowright_img)
    leftbar.leftlight(screen, screensize, glowleft_img)
