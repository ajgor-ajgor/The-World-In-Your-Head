import pygame
from prefabrykaty import prefabrykaty
from mapa import mapa
import random
pygame.init()
screen = pygame.display.set_mode((640, 480))
blok1 = pygame.image.load("blok1.png").convert()
blok2 = pygame.image.load("blok2.png").convert()
blok3 = pygame.image.load("blok3.png").convert()
blok4 = pygame.image.load("blok4.png").convert()
rzul = pygame.image.load("player.png").convert_alpha()
x = 5
z = 10
xs = 0
zs = 0
seed = random.randint(1, 255)
ssektora = seed + 1
sektorx = 0
sektory = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and z + sektory * 20 > 0:
        zs = zs - 1
    if key[pygame.K_DOWN] and z + sektory * 20 < 80:
        zs = zs + 1
    if key[pygame.K_LEFT] and x + sektorx * 10 > 0:
        xs = xs - 1
    if key[pygame.K_RIGHT] and x + sektorx * 10 < 50:
        xs = xs + 1
    if key[pygame.K_BACKSPACE]:
        mapa[z + sektory * 20 + 2][x + sektorx * 10] = 0
    if xs == 64:
        xs = 0
        x = x + 1
    if xs == -1:
        xs = 63
        x = x - 1
    if zs == 24:
        zs = 0
        z = z + 1
    if zs == -1:
        zs = 23
        z = z - 1
    if x == 10:
        x = 0
        sektorx = sektorx + 1
    if x == -1:
        x = 9
        sektorx = sektorx - 1
    if z == 20:
        z = 0
        sektory = sektory + 1
    if z == -1:
        z = 19
        sektory = sektory - 1
    sektora = (173 * sektorx) ^ (163 * sektory) ^ seed
    ysektor = sektora % 4
    ymapa = prefabrykaty[ysektor]
    if sektora != ssektora and mapa[sektory * 20][sektorx * 10] == 0:
        ssektora = sektora
        for m in range(20):
            for n in range(10):
                if ymapa[m][n] == 1:
                    mapa[m + sektory * 20][n + sektorx * 10] = 1
                if ymapa[m][n] == 2:
                    mapa[m + sektory * 20][n + sektorx * 10] = 2
                if ymapa[m][n] == 3:
                    mapa[m + sektory * 20][n + sektorx * 10] = 3
                if ymapa[m][n] == 4:
                    mapa[m + sektory * 20][n + sektorx * 10] = 4
    screen.fill((0, 128, 255))
    for a in range(20):
        for b in range(10):
            if mapa[a + sektory * 20][b + sektorx * 10] == 1:
                screen.blit(blok1, (b * 64, a * 24))
            if mapa[a + sektory * 20][b + sektorx * 10] == 2:
                screen.blit(blok2, (b * 64, a * 24))
            if mapa[a + sektory * 20][b + sektorx * 10] == 3:
                screen.blit(blok3, (b * 64, a * 24))
            if mapa[a + sektory * 20][b + sektorx * 10] == 4:
                screen.blit(blok4, (b * 64, a * 24))
    screen.blit(rzul, (x * 64 + xs, z * 24 + zs))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.QUIT