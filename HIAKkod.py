from pynput.keyboard import Key, Controller
import subprocess
import time
import tkinter as tk

root = tk.Tk()
keyboard = Controller()

z_start_entry = tk.Entry(root,bg='black',fg='white')
z_slut_entry = tk.Entry(root,bg='black',fg='white')
z_steg_entry = tk.Entry(root,bg='black',fg='white')

#Man måste manuellt gå in i cadnaA och kolla vid vilken nivå man först får röda pixlar på, och vilken nivå man sist får dem. 
# Detta bestämmer hur många gånger loopen skall iterera.

z_start = input('Vilken z-nivå är den lägsta som har pixlar som uppfyller Lp≥50 dB?') 
z_slut = input('Vilken z-nivå är den högsta som har pixlar som uppfyller Lp≥50 dB?')
steg = input('Vad ska steglängden för dz vara?')

subprocess.call(['C:\\Program (x86)\\Datakustik\\CadnaA23\\cna32.exe']) #Filvägen till cadnaA programmet, hittas genom att högerklicka cadnaA på skrivbordet och klicka "Öppna filsökväg" i menyn.

keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.down)
keyboard.release(Key.down)
keyboard.press(Key.enter)
keyboard.release(Key.enter) #öppnar 'Open' i file menyn där man väljer vilken cadnaA fil man vill använda, måste väljas manuellt.

raknare = 1 #Räknar antalet kalkulerade grids man exporterar

for nuverande_dz in range(z_start, steg ,(z_slut+1)):
    
    #Navigera till grid properties
    keyboard.press(Key.tab)
    keyboard.press(Key.right)
    keyboard.press(Key.right)
    keyboard.press(Key.right)
    keyboard.press(Key.right)
    keyboard.press(Key.down)
    keyboard.press(Key.enter)

    #Ändra inuti grid properties
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.type(steg) #Sätter dx till given steglängd
    keyboard.press(Key.tab)

    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.type(steg) #Sätter dy till given steglängd
    keyboard.press(Key.tab)

    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.type(nuverande_dz) #Sätter dz till startvärdet och adderar en multipel av steglängden beroende på numret av iterationen
    keyboard.press(Key.tab)

    for i in range (0,6):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) #Navigerar till OK knappen i grid properties och klickar på den.


    for i in range (0,5):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    for i in range (0,3):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    keyboard.press(Key.enter)
    time.sleep(5) #Navigerar till och klickar på "Calc grid"

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    for i in range (0,8):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    keyboard.type('grid vid höjd ' + str(raknare)) #namnger de exporterade bitmaps

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    for i in range (0,4):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    raknare = raknare + 1



root.mainloop()