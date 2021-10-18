from modules.Graphics.gui.main import bottombar, upbar, optionscreen, spectrum


def play(pg, screen, screensize, clock, lightfont, regularfont, play_img, pause_img, stop_img, next_img, prev_img,
         gear_img, audiot, audiotimecount, audiobars, analyzer, min_radius, max_radius, radius, min_decibel, max_decibel,
         bass_trigger, bass_trigger_started):
    # option screen
    spectrum.spectrum(pg, screen, screensize, audiot, audiotimecount, audiobars, analyzer, min_radius, max_radius,
                      radius, min_decibel, max_decibel, bass_trigger, bass_trigger_started)
    optionscreen.optionse(pg, screen, screensize)
    # background
    bottombar.bottomnews(pg, screen, screensize)
    bottombar.optionbtn(pg, screen, screensize, gear_img)
    bottombar.bottom(pg, screen, screensize, regularfont)
    # fps
    upbar.Fps_shower(screen, screensize, lightfont, clock)
    # playing_music
    upbar.Music_shower(pg, screen, screensize, regularfont, play_img, pause_img, stop_img, next_img, prev_img)