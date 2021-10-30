def selection(pg, screen, screensize, font):
    beatsection = pg.Surface((screensize.current_w * 1 / 2, screensize.current_h * 1 / 9))
    beatsection.set_alpha(30)
    beatsection.fill((0, 0, 0))
    screen.blit(beatsection, (screensize.current_w - 2 * screensize.current_h * 27 / 80, screensize.current_h * 1 / 8))

    beatsectionw = pg.Surface((screensize.current_w * 1 / 2, screensize.current_h * 1 / 90))
    beatsectionw.fill((255, 255, 255))
    screen.blit(beatsectionw, (screensize.current_w - 2 * screensize.current_h * 27 / 80, screensize.current_h * 1 / 8))

    beatlt = font.render("Solo", True, (255, 255, 255))
    screen.blit(beatlt, (screensize.current_w - 2 * screensize.current_h * 27 / 80 + beatlt.get_width() / 8,
                         screensize.current_h * 1 / 8 + beatlt.get_height() / 1.2))

    multisection = pg.Surface((screensize.current_w * 1 / 2, screensize.current_h * 1 / 9))
    multisection.set_alpha(30)
    multisection.fill((0, 0, 0))
    screen.blit(multisection, (screensize.current_w - 2 * screensize.current_h * 27 / 80, screensize.current_h * 2 / 8))

    multisectionw = pg.Surface((screensize.current_w * 1 / 2, screensize.current_h * 1 / 90))
    multisectionw.fill((255, 255, 255))
    screen.blit(multisectionw,
                (screensize.current_w - 2 * screensize.current_h * 27 / 80, screensize.current_h * 2 / 8))

    multilt = font.render("Multi", True, (255, 255, 255))
    screen.blit(multilt, (screensize.current_w - 2 * screensize.current_h * 27 / 80 + beatlt.get_width() / 8,
                          screensize.current_h * 2 / 8 + beatlt.get_height() / 1.2))

    editsection = pg.Surface((screensize.current_w * 1 / 2, screensize.current_h * 1 / 9))
    editsection.set_alpha(30)
    editsection.fill((0, 0, 0))
    screen.blit(editsection, (screensize.current_w - 2 * screensize.current_h * 27 / 80, screensize.current_h * 3 / 8))

    editsectionw = pg.Surface((screensize.current_w * 1 / 2, screensize.current_h * 1 / 90))
    editsectionw.fill((255, 255, 255))
    screen.blit(editsectionw, (screensize.current_w - 2 * screensize.current_h * 27 / 80, screensize.current_h * 3 / 8))

    editlt = font.render("Edit", True, (255, 255, 255))
    screen.blit(editlt, (screensize.current_w - 2 * screensize.current_h * 27 / 80 + beatlt.get_width() / 8,
                         screensize.current_h * 3 / 8 + beatlt.get_height() / 1.2))
