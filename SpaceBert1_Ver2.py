import pygame
import math
import random

# inizializzazione
pygame.init()
clock = pygame.time.Clock() # orologio per i frame
running = True
#global redMainWin,greenMainWin,blueMainWin
redMainWin = 34
greenMainWin = 113
blueMainWin =179
#--------SCHERMO PRINCIPALE -------
widthMainWin = 500
heightMainWin = 800
#immagini
razzo = pygame.image.load("Immagini/FalconHeavyMini.png")
fumo_Fase1 = pygame.image.load("Immagini/Fumo_Razzo_Stadio1.png")
fumo_Fase3 = pygame.image.load("Immagini/Fumo_Razzo_Stadio3.png")
fumo_Fase4 = pygame.image.load("Immagini/Fumo_Razzo_Stadio4.png")
# SUONI
countdownSound = pygame.mixer.Sound("Suoni/countdown.mp3")
voloSpazialeSound = pygame.mixer.Sound("Suoni/voloSpaziale.mp3")
#FONT
FONT = pygame.font.SysFont('Comic Sans MS', 35, bold = True)
FONT_MIN = pygame.font.SysFont('Comic Sans MS', 25, bold = True)
# TIMER
TIMERSHOT = pygame.event.custom_type()
pygame.time.set_timer(TIMERSHOT, 1000, 1000)


def convertTime(secNeg):
    if secNeg < 0:
        sec = secNeg * -1 # converto i numeri negativi in positivi
        time = "00:00:"
    else:
        sec = secNeg
        time = "-00:00:"
    if sec < 60:
        if sec < 10:
            time = time + "0"+ str(sec) 
        else:
            time = time + str(sec) 
    elif sec == 60:
        time = "00:01:00"
    else:
        secondi = sec % 60
        secondiStr = str(secondi)
        if secondi < 10:
            secondiStr = "0"+secondiStr
        minuti = sec // 60
        minutiStr = str(minuti)
        if minuti < 10:
            minutiStr = "0"+minutiStr
        ora = sec // 3600
        oraStr = str(ora)
        if ora < 10 :
            oraStr = "0"+ oraStr
        time = oraStr+":"+minutiStr+":"+secondiStr
        
    return time


def altitudineRend(altezza):
    if altezza < 1000:
        return str(round(altezza,2))+ " M"

    altezza = altezza/1000
    return str(round(altezza,2)) + " KM"

def velocitaRend(velocita):
    return str(round((velocita)*-1,2)) +" KM/H"


#-------------------------------------- PROGRAMMA -----------------------------------
# 0 = Falcon Heavy

def altezze_razzi_reali(razzo = 0): # espressi in m
    raz = [70]
    return raz[razzo]

def proporzione_pixel(raz = 0):
    return  razzo.get_height() / altezze_razzi_reali(raz)# è la proporzione di un pixel

def accelerazione_gravitazionale(pianeta = 0,razzo = 0): # 0 = Terra, 1 = Luna
    acc = [9.81,1.62]
    return acc[pianeta]/proporzione_pixel(razzo)

def masse_razzi_reali(razzo = 0): # espressi in kg
    mas = [1420788]
    return mas[razzo]

def velocità_razzi(razzo = 0): # km/h
    vel = [3000]
    return vel[0] 

def inizializza():
    #--- COSTANTI
    global g 
    g= accelerazione_gravitazionale(0,0) 

    #----------------RAZZO--------------------
    global timer,xRazzo,yRazzo,heightTerreno,razzo_vely,altitudine,velAlt,redMainWin,greenMainWin,blueMainWin
    # inizio sarà a terra il razzo
    heightTerreno = 50 # altezza del terreno in basso dove si appoggia il razzo
    timer = 10 # 60 secondi
    xRazzo = (widthMainWin/2) - (razzo.get_width()/2) # posiziono il razzo al centro verticalmente
    yRazzo = heightMainWin - heightTerreno-razzo.get_height()
    razzo_vely = 0 # all'inizio la velocità sarà a zero
    altitudine = 0 # altezza del razzo dal pianeta
    velAlt = 0
    redMainWin = 34
    greenMainWin = 113
    blueMainWin =179

    #------ COUNTDOWN SOUND
    pygame.mixer.Sound.play(countdownSound)
    pygame.mixer.music.stop()


inizializza()



def disegna():
    mainWindow.blit(razzo,(xRazzo,yRazzo))# disegna razzo
    # TIME
    timer_render = FONT.render(convertTime(timer),1,(255,255,255))
    centroSchermoWidth = (widthMainWin/2) - (timer_render.get_width()/2)
    yTimer = 50
    mainWindow.blit(timer_render,(centroSchermoWidth,yTimer))
    
    # VELOCITA'
    velocita_render = FONT_MIN.render(velocitaRend(razzo_vely*500),1,(255,255,255))
    xVel = widthMainWin - (widthMainWin/ 3)
    yVel = (heightMainWin) - (velocita_render.get_height()*3)  
    mainWindow.blit(velocita_render,(xVel,yVel))
    # ALTITUDINE
    altitudine_render = FONT_MIN.render(altitudineRend(altitudine),1,(255,255,255))
    xAltid = widthMainWin - (widthMainWin/ 3)
    yAltid = (heightMainWin) - (altitudine_render.get_height()*5)
    mainWindow.blit(altitudine_render,(xAltid,yAltid))

def aggiornaCielo():#redMainWin,greenMainWin,blueMainWin):
    if (timer%10 ) == 0:
            redMainWin = redMainWin -10
            if (greenMainWin > 20) :
                greenMainWin -= 10
            if (blueMainWin < 255):
                blueMainWin += 10
            print(redMainWin,greenMainWin,blueMainWin)
            mainWindow.fill((redMainWin,greenMainWin,blueMainWin))
            pygame.display.update()


while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMERSHOT:
            # countdown
            timer -= 1
    
    #--------SCHERMO PRINCIPALE -------
    widthMainWin = 500
    heightMainWin = 800
    mainWindow = pygame.display.set_mode((widthMainWin,heightMainWin))
    mainWindow.fill((redMainWin,greenMainWin,blueMainWin))
    

    # ------------------ PROGRAMMA ------------------
    #--- FUNZIONE LANCIO ---
    disegna()
    # vola
    #razzo_vely = 0 - g * (timer * -1) # v0 - gt
    if timer <= -5 :
        # ALTITUDINE E VELOCITA'
        limiteAlt_1 = 25000 #m # 25000
        limiteAlt_2 = 120000 # m 
        if altitudine  < limiteAlt_1 : # fino i 25 km il razzo aumenta velocità
            razzo_vely += (0.001)*((velocità_razzi(0)/100)*-1)
            velAlt = razzo_vely
            altitudine = (600)* (razzo_vely*-1) # altezza di volo del razzo dal pianeta aumeta col passare del tempo e aumento della velocità
        elif altitudine < limiteAlt_2:  # fino i 120 km il razzo aumenta velocità
            if yRazzo < 600:
                print(razzo_vely*500,razzo_vely)
                if (razzo_vely*500*-1) > 9500: # 9500
                    razzo_vely -= (0.005)*((velocità_razzi(0)/100)*-1)
                    yRazzo = yRazzo + (razzo_vely*5-1)

            velAlt += (0.001)*((velocità_razzi(0)/100)*-1)
            altitudine = (600)* (velAlt*-1)

        # CAMBIO COLORE SFONDO
        # ogni 3 km cambia leggermente lo sfondo
        
        #print(timer%10)
        aggiornaCielo()#redMainWin,greenMainWin,blueMainWin)
        
                
        # SPOSTAMENTO RAZZO
        if (yRazzo > 200 and altitudine < limiteAlt_2): # il razzo dopo un pò smette di salire
            #formula_spinta_alto = 0 * (timer * -1) - ( (g * (timer * -1)**2)/2)
            yRazzo += razzo_vely #formula_spinta_alto
    #------ VOLO SOUND
    if timer < -42:
        pygame.mixer.Sound.play(voloSpazialeSound)
        pygame.mixer.music.stop()



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 50








pygame.quit()








