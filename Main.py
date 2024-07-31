import AlarmSys
class Main :
    def __init__(self): 
        self.AlarmSys = AlarmSys.AlarmSys(z1=22, z2=5, z3=6, z4=19, on_off=27, reset=16, alarme=21,
                                        lblz1="Z1", lblz2="Z2", lblz3="Z3", lblz4="Z4", lbl_on_off="ON/OFF"
                                        ,pa=24, pb=9, pc=10, pd=11, pe=12, pf=13, pg=17, ppd=1, type=False)

if __name__ == "__main__":
    Main()

