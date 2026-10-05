import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("merry christmas please don't call")

# Fonts
font = pygame.font.SysFont("perpetua", 40)
title_font = pygame.font.SysFont("perpetua", 60)

# Lyrics
lyrics = [
    (0.0, "But you should know that I died slow"),
    (5, "Running through the halls of your haunted home"),
    (9.5,"And the toughest part is that we both know"),
    (13,"What happened to you"),
    (15,"Why you're out on your own"),
    (18,"Merry Christmas..."),
    (19.8,"PLEASE"),
    (20.6,"DON'T"),
    (21.4,"CALL"),
    (22,"@jaspaooo")
]

# Snowflakes
snowflakes = []

for i in range(15):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.randint(1, 1)
    snowflakes.append([x, y, speed])

# Title screen
show_title = True
title_start = pygame.time.get_ticks()

# Lyrics timer
current_line = 0
start_time = None

# Background flicker
last_flicker = pygame.time.get_ticks()
background = (255, 0, 0)

running = True

while running:
    now = pygame.time.get_ticks()

    # -------------------------
    # TITLE SCREEN
    # -------------------------
    if show_title:

        screen.fill((120, 0, 0))

        title1 = title_font.render(
            "Merry Christmas,",
            True,
            (255, 255, 255)
        )

        title2 = title_font.render(
            "Please Don't Call",
            True,
            (255, 255, 255)
        )

        title1_rect = title1.get_rect(
            center=(WIDTH // 1.95, HEIGHT // 2 - 35)
        )

        title2_rect = title2.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 35)
        )

        screen.blit(title1, title1_rect)
        screen.blit(title2, title2_rect)

        # Wait 3 seconds
        if now - title_start > 3000:
            show_title = False
            start_time = pygame.time.get_ticks()

    # -------------------------
    # LYRICS
    # -------------------------
    else:

        # Flickering red background
        if now - last_flicker > 100:
            red = random.randint(120, 190)
            background = (red, 0, 0)
            last_flicker = now

        screen.fill(background)

        # Calculate lyric time
        elapsed_time = (now - start_time) / 1000

        for i in range(len(lyrics)):
            if elapsed_time >= lyrics[i][0]:
                current_line = i

        lyric_text = lyrics[current_line][1]

        text = font.render(
            lyric_text,
            True,
            (255, 255, 255)
        )

        text_rect = text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(text, text_rect)

    # -------------------------
    # SNOWFLAKES
    # -------------------------

    for snowflake in snowflakes:
        snowflake[1] += snowflake[2]

        if snowflake[1] > HEIGHT:
            snowflake[0] = random.randint(0, WIDTH)
            snowflake[1] = 0

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (snowflake[0], snowflake[1]),
            2
        )

    # -------------------------
    # EVENTS
    # -------------------------

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
