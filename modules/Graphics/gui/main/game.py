def selection(pg, screen, screensize, beat_img, edit_img, font):
    beatsection = pg.Surface((screensize.current_h * 27 / 80, screensize.current_h * 27 / 80))
    beatsection.set_alpha(30)
    beatsection.fill((0, 0, 0))
    screen.blit(beatsection, (screensize.current_w - 2 * screensize.current_h * 27 / 80, screensize.current_h * 1 / 8))

    beat_img = pg.transform.smoothscale(beat_img, (screensize.current_h / 6, screensize.current_h / 6))
    screen.blit(beat_img, (screensize.current_w - 2 * screensize.current_h * 27 / 80 +
                           (screensize.current_h * 27 / 80 - beat_img.get_width()) / 2,
                           screensize.current_h * 1 / 8 +
                           (screensize.current_h * 27 / 80 - beat_img.get_height()) / 2 - screensize.current_h / 20))

    beatlt = font.render("Solo", True, (255, 255, 255))
    screen.blit(beatlt, (screensize.current_w - 2 * screensize.current_h * 27 / 80 +
                         (screensize.current_h * 27 / 80 - beatlt.get_width()) / 2, screensize.current_h * 1 / 8 +
                         (screensize.current_h * 27 / 80 - beatlt.get_height()) / 2 + screensize.current_h / 12))

    editsection = pg.Surface((screensize.current_h * 27 / 80, screensize.current_h * 27 / 80))
    editsection.set_alpha(30)
    editsection.fill((0, 0, 0))
    screen.blit(editsection, (screensize.current_w - screensize.current_h * 27 / 80, screensize.current_h * 1 / 8))

    edit_img = pg.transform.smoothscale(edit_img, (screensize.current_h / 6, screensize.current_h / 6))
    screen.blit(edit_img, (screensize.current_w - screensize.current_h * 27 / 80 +
                           (screensize.current_h * 27 / 80 - beat_img.get_width()) / 2,
                           screensize.current_h * 1 / 8 +
                           (screensize.current_h * 27 / 80 - beat_img.get_height()) / 2 - screensize.current_h / 20))

    editlt = font.render("Edit", True, (255, 255, 255))
    screen.blit(editlt, (screensize.current_w - screensize.current_h * 27 / 80 +
                         (screensize.current_h * 27 / 80 - beatlt.get_width()) / 2, screensize.current_h * 1 / 8 +
                         (screensize.current_h * 27 / 80 - beatlt.get_height()) / 2 + screensize.current_h / 12))

    multisection = pg.Surface((screensize.current_h * 27 / 80, screensize.current_h * 27 / 80))
    multisection.set_alpha(30)
    multisection.fill((0, 0, 0))
    screen.blit(multisection, (screensize.current_w - 2 * screensize.current_h * 27 / 80, screensize.current_h * 1 / 8 +
                               screensize.current_h * 27 / 80))

    multi_img = pg.transform.smoothscale(beat_img, (screensize.current_h / 6, screensize.current_h / 6))
    screen.blit(multi_img, (screensize.current_w - 2 * screensize.current_h * 27 / 80 +
                            (screensize.current_h * 27 / 80 - beat_img.get_width()) / 2,
                            screensize.current_h * 1 / 8 + screensize.current_h * 27 / 80 +
                            (screensize.current_h * 27 / 80 - beat_img.get_height()) / 2 - screensize.current_h / 20))

    multilt = font.render("Multi", True, (255, 255, 255))
    screen.blit(multilt, (screensize.current_w - 2 * screensize.current_h * 27 / 80 +
                          (screensize.current_h * 27 / 80 - beatlt.get_width()) / 2, screensize.current_h * 1 / 8 +
                          screensize.current_h * 27 / 80 +
                          (screensize.current_h * 27 / 80 - beatlt.get_height()) / 2 + screensize.current_h / 12))

    whatsection = pg.Surface((screensize.current_h * 27 / 80, screensize.current_h * 27 / 80))
    whatsection.set_alpha(30)
    whatsection.fill((0, 0, 0))
    screen.blit(whatsection, (screensize.current_w - screensize.current_h * 27 / 80, screensize.current_h * 1 / 8 +
                              screensize.current_h * 27 / 80))

    what_img = pg.transform.smoothscale(edit_img, (screensize.current_h / 6, screensize.current_h / 6))
    screen.blit(what_img, (screensize.current_w - screensize.current_h * 27 / 80 +
                           (screensize.current_h * 27 / 80 - beat_img.get_width()) / 2,
                           screensize.current_h * 1 / 8 + screensize.current_h * 27 / 80 +
                           (screensize.current_h * 27 / 80 - beat_img.get_height()) / 2 - screensize.current_h / 20))

    whatlt = font.render("What", True, (255, 255, 255))
    screen.blit(whatlt, (screensize.current_w - screensize.current_h * 27 / 80 +
                         (screensize.current_h * 27 / 80 - beatlt.get_width()) / 2, screensize.current_h * 1 / 8 +
                         screensize.current_h * 27 / 80 +
                         (screensize.current_h * 27 / 80 - beatlt.get_height()) / 2 + screensize.current_h / 12))
