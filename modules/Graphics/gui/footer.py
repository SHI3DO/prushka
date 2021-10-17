def shi3do(screen, screensize, font):
    dev = font.render(f"shi3do", True, (255, 255, 255))
    screen.blit(dev, (screensize.current_w / 90, screensize.current_h * 43 / 45))
