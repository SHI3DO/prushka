def optionse(pg, screen, screensize, font, boldfont, circle_img, circlefilled_img):
    f = open("./resources/tmp/options_screen.txt", 'r', encoding='UTF-8')
    if f.read() == "1":
        optionscreen = pg.Surface((screensize.current_w / 2, screensize.current_h))
        optionscreen.set_alpha(100)
        optionscreen.fill((0, 0, 0))
        screen.blit(optionscreen, (screensize.current_w * 2 / 3, 0))

        discord_rpc_option = boldfont.render(f"Discord RPC", True, (255, 255, 255))
        discord_rpc_option_desc = font.render(f"Discord Rich Presence", True, (255, 255, 255))
        screen.blit(discord_rpc_option, (screensize.current_w * 2 / 3 + screensize.current_w * 1 / 80,
                                         screensize.current_h / 7))
        screen.blit(discord_rpc_option_desc, (screensize.current_w * 2 / 3 + screensize.current_w * 1 / 80,
                                              screensize.current_h / 7 + discord_rpc_option.get_height()))

        f = open("./resources/tmp/options_discordrpc.txt", 'r', encoding='UTF-8')
        if f.read() == "0":
            f.close()
            circle_img = pg.transform.smoothscale(circle_img, (screensize.current_h / 20, screensize.current_h / 20))
            screen.blit(circle_img, (screensize.current_w * 23 / 24, screensize.current_h / 7))
        else:
            f.close()
            circlefilled_img = pg.transform.smoothscale(circlefilled_img, (screensize.current_h / 20,
                                                                           screensize.current_h / 20))
            screen.blit(circlefilled_img, (screensize.current_w * 23 / 24, screensize.current_h / 7))
