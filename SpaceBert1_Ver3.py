import pygame
import math
import random
import schermo
import volo
import mytimer
import razzo

# inizializzazione
pygame.init()
clock = pygame.time.Clock() # orologio per i frame
running = True

#--------SCHERMO PRINCIPALE -------
#immagini
myRocket = pygame.image.load("Immagini/FalconHeavyMini.png")
fumo_Fase1 = pygame.image.load("Immagini/Fumo_Razzo_Stadio1.png")
fumo_Fase3 = pygame.image.load("Immagini/Fumo_Razzo_Stadio3.png")
fumo_Fase4 = pygame.image.load("Immagini/Fumo_Razzo_Stadio4.png")
fumi = [fumo_Fase1,fumo_Fase3,fumo_Fase4]
# SUONI
countdownSound = pygame.mixer.Sound("Suoni/countdown.mp3")
#voloSpazialeSound = pygame.mixer.Sound("Suoni/voloSpaziale.mp3")
voloSpazialeSound = pygame.mixer.Sound("Suoni/countdown_parte2.mp3")
voloSpazialeFineSound = pygame.mixer.Sound("Suoni/countdown_parte_finale.mp3")
#FONT
FONT = pygame.font.SysFont('Comic Sans MS', 35, bold = True)
FONT_MIN = pygame.font.SysFont('Comic Sans MS', 25, bold = True)
# TIMER
TIMERSHOT = pygame.event.custom_type()
pygame.time.set_timer(TIMERSHOT, 1000, 1000)



#-----CREAZIONE OGGETTI DELLE CLASSI PRINCIPALI
def inizializza():
    global mainWindow,myRazzo,myVolo,myTimer
    mainWindow = schermo.Schermo()
    myRazzo = razzo.Razzo(myRocket,fumi)
    widthMainWin = mainWindow.width
    heightMainWin = mainWindow.height
    xRazzo = (widthMainWin/2) - (myRazzo.rocket.get_width()/2) # posiziono il razzo al centro verticalmente
    myVolo = volo.Volo(xRazzo)
    myVolo.yRazzo = heightMainWin - myVolo.heightTerreno - myRazzo.rocket.get_height()
    myTimer = mytimer.Timer()
    myVolo.suonoDecollo(countdownSound)

inizializza()

def disegna():
    mainWindow.aggiornaCielo(myTimer.value)
    widthMainWin = mainWindow.width
    heightMainWin = mainWindow.height

    mainWindow.schermo.blit(myRazzo.rocket,(myVolo.xRazzo,myVolo.yRazzo))# disegna razzo
    # TIME
    timer_render = FONT.render(myTimer.convertToString(),1,(255,255,255))
    centroSchermoWidth = (widthMainWin/2) - (timer_render.get_width()/2)
    yTimer = 50
    mainWindow.schermo.blit(timer_render,(centroSchermoWidth,yTimer))
    
    # VELOCITA'
    velocita_render = FONT_MIN.render(myVolo.velocitaRend(),1,(255,255,255))
    xVel = widthMainWin - (widthMainWin/ 3)
    yVel = (heightMainWin) - (velocita_render.get_height()*3)  
    mainWindow.schermo.blit(velocita_render,(xVel,yVel))
    # ALTITUDINE
    altitudine_render = FONT_MIN.render(myVolo.altitudineRend(),1,(255,255,255))
    xAltid = widthMainWin - (widthMainWin/ 3)
    yAltid = (heightMainWin) - (altitudine_render.get_height()*5)
    mainWindow.schermo.blit(altitudine_render,(xAltid,yAltid))


while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMERSHOT:
            # countdown
            myTimer.countdown()
            mainWindow.aggiornaCieloVolo(myTimer.value)
            myTimer.suonoVolo(voloSpazialeSound)
            myTimer.suonoVoloFine(voloSpazialeFineSound)
    disegna()
    
    
    
    myVolo.lancio(myTimer.value,mainWindow,0)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 50








pygame.quit()








