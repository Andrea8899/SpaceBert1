import pygame

class Razzo:
    def __init__(self,rocket= pygame.image.load("Immagini/FalconHeavyMini.png"),fumi=[]):
        self.rocket = rocket 
        self.fumi = fumi
        
    def getFumo(self,index):
        return self.fumi[index]