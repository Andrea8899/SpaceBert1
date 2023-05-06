import pygame
class Timer:
    def __init__(self,value= 10):
        self.value = value

    def countdown(self):
        self.value -= 1
        return self.value
    
    def convertToString(self):
        if self.value < 0:
            sec = self.value * -1 # converto i numeri negativi in positivi
            time = "00:00:"
        else:
            sec = self.value
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
    
    def suonoVolo(self,voloSpazialeSound):
        if self.value == -40 :
            pygame.mixer.Sound.play(voloSpazialeSound)
            pygame.mixer.music.stop()

    def suonoVoloFine(self,voloSpazialeFineSound):
        if self.value == -60:
            pygame.mixer.Sound.play(voloSpazialeFineSound)
            pygame.mixer.music.stop()

