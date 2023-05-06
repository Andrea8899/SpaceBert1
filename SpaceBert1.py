from tkinter import * 
from tkinter import ttk
''' ----------------------------------------- FUNZIONI --------------------------------------------'''

def center_window(width=300, height=200):
    #misure dello schermo principale
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
''' -----------------------------------------------------------------------------------------------'''


#-------- INFO SCHERMO -----------------
widthSchermo = 500
heightSchermo = 800;
root = Tk() # il main dello schermo
root.title("SpaceBert1") # titolo
center_window(widthSchermo,heightSchermo) # dimensioni dello schermo principale
root.configure(bg='#2271b3') # colore schermo
#---------------------------

#-------- FRAME PRINCIPALE -----------------
s = ttk.Style()#creo uno stile per il background
s.configure('Frame1.TFrame', background='#2271b3')# colore cielo
widthMainFrame = widthSchermo
heightMainFrame = heightSchermo
mainframe = ttk.Frame(root,style='Frame1.TFrame',relief='raised') # il fram dentro lo schermo dove andranno posizionati gli oggetti
mainframe.place(x=0, y=0, anchor="nw",width = widthMainFrame,height=heightMainFrame) 
#---------------------------

#-------- FRAME INFERIORE(INFO, TERRENO) -----------------
s = ttk.Style()#creo uno stile per il background
s.configure('Frame2.TFrame', background='#35682d')# colore prato
frameInferiore = ttk.Frame(mainframe,padding ="3 3 12 12",style='Frame2.TFrame') # il fram dentro lo schermo dove andranno posizionati gli oggetti
heigthFrameInf = 50
widthFrameInf = widthSchermo
frameInferiore.place(x=0, y=heightMainFrame-heigthFrameInf, anchor="nw",width = widthFrameInf,height = heigthFrameInf) 




root.mainloop() # mette in loop lo schermo principale

