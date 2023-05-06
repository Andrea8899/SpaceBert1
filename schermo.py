import pygame
class Schermo:
    def __init__(self,width=500,height=800,red = 34,green= 114,blue= 180):
        self.height = height
        self.width = width
        self.red = red
        self.green = green
        self.blue = blue
        self.schermo = pygame.display.set_mode((self.width,self.height))
        self.schermo.fill((self.red,self.green,self.blue))

    def changeColor(self, newColor):
        self.color = newColor
        self.schermo.fill(newColor)

    def aggiornaCielo(self,timer):
        self.schermo.fill((self.red,self.green,self.blue))

    def aggiornaCieloVolo(self,timer):
        if (timer%6 ) == 0  and timer < 0:
            if (self.red >= 2):
                self.red = self.red -2
            if (self.green >= 5) :
                self.green -= 7
            if (self.blue < 200 and self.red >= 2 and self.green >= 5 ):
                self.blue += 2
            elif (self.blue > 0 and self.red <= 2 and self.green <= 5  ):
                self.blue -= 20
            ''' 
            if (self.blue < 220 and self.green > 0 and self.green <= 80 and self.blue > 0 and self.red < 2):
                self.blue -= 20
                self.green -= 5
            elif (self.blue < 214 and self.red > 0 and self.green > 80 and self.blue > 0 ):
                self.blue += 2
            '''
            
            print(self.red,self.green,self.blue)
            self.changeColor((self.red,self.green,self.blue))
            pygame.display.update()
        else:
            self.schermo.fill((self.red,self.green,self.blue))
            



    