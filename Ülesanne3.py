import pygame

# Pygame'i initialiseerimine
pygame.init()

# Ekraani seaded
laius = 640
kõrgus = 480
ekraan = pygame.display.set_mode((laius, kõrgus))
pygame.display.set_caption("Ruudustik")

# Värvid
taustavärv = [153, 255, 153]
joonevärv = [255, 0, 0]

# Ruudu suurus
ruudu_suurus = 20

# Arvutame ridade ja veergude arvu ekraani suuruse ja ruudu suuruse põhjal
tulbad = laius // ruudu_suurus
read = kõrgus // ruudu_suurus

# Funktsioon ruudustiku joonistamiseks
def ruudustik(pind, ruut, ridade_arv, tulpade_arv, joon):
    for rida in range(ridade_arv):
        for tulp in range(tulpade_arv):
            x = tulp * ruut
            y = rida * ruut
            pygame.draw.rect(pind, joon, (x, y, ruut, ruut), 1)

# Täidame tausta värviga
ekraan.fill(taustavärv)

# Kutsume funktsiooni ruudustiku joonistamiseks
ruudustik(ekraan, ruudu_suurus, read, tulbad, joonevärv)

# Värskendame ekraani
pygame.display.update()

# Mängu põhitsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()