from gpiozero import LED , Button as btnZ
from tkinter import *
from tkinter import  Button as btnK
import SevenSeg
 
class AlarmSys:
    def __init__(self, z1, z2, z3, z4, on_off, reset, alarme,
                 lblz1, lblz2, lblz3, lblz4, lbl_on_off,
                 pa, pb, pc, pd, pe, pf, pg, ppd, type):
 
        # GPIO Button
        self.__z1 = btnZ(z1)
        self.__z2 = btnZ(z2)
        self.__z3 = btnZ(z3)
        self.__z4 = btnZ(z4)
        self.__reset = btnZ(reset)
        self.__on_off = btnZ(on_off)
 
        # Tikinter 
        self.__Root = Tk()
        self.__Root.title("Alarm System")
        
        #frame pour les labels tikinte
        self.frame = Frame(self.__Root,bg="gray")
        self.frame.grid(row=0, column=0, columnspan=2, rowspan=3, padx=5, pady=5)

        #frame pour les bouton tikinter
        self.frame_button = Frame(self.__Root,bg="gray")
        self.frame_button.grid(row=0, column=2, rowspan=3, padx=5, pady=5)

 
        # Tikinter label
        self.__lblz1 = Label(self.frame, text=lblz1, bg="light blue", width=4)
        self.__lblz2 = Label(self.frame, text=lblz2, bg="light blue", width=4)
        self.__lblz3 = Label(self.frame, text=lblz3, bg="light blue", width=4)
        self.__lblz4 = Label(self.frame, text=lblz4, bg="light blue", width=4)
        self.__lbl_on_off = Label(self.__Root, text=lbl_on_off, bg="light blue")
 
        # Tikinter Button
        self.__activate = btnK(self.frame_button, text="Activate", command=self.__Activate, bg="orange",width=10)
        self.__deactivate = btnK(self.frame_button, text="Deactivate", command=self.__Deactivate, bg="orange",width=10)
        self.__resetTk = btnK(self.frame_button, text="Reset", command=self.__Reset, bg="orange",width=10)
 
        # LED
        self.__alarme = LED(alarme)
 
        # 7segemts
        self.__pa = pa
        self.__pb = pb
        self.__pc = pc
        self.__pd = pd
        self.__pe = pe
        self.__pf = pf
        self.__pg = pg
        self.__ppd = ppd
        self.__type = type
 
        # __afficheur de type sevenSeg(relation de composition avec la class SevenSeg)
        self.__afficheur = SevenSeg.SevenSeg(self.__pa, self.__pb, self.__pc, self.__pd, self.__pe, self.__pf, self.__pg, self.__ppd, self.__type)
        self.__afficheur.Show0()
 
        self.systemStatus = 0
 
        # configuration des evenements des boutons gpio
        self.__z1.when_pressed = lambda: self.__check_z1_z2_z3_z4(1)
        self.__z2.when_pressed = lambda: self.__check_z1_z2_z3_z4(2)
        self.__z3.when_pressed = lambda: self.__check_z1_z2_z3_z4(3)
        self.__z4.when_pressed = lambda: self.__check_z1_z2_z3_z4(4)
        self.__on_off.when_pressed = self.__Activate
        self.__reset.when_pressed = self.__Reset
 
        # placere les labels et boutons dans la fenetre tikinter
        self.__lblz1.grid(row=0, column=0)
        self.__lblz2.grid(row=0, column=1)
        self.__lblz3.grid(row=1, column=0)
        self.__lblz4.grid(row=1, column=1)
        self.__lbl_on_off.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.__activate.grid(row=0, column=2, padx=10, pady=5)
        self.__deactivate.grid(row=1, column=2, padx=10, pady=10)
        self.__resetTk.grid(row=2, column=2, padx=10, pady=5)
 
        # demmarage de la fenetre tikinter
        self.__Root.mainloop()
 
    def __Activate(self):
        if self.systemStatus == 0:
            self.__afficheur.count_up()
            self.__afficheur.ShowA()
            self.systemStatus = 1
            self.__alarme.off()
            self.__lbl_on_off.config(bg="green")
        elif self.systemStatus == 1 :
            self.__afficheur.count_down()
            self.__afficheur.Show0()
            self.systemStatus = 0
            self.__alarme.off()
            self.__lbl_on_off.config(bg="red")
 
    def __Deactivate(self):
        if self.systemStatus == 1:
            self.__afficheur.count_down()
            self.__afficheur.Show0()
            self.systemStatus = 0
            self.__alarme.off()
            self.__lbl_on_off.config(bg="red")
 
    def __check_z1_z2_z3_z4(self, zone):
        if self.systemStatus == 1:
            self.show_zone(zone)
            self.__alarme.blink(on_time=0.5, off_time=0.5)
            self.__set_zone_color(zone, "red")
 
    def show_zone(self, zone):
        if zone == 1:
            self.__afficheur.Show1()
        elif zone == 2:
            self.__afficheur.Show2()
        elif zone == 3:
            self.__afficheur.Show3()
        elif zone == 4:
            self.__afficheur.Show4()
 
    def __set_zone_color(self, zone, color):
        if zone == 1:
            self.__lblz1.config(bg=color)
        elif zone == 2:
            self.__lblz2.config(bg=color)
        elif zone == 3:
            self.__lblz3.config(bg=color)
        elif zone == 4:
            self.__lblz4.config(bg=color)
 
    def __Reset(self):
        self.__alarme.off()
        self.__reset_zone_colors()
 
    def __reset_zone_colors(self):
        self.__lblz1.config(bg="light blue")
        self.__lblz2.config(bg="light blue")
        self.__lblz3.config(bg="light blue")
        self.__lblz4.config(bg="light blue")
 

