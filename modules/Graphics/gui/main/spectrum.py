from modules.Sounds.audioanalyzer import *


def spectrum(pg, screen, screensize, gettickslastframe, timecount, bars, analyzer, min_radius, max_radius, radius,
             min_decibel, max_decibel, bass_trigger, bass_trigger_started):
    avg_bass = 0
    poly = []

    t = pg.time.get_ticks()
    deltaTime = (t - gettickslastframe) / 1000.0
    gettickslastframe = t

    timecount += deltaTime

    for b1 in bars:
        for b in b1:
            b.update_all(deltaTime, pygame.mixer.music.get_pos() / 1000.0, analyzer)

    for b in bars[0]:
        avg_bass += b.avg

    avg_bass /= len(bars[0])

    if avg_bass > bass_trigger:
        if bass_trigger_started == 0:
            bass_trigger_started = pygame.time.get_ticks()
        if (pygame.time.get_ticks() - bass_trigger_started) / 1000.0 > 2:
            bass_trigger_started = 0

        newr = min_radius + int(
            avg_bass * ((max_radius - min_radius) / (max_decibel - min_decibel)) + (max_radius - min_radius))
        radius_vel = (newr - radius) / 0.15

    elif radius > min_radius:
        bass_trigger_started = 0
        polygon_bass_color = None
        radius_vel = (min_radius - radius) / 0.15

    else:
        bass_trigger_started = 0
        poly_color = (255, 255, 255)
        polygon_bass_color = None
        polygon_color_vel = [0, 0, 0]

        radius_vel = 0
        radius = min_radius

    radius += radius_vel * deltaTime

    for b1 in bars:
        for b in b1:
            b.x, b.y = int(screensize.current_w / 2) + radius * math.cos(math.radians(b.angle - 90)), \
                       int(screensize.current_h / 2) + radius * math.sin(
                           math.radians(b.angle - 90))
            b.update_rect()

            poly.append(b.rect.points[3])
            poly.append(b.rect.points[2])

    pg.draw.polygon(screen, (0, 0, 0), poly)
    pg.draw.circle(screen, (255, 255, 255), (int(screensize.current_w / 2), int(screensize.current_h / 2)), int(radius))
