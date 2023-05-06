import pygame 
class Volo:
    def __init__(self,xRazzo,yRazzo=0,heightTerreno=50,razzo_vely=0,altitudine=0,velAlt=0,limitAlt1=25000,limiteAlt2=12000):
        self.xRazzo = xRazzo
        self.yRazzo = yRazzo
        self.heightTerreno = heightTerreno
        self.razzo_vely = razzo_vely
        self.altitudine = altitudine
        self.velAlt = velAlt
        self.limiteAlt1 = limitAlt1
        self.limiteAlt2 = limiteAlt2
    
    def velocità_razzi(self,razzo): # km/h
        vel = [3000]
        return vel[razzo] 

    def lancio(self,timer,schermo,razzo):
        if timer <= -5 :
        # ALTITUDINE E VELOCITA'
            if self.altitudine  < self.limiteAlt1 : # fino i 25 km il razzo aumenta velocità
                self.razzo_vely += (0.001)*((self.velocità_razzi(razzo)/100)*-1)
                self.velAlt = self.razzo_vely
                self.altitudine = (600)* (self.razzo_vely*-1) # altezza di volo del razzo dal pianeta aumeta col passare del tempo e aumento della velocità
            elif self.altitudine < self.limiteAlt2:  # fino i 120 km il razzo aumenta velocità
                if self.yRazzo < 600:
                    print(self.razzo_vely*500,self.razzo_vely)
                    if (self.razzo_vely*500*-1) > 9500: # 9500
                        self.razzo_vely -= (0.005)*((self.velocità_razzi(razzo)/100)*-1)
                        self.yRazzo = self.yRazzo + (self.razzo_vely*5-1)

                self.velAlt += (0.001)*((self.velocità_razzi(razzo)/100)*-1)
                self.altitudine = (600)* (self.velAlt*-1)

            # CAMBIO COLORE SFONDO
            # ogni 3 km cambia leggermente lo sfondo
            #schermo.aggiornaCielo(timer)
            
                    
            # SPOSTAMENTO RAZZO
            if (self.yRazzo > 200 and self.altitudine < self.limiteAlt2): # il razzo dopo un pò smette di salire
                #formula_spinta_alto = 0 * (timer * -1) - ( (g * (timer * -1)**2)/2)
                self.yRazzo += self.razzo_vely #formula_spinta_alto

            

    def altitudineRend(self):
        if self.altitudine < 1000:
            return str(round(self.altitudine,2))+ " M"

        self.altitudine = self.altitudine/1000
        return str(round(self.altitudine,2)) + " KM"

    def velocitaRend(self):
        return str(round((self.razzo_vely*500)*-1,2)) +" KM/H"
    
    

    def suonoDecollo(self,countdownSound):
        pygame.mixer.Sound.play(countdownSound)
        pygame.mixer.music.stop()

