
try:
    import os
    import time
    import tkinter as UI
    from tkinter import *
    from random import randint
    from colorama import Fore, Back, Style

    print(Fore.RED+"[Vitals X]")
    print("V.0.0.1 (DEV)")

    # Files & Paths Check

    def VitalsXFC(file):
        if os.path.exists(file) == False:
            print(Fore.WHITE+"\n["+Fore.CYAN+"!"+Fore.WHITE+"] "+Fore.RED+"The file "+Fore.BLUE+file+" "+Fore.RED+"doesn't exists")
            time.sleep(1)
            exit()

    def VitalsXPC(dir):
        if os.path.exists(dir) == False:
            print(Fore.WHITE+"\n["+Fore.CYAN+"!"+Fore.WHITE+"] "+Fore.RED+"The dir "+Fore.BLUE+dir+" "+Fore.RED+"doesn't exists")
            time.sleep(1)
            exit()

    # Initial Check

    VitalsXPC("VitalsX")
    VitalsXPC("VitalsX\\BloodKernel")
    VitalsXFC("VitalsX\\BloodKernel\\BloodKernel.py")
    VitalsXFC("VitalsX\\vitalsxlogo.png")

    # Loading & Splash

    def PBVitalsX():
        try:
            def ProgressBar():
                if x == 0:
                    print("[          ]", end='\r')
                if x == 1:
                    print("[■         ]", end='\r')
                if x == 2:
                    print("[■■        ]", end='\r')
                if x == 3:
                    print("[■■■       ]", end='\r')
                if x == 4:
                    print("[■■■■      ]", end='\r')
                if x == 5:
                    print("[■■■■■     ]", end='\r')
                if x == 6:
                    print("[■■■■■■    ]", end='\r')
                if x == 7:
                    print("[■■■■■■■   ]", end='\r')
                if x == 8:
                    print("[■■■■■■■■  ]", end='\r')
                if x == 9:
                    print("[■■■■■■■■■ ]", end='\r')
                if x == 10:
                    print("[■■■■■■■■■■]", end='\r')
            for x in range(0, 11):
                ProgressBar()
                rn = randint(1,3)
                if rn == 1:
                    rn = float(0.1)
                elif rn == 2:
                    rn = float(0.2)
                elif rn == 3:
                    rn = float(0.3)
                time.sleep(rn)
        except KeyboardInterrupt:
            print(Fore.WHITE+"\n\n["+Fore.CYAN+"!"+Fore.WHITE+"] "+Fore.RED+"Keyboard Interrupt")
            time.sleep(1)
            exit()
    ui = UI.Tk()
    ui.geometry("526x526")
    ui.title("Vitals X - BloodKernel")
    ui.wm_attributes("-topmost", True)
    ui.wm_attributes('-alpha', 0.8)
    ui.wm_attributes('-toolwindow', True)
    ui.configure(bg="black")

    VitalsXPC("VitalsX")
    VitalsXFC("VitalsX\\vitalsxlogo.png")
    vitalslogo = PhotoImage(file="VitalsX/vitalsxlogo.png")
    Label(ui, image=vitalslogo).place(x=0, y=0)

    def LoadingVitalsX1():
        print("\n\nLoading BloodKernel...")
        PBVitalsX()

    def LoadingVitalsX2():
        print("\n\nLoading Vitals X...")
        PBVitalsX()

    def SplashDestroy():
        ui.destroy()

    ui.after(100, LoadingVitalsX1)
    ui.after(1000, LoadingVitalsX2)
    ui.after(5000, SplashDestroy)
    ui.mainloop()

    print("\n\nENDLOOP")

except KeyboardInterrupt:
    print(Fore.WHITE+"\n["+Fore.CYAN+"!"+Fore.WHITE+"] "+Fore.RED+"Keyboard Interrupt")
    time.sleep(1)
    exit()