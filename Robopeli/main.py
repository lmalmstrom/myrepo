import pygame
import sys
from random import randint


pygame.init()
nayton_leveys = 640
nayton_korkeus = 480
naytto = pygame.display.set_mode((nayton_leveys, nayton_korkeus))

#kuvat
robo_kuva = pygame.image.load("robo.png")
kolikko_kuva = pygame.image.load("kolikko.png")
hirvio_kuva = pygame.image.load("hirvio.png")
tausta_kuva = pygame.image.load("tausta.png")
#mitat
robo_leveys = robo_kuva.get_width()
robo_korkeus = robo_kuva.get_height()
kolikko_leveys = kolikko_kuva.get_width()
kolikko_korkeus = kolikko_kuva.get_height()
hirvio_leveys = hirvio_kuva.get_width()
hirvio_korkeus = hirvio_kuva.get_height()
#kello
kello = pygame.time.Clock()
#pistelasku
pisteet_yht = 0
fontti = pygame.font.Font('freesansbold.ttf', 16)
#lopputeksti
loppu_fontti = pygame.font.Font('freesansbold.ttf', 64)
#värit
musta = (0, 0, 0)
valkoinen = (255,255,255)
kolikot = [(randint(0,640-kolikko_leveys),-100)]
hirviot = []
#liike
oikealle = False
vasemmalle = False
kolikot_nopeus = 1

#robon sijainti alussa
robo_x = 0
robo_y = 470-robo_korkeus
    #piirretään robo annetuihin koordinaatteihin
def robo(x,y):
    naytto.blit(robo_kuva, (x,y))

    #piirretään pistelaskuri vasempaan ylänurkkaan
def pisteiden_lasku(x,y):
    naytto_pisteet = fontti.render("Pisteet : " + str(pisteet_yht), True, (valkoinen))
    naytto.blit(naytto_pisteet, (x,y))

def kolari(robo_x,robo_y, kohde_x,kohde_y):
    palautus = False
    if 470 > kohde_y+kolikko_korkeus/1.8 >= robo_y:
        if robo_x < kohde_x+kolikko_leveys/2 < robo_x+robo_leveys:
            palautus = True

    return palautus

def kolikkojen_piirto_pisteet_nopeus(kolikot, robo_y, robo_x, pisteet, kolikot_nopeus):
    uudet_kolikot = []
    pisteiden_palautus = pisteet
    for kolikko in kolikot:
        #ymmärrettävät muuttujat
        kolikko_x = kolikko[0]
        kolikko_y = kolikko[1]
        #kolikko laskeutuu 
        kolikko_y += kolikot_nopeus
        #Tarkistetaan kolarin kautta, osuuko kolikko roboon. Jos osuu niin annetaan piste. Nopeutetaan kolikoita
        if kolari(robo_x,robo_y, kolikko_x,kolikko_y):
            pisteiden_palautus += 1
            if pisteiden_palautus % 4 == 0 and kolikot_nopeus < 3:
                kolikot_nopeus *= 1.3
                
            elif pisteiden_palautus == 1:
                kolikot_nopeus *= 1.3
        else:
        #luodaan kolikko palautuslistaan
            if kolikko_y+kolikko_korkeus < 480:
                uudet_kolikot.append((kolikko_x,kolikko_y))
        #piirretään kolikko
        naytto.blit(kolikko_kuva, (kolikko_x,kolikko_y))
        #palautetaan kolikkolista,pisteet ja kolikkojen nopeus
    return uudet_kolikot, pisteiden_palautus, kolikot_nopeus

def hirvioiden_piirto(hirviolista, pisteet, robo_x, robo_y):
    hirvio_palautus = []
    #testi jotta seuraava hirviö voi tulla, pitää listan olla joko tyhjä tai aiempi ruudulla
    testi = False
    #alle 3 pisteellä ei hirviöitä. Sen jälkeen uusien luonti
    if not pisteet < 3:
        #jos ei hirvioitä -> tee hirviö
        if len(hirviolista) == 0:
            hirvio_palautus.append((randint(0,640-hirvio_leveys), randint(-500,-100)))
        elif len(hirviolista) < pisteet/3 and len(hirviolista) < 10:
            hirvio_palautus.append((randint(0,640-hirvio_leveys), randint(-500,-100)))

    for hirvio in hirviolista:
        hirvio_x = hirvio[0]
        hirvio_y = hirvio[1]
        if kolari(robo_x,robo_y, hirvio_x,hirvio_y):
            peli_loppu()

        if hirvio_y < 480:
            hirvio_palautus.append((hirvio_x,hirvio_y+kolikot_nopeus))
        naytto.blit(hirvio_kuva,(hirvio_x,hirvio_y))
                    
    return hirvio_palautus

def kolikoiden_luominen(kolikot, pisteet):
    #jos ei kolikoita, tehdään uus
    if len(kolikot) < 1:
        kolikot.append((randint(0,640-kolikko_leveys),-100))
    elif len(kolikot) < pisteet and len(kolikot) < 4:
        kolikot.append((randint(0,640-kolikko_leveys),randint(-500,-100)))

    return kolikot

def peli_loppu():
    loppu_teksti = loppu_fontti.render("GAME OVER", True, (valkoinen))
    naytto.blit(loppu_teksti, (120, nayton_korkeus/2-32))
    pygame.display.flip()
    time.sleep(5)
    exit(0)


while True:  
    #Pyyhitään näyttö ja tausta
    naytto.fill(musta)
    naytto.blit(tausta_kuva, (0,0))
    #Näppäinten vahtiminen sekä suunnan muutos
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True


        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False

        if tapahtuma.type == pygame.QUIT:
            exit(0)
    #Robon liike
    if oikealle:
        if robo_x < 640-robo_leveys:
            robo_x += 3
    if vasemmalle and robo_x > 0:
        robo_x -= 3
    #kolikkojen piirtäminen ja pisteiden lasku
    kolikot, pisteet_yht, kolikot_nopeus = kolikkojen_piirto_pisteet_nopeus(kolikot, robo_y, robo_x, pisteet_yht, kolikot_nopeus)
    #kolikoiden luominen
    kolikot = kolikoiden_luominen(kolikot, pisteet_yht)

    #piirretään robo
    robo(robo_x,robo_y)
    #piiretään pisteet
    pisteiden_lasku(5,5)
    #hirvioiden piirto ja luominen
    hirviot = hirvioiden_piirto(hirviot, pisteet_yht, robo_x, robo_y)    
    #Päivitetään näyttö
    pygame.display.flip()
    #kello eteenpäin
    kello.tick(60)