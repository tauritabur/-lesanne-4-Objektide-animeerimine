import pygame
import random

# Pygame'i initsialiseerimine
pygame.init()

# Mänguakna suurus
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autode animatsioon")

# Piltide laadimine
bg = pygame.image.load("bg_rally.jpg")
f1_red = pygame.image.load("f1_red.png")
f1_blue = pygame.image.load("f1_blue.png")

# Auto mõõtmed
RED_CAR_WIDTH, RED_CAR_HEIGHT = f1_red.get_width(), f1_red.get_height()
BLUE_CAR_WIDTH, BLUE_CAR_HEIGHT = f1_blue.get_width(), f1_blue.get_height()

# Punase auto algpositsioon
red_x = WIDTH // 2 - RED_CAR_WIDTH // 2
red_y = HEIGHT - RED_CAR_HEIGHT - 10
red_speed = 5

# Siniste autode parameetrid
blue_cars = []
for _ in range(3):  # Kolm sinist autot
    blue_x = random.randint(100, WIDTH - 100 - BLUE_CAR_WIDTH)
    blue_y = random.randint(-HEIGHT, -BLUE_CAR_HEIGHT)
    blue_cars.append([blue_x, blue_y])

blue_speed = 5

# Punktisüsteem
score = 0
font = pygame.font.Font(None, 36)


def reset_game():
    global red_x, score, blue_cars
    red_x = WIDTH // 2 - RED_CAR_WIDTH // 2
    score = 0
    blue_cars = [[random.randint(100, WIDTH - 100 - BLUE_CAR_WIDTH), random.randint(-HEIGHT, -BLUE_CAR_HEIGHT)] for _ in
                 range(3)]


# Mängutsükkel
running = True
clock = pygame.time.Clock()
while running:
    screen.blit(bg, (0, 0))
    screen.blit(f1_red, (red_x, red_y))

    # Liikumine
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and red_x > 0:
        red_x -= red_speed
    if keys[pygame.K_d] and red_x < WIDTH - RED_CAR_WIDTH:
        red_x += red_speed

    # Siniste autode liikumine ja kokkupõrke tuvastamine
    for car in blue_cars:
        car[1] += blue_speed
        if car[1] > HEIGHT:
            car[1] = random.randint(-HEIGHT, -BLUE_CAR_HEIGHT)
            car[0] = random.randint(100, WIDTH - 100 - BLUE_CAR_WIDTH)
            score += 1

        # Kokkupõrke tuvastamine
        if (red_x < car[0] + BLUE_CAR_WIDTH and red_x + RED_CAR_WIDTH > car[0] and
                red_y < car[1] + BLUE_CAR_HEIGHT and red_y + RED_CAR_HEIGHT > car[1]):
            game_over = True
            while game_over:
                screen.fill((0, 0, 0))
                text = font.render("Mäng läbi! Vajuta ENTER, et uuesti alustada", True, (255, 0, 0))
                screen.blit(text, (WIDTH // 2 - 180, HEIGHT // 2))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        game_over = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        reset_game()
                        game_over = False

        screen.blit(f1_blue, (car[0], car[1]))

    # Skoori kuvamine
    score_text = font.render("Skoor: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
