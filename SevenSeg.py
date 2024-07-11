from gpiozero import LED
from signal import pause
from time import sleep
class SevenSeg : 

    #Constructeur
    def __init__(self,sa,sb,sc,sd,se,sf,sg,pd,type):
        self.__sa = LED(sa)
        self.__sb = LED(sb)
        self.__sc = LED(sc)
        self.__sd = LED(sd)
        self.__se = LED(se)
        self.__sf = LED(sf)
        self.__sg = LED(sg)
        self.__pd = LED(pd)
        self.__type = type
    
    #get & set __sa
    @property
    def SA(self) :
        return self.__sa
    @SA.setter
    def SA(self,sa) :
        self.__sa = sa
    
    #get & set __sa
    @property
    def SB(self) :
        return self.__sb
    @SB.setter
    def SB(self,sb) :
        self.__sb = sb

    #get & set __sc
    @property
    def SC(self) :
        return self.__sc
    @SC.setter
    def SC(self,sc) :
        self.__sc = sc

    #get & set __sd
    @property
    def SD(self) :
        return self.__sd
    @SD.setter
    def SD(self,sd) :
        self.__sd = sd

    #get & set __se
    @property
    def SE(self) :
        return self.__se
    @SE.setter
    def SE(self,se) :
        self.__se = se

    #get & set __sf
    @property
    def SF(self) :
        return self.__sf
    @SF.setter
    def SF(self,sf) :
        self.__sf = sf

    #get & set __sg
    @property
    def SG(self) :
        return self.__sg
    @SG.setter
    def SG(self,sg) :
        self.__sg = sg

    #get & set __type
    @property
    def Type(self) :
        return self.__type
    @Type.setter
    def Type(self,type) :
        self.__type = type
    
    #get & set __pd
    @property
    def PD(self) :
        return self.__pd
    @PD.setter
    def PD(self,pd) :
        self.__pd = pd
    
    #Méthode pour afficher un chiffre 0
    def Show0(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()

    #Méthode pour afficher un chiffre 1
    def Show1(self):
        if self.__type == True:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()

    #Méthode pour afficher un chiffre 2
    def Show2(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.on()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.off()
    
    #Méthode pour afficher un chiffre 3
    def Show3(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()

    #Méthode pour afficher un chiffre 4
    def Show4(self):
        if self.__type == True:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.off()

    #Méthode pour afficher un chiffre 5
    def Show5(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.off()
            self.__sc.on()
            self.__sd.on()
            self.__se.off()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.off()
            self.__sd.off()
            self.__se.on()
            self.__sf.off()
            self.__sg.off()

    #Méthode pour afficher un chiffre 6
    def Show6(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.off()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()

    #Méthode pour afficher un chiffre 7
    def Show7(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()

    #Méthode pour afficher un chiffre 8
    def Show8(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()

    #Méthode pour afficher un chiffre 9
    def Show9(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.off()

    #Methode pour afficher la lettre A
    def ShowA(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()

    #Methode pour afficher la lettre b en miniscule
    def ShowB(self):
        if self.__type == True:
            self.__sa.off()
            self.__sb.off()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.on()
            self.__sb.on()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()

    #Methode pour afficher la lettre C
    def ShowC(self):
        if self.__type == True:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()

    # Méthode pour afficher la lettre D
    def ShowD(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.off()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.on()
            self.__sg.off()

    # Méthode pour afficher la lettre E
    def ShowE(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()

    #Methode pour afficher la lettre F
    def ShowF(self):
        if self.__type == True:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
    
    #Methode pour afficher la lettre L
    def ShowL(self):
        if self.__type == True:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.off()
        else:
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.on()

    #Methode pour afficher la lettre H
    def ShowH(self):
        if self.__type == True:
            self.__sa.off()
            self.__sb.on()
            self.__sc.on()
            self.__sd.off()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
        else:
            self.__sa.on()
            self.__sb.off()
            self.__sc.off()
            self.__sd.on()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()

    #Methode pour etteindre tout les segements
    def Clear(self):
        if self.__type == True:
            self.__sa.off()
            self.__sb.off()
            self.__sc.off()
            self.__sd.off()
            self.__se.off()
            self.__sf.off()
            self.__sg.off()
        else : 
            self.__sa.on()
            self.__sb.on()
            self.__sc.on()
            self.__sd.on()
            self.__se.on()
            self.__sf.on()
            self.__sg.on()
    
    #Methode pour compter de 0 a 9
    def count_up(self):
        self.Show0()
        sleep(1)

        self.Show1()
        sleep(1)

        self.Show2()
        sleep(1)

        self.Show3()
        sleep(1)

        self.Show4()
        sleep(1)

        self.Show5()
        sleep(1)

        self.Show6()
        sleep(1)

        self.Show7()
        sleep(1)

        self.Show8()
        sleep(1)

        self.Show9()
        sleep(1)
    
    #Methode pour compter de 9 a 0 
    def count_down(self):
        self.Show9()
        sleep(1)

        self.Show8()
        sleep(1)

        self.Show7()
        sleep(1)

        self.Show6()
        sleep(1)

        self.Show5()
        sleep(1)

        self.Show4()
        sleep(1)

        self.Show3()
        sleep(1)

        self.Show2()
        sleep(1)

        self.Show1()
        sleep(1)

        self.Show0()
        sleep(1)
        
    def Flas0(self) : 
        while True:  
            self.Show0()   
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def Flas1(self) :
        while True:  
            self.Show1()   
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def Flas2(self) :
        while True:  
            self.Show2()   
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def Flas3(self) : 
        while True:
            self.Show3()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def Flas4(self) :
        while True:
            self.Show4()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def Flas5(self) :
        while True:
            self.Show5()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def Flas6(self) :
        while True:
            self.Show6()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def Flas7(self) :
        while True:
            self.Show7()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def Flas8(self) :
        while True:
            self.Show8()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def Flas9(self) :
        while True:
            self.Show9()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def FlasA(self) :
        while True:
            self.ShowA()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def FlasB(self) :
        while True:
            self.ShowB()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def FlasC(self) :
        while True:
            self.ShowC()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def FlasD(self) :
        while True:
            self.ShowD()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def FlasE(self) :
        while True:
            self.ShowE()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def FlasF(self) :
        while True:
            self.ShowF()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def FlasL(self):
         for _ in range(5):
            self.ShowL()
            sleep(0.5)
            self.Clear()
            sleep(0.5)

    def FlasH(self):
        for _ in range(5):
            self.ShowH()
            sleep(0.5)
            self.Clear()
            sleep(0.5)
