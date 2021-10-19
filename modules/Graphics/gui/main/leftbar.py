def chat_screen(pg, screen, screensize, font, boldfont, glowleft_img):
    f = open("./resources/tmp/chat_screen.txt", 'r', encoding='UTF-8')
    if f.read() == "1":
        leftlight(screen, screensize, glowleft_img)
        chatscreen = pg.Surface((screensize.current_w * 1 / 3, screensize.current_h))
        chatscreen.set_alpha(100)
        chatscreen.fill((0, 0, 0))
        screen.blit(chatscreen, (0, 0))


def leftlight(screen, screensize, glowright_img):
    glowright_img.set_alpha(50)
    screen.blit(glowright_img, (screensize.current_w * 0, 0))
