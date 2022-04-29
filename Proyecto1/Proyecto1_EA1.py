'''------------------------------------------------------------------------------
Autor: Andy Bonilla
Programa: proyecto 1, electronica analogica 1
Creado: 20 de marzo de 2022     
Descripcion: GUI para un ecualizador de 10 bandas con comunicacion con programa 
LTSpice
-------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------
-------------------------IMPORTAR LIBRERIAS--------------------------------------
------------------------------------------------------------------------------'''
from ast import AsyncFunctionDef
import builtins
from cmath import inf
from fileinput import filename
import tkinter as tk            #se importa libreria de GUI
from tkinter import *
from tkinter import filedialog
from numpy import rot90
#
import math
import time
import sys
from PyLTSpice.LTSpiceBatch import LTCommander
from shutil import copyfile
import os
'''------------------------------------------------------------------------------
-----------------------DEFINICION DE OBJETOS------------------------------------
------------------------------------------------------------------------------'''
root = Tk()                     #se le da nombre al objeto principal

#filename = fd.askopenfilename()
#variables de ganancia
gain1 = IntVar()         #variable de ganancia en slider 1
gain2 = IntVar()         #variable de ganancia en slider 2
gain3 = IntVar()         #variable de ganancia en slider 3
gain4 = IntVar()         #variable de ganancia en slider 4
gain5 = IntVar()         #variable de ganancia en slider 5
gain6 = IntVar()         #variable de ganancia en slider 6
gain7 = IntVar()         #variable de ganancia en slider 7
gain8 = IntVar()         #variable de ganancia en slider 8
gain9 = IntVar()         #variable de ganancia en slider 9
gain10 = IntVar()         #variable de ganancia en slider 10
gain11 = IntVar()         #variable de ganancia en slider 11
gain12 = IntVar()         #variable de ganancia en slider 12'''
#variables de conversion ganancia a resistencias
RB1 = IntVar()  #variable de ganancia 
RB2 = IntVar()         #variable de ganancia
RB3 = IntVar()         #variable de ganancia
RB4 = IntVar()         #variable de ganancia
RB5 = IntVar()         #variable de ganancia
RB6 = IntVar()         #variable de ganancia
RB7 = IntVar()         #variable de ganancia
RB8 = IntVar()         #variable de ganancia
RB9 = IntVar()         #variable de ganancia
RB10 = IntVar()         #variable de ganancia
M_dist = IntVar()         #variable de ganancia
M_gain = IntVar()         #variable de ganancia
#variables de archivos a importar
filename1 = Variable()    #variable para archivo de audio 1
filename2 = Variable()    #variable para archivo de audio 2
#variables de modos de ecualizacion
rock_var = IntVar()         #ecualizacion de rock
jazz_var = IntVar()         #ecualizacion de jazz
hiphop_var = IntVar()       #ecualizacion de hiphop
#
eq_var=0
'''------------------------------------------------------------------------------
-----------------------DEFINICION DE CLASES ------------------------------------
------------------------------------------------------------------------------'''
sliders1={'puntox1': 130, 'puntoy':60}
sliders2={'puntox2': 180, 'puntoy':60}
sliders3={'puntox3': 230, 'puntoy':60}
sliders4={'puntox4': 280, 'puntoy':60}
sliders5={'puntox5': 330, 'puntoy':60}
sliders6={'puntox6': 380, 'puntoy':60}
sliders7={'puntox7': 430, 'puntoy':60}
sliders8={'puntox8': 480, 'puntoy':60}
sliders9={'puntox9': 530, 'puntoy':60}
sliders10={'puntox10': 580, 'puntoy':60}
sliders11={'puntox11': 650, 'puntoy':60}
sliders12={'puntox12': 700, 'puntoy':60}
actualizar={'puntoxa':390, 'puntoya':350}

'''------------------------------------------------------------------------------
-----------------------DEFINICION DE FUNCIONES-----------------------------------
------------------------------------------------------------------------------'''
 #conjunto de funciones para convertir la ganancia en valores utiles de resistenci
def conv_gain1(g1):
    global RB1              #se usa la variable global para que jale
    #se mapea por intervalos
    if (g1==0):
        RB1 = 1000
        
    elif (g1==1):
        RB1 = 1700
        
    elif (g1==2):
        RB1 = 2400
        
    elif (g1==3):
        RB1 = 3100
        
    elif (g1==(-1)):
        RB1 = 700

    elif (g1==(-2)):
        RB1 = 400

    elif (g1==(-3)):
        RB1 = 100

    return RB1;

def conv_gain2(g2):
    global RB2          #se usa la variable global para que jale
    #se mapea por intervalos
    if (g2==0):
        RB2 = 1000
        
    elif (g2==1):
        RB2 = 1700
        
    elif (g2==2):
        RB2 = 2400
        
    elif (g2==3):
        RB2 = 3100
        
    elif (g2==(-1)):
        RB2 = 700

    elif (g2==(-2)):
        RB2 = 400

    elif (g2==(-3)):
        RB2 = 100
    return RB2

def conv_gain3(g3):
    global RB3  #se usa la variable global para que jale
    #se mapea por intervalos
    if (g3==0):
        RB3 = 1000
        
    elif (g3==1):
        RB3 = 1700
        
    elif (g3==2):
        RB3 = 2400
        
    elif (g3==3):
        RB3 = 3100
        
    elif (g3==(-1)):
        RB3 = 700

    elif (g3==(-2)):
        RB3 = 400

    elif (g3==(-3)):
        RB3 = 100
    return RB3

def conv_gain4(g4):
    global RB4  #se usa la variable global para que jale
    #se mapea por intervalos
    if (g4==0):
        RB4 = 1000
        
    elif (g4==1):
        RB4 = 1700
        
    elif (g4==2):
        RB4 = 2400
        
    elif (g4==3):
        RB4 = 3100
        
    elif (g4==(-1)):
        RB4 = 700

    elif (g4==(-2)):
        RB4 = 400

    elif (g4==(-3)):
        RB4 = 100
    return RB4

def conv_gain5(g5):
    global RB5      #se usa la variable global para que jale
    #se mapea por intervalos
    if (g5==0):
        RB5 = 1000
        
    elif (g5==1):
        RB5 = 1700
        
    elif (g5==2):
        RB5 = 2400
        
    elif (g5==3):
        RB5 = 3100
        
    elif (g5==(-1)):
        RB5 = 700

    elif (g5==(-2)):
        RB5 = 400

    elif (g5==(-3)):
        RB4 = 100
    return RB5

def conv_gain6(g6):
    global RB6  #se usa la variable global para que jale
    #se mapea por intervalos
    if (g6==0):
        RB6 = 1000
        
    elif (g6==1):
        RB6 = 1700
        
    elif (g6==2):
        RB6 = 2400
        
    elif (g6==3):
        RB6 = 3100
        
    elif (g6==(-1)):
        RB6 = 1800

    elif (g6==(-2)):
        RB6 = 2000

    elif (g6==(-3)):
        RB6 = 2200
    return RB6

def conv_gain7(g7):
    global RB7  #se usa la variable global para que jale
    #se mapea por intervalos
    if (g7==0):
        RB7 = 1000
        
    elif (g7==1):
        RB7 = 1700
        
    elif (g7==2):
        RB7 = 2400
        
    elif (g7==3):
        RB7 = 3100
        
    elif (g7==(-1)):
        RB7 = 700

    elif (g7==(-2)):
        RB7 = 400

    elif (g7==(-3)):
        RB7 = 100
    return RB7

def conv_gain8(g8):
    global RB8  #se usa la variable global para que jale
    #se mapea por intervalos
    if (g8==0):
        RB8 = 1000
        
    elif (g8==1):
        RB8 = 1700
        
    elif (g8==2):
        RB8 = 2400
        
    elif (g8==3):
        RB8 = 3100
        
    elif (g8==(-1)):
        RB8 = 700

    elif (g8==(-2)):
        RB8 = 400

    elif (g8==(-3)):
        RB8 = 100
    return RB8

def conv_gain9(g9):
    global RB9  #se usa la variable global para que jale
    #se mapea por intervalos
    if (g9==0):
        RB9 = 1000
        
    elif (g9==1):
        RB9 = 1700
        
    elif (g9==2):
        RB9 = 2400
        
    elif (g9==3):
        RB9 = 3100
        
    elif (g9==(-1)):
        RB9 = 700

    elif (g9==(-2)):
        RB9 = 400

    elif (g9==(-3)):
        RB9 = 100
    return RB9

def conv_gain10(g10):
    global RB10     #se usa la variable global para que jale
    #se mapea por intervalos
    if (g10==0):
        RB10 = 1000
        
    elif (g10==1):
        RB10 = 1700
        
    elif (g10==2):
        RB10 = 2400
        
    elif (g10==3):
        RB10 = 3100
        
    elif (g10==(-1)):
        RB10 = 700

    elif (g10==(-2)):
        RB10 = 400

    elif (g10==(-3)):
        RB10 = 100
    return RB10

def conv_dist(dist):
    global M_dist #se usa la variable global para que jale
    #se mapea por intervalos
    if (dist==0):
        M_dist = 0.0000000001
        
    elif (dist==1):
        M_dist = 1000
        
    elif (dist==2):
        M_dist = 2000
        
    elif (dist==3):
        M_dist = 3000
        
    elif (dist==(-1)):
        M_dist = 0.0000000001

    elif (dist==(-2)):
        M_dist = 0.0000000001

    elif (dist==(-3)):
        M_dist = 0.0000000001
    return M_dist

def conv_master(gain):
    global M_gain   #se usa la variable global para que jale
    #se mapea por intervalos
    if (gain==0):
        M_gain = 1000
        
    elif (gain==1):
        M_gain = 1700
        
    elif (gain==2):
        M_gain = 2400
        
    elif (gain==3):
        M_gain = 3100
        
    elif (gain==(-1)):
        M_gain = 700

    elif (gain==(-2)):
        M_gain= 400

    elif (gain==(-3)):
        M_gain = 100
    return M_gain
#conversion de todas las resistencias
def conversion_ganancias():
    conv_gain1( gain1.get())
    conv_gain2( gain2.get())
    conv_gain3( gain3.get())
    conv_gain4( gain4.get())
    conv_gain5( gain5.get())
    conv_gain6( gain6.get())
    conv_gain7( gain7.get())
    conv_gain8( gain8.get())
    conv_gain9( gain9.get())
    conv_gain10( gain10.get())
    conv_dist( gain11.get())
    conv_master(gain12.get())
#funcion de ejecutar el programa
def ecualizar():
    global eq_var                                                   #variable global de equalizacion
    global RB1, RB2, RB3, RB4, RB5, RB6, RB7, RB8, RB9, RB10        #variables globales de ganancias/banda
    global M_dist, M_gain                                           #variables globales distorsion y main

    print("El archivo 1 a importar es: "+filename1)                 #se muestra ubicaciond e .wav 1
    print("El archivo 2 a importar es: "+filename2)                 #se muestra ubicaciond e .wav 2
    #si se escogio un valor de ecualizacion predeterminado
    if (eq_var>0):
        #modo rock
        if(eq_var==1):
            eq_var=0                            #se baja banderazo
            print("Modo ecualización en Rock")  #se dan nuevos valores a resistencias segun Rock
            RB1=3000
            RB2=2800
            RB3=2500
            RB4=2800
            RB5=1500
            RB6=1900
            RB7=2000    
            RB8=2500
            RB9=2700
            RB10=3000
            M_dist=0.0000000001
            M_gain=1000
        #modo jazz
        elif(eq_var==2):                        #se dan nuevos valores a resistencias segun Jazz
            eq_var=0                            #se baja banderazo
            print("Modo ecualización en Jazz")
            RB1=2900
            RB2=2500
            RB3=2800
            RB4=2200
            RB5=1300
            RB6=1100
            RB7=1200    
            RB8=2000
            RB9=2200
            RB10=2300
            M_dist=0.0000000001
            M_gain=1000
        #modo reggae
        elif(eq_var==3):                        #se dan nuevos valores a resistencias segun Reggae
            eq_var=0                            #se baja banderazo
            print("Modo ecualización en Reggae")  
            RB1=2700
            RB2=2800
            RB3=2920
            RB4=2800
            RB5=1900
            RB6=1200
            RB7=2300    
            RB8=2700
            RB9=2900
            RB10=3000
            M_dist=0.0000000001
            M_gain=1000
    #si se hace ecualizacion manual
    else:
        conversion_ganancias()
        eq_var=0
    #se imprimen los valores de las resistencias segun el modo de ecualizacion
    selection1 = "RB1 = " + str(RB1) + " Ohms"
    selection2 = "RB2 = " + str(RB2) + " Ohms"
    selection3 = "RB3 = " + str(RB3) + " Ohms"
    selection4 = "RB4 = " + str(RB4) + " Ohms"
    selection5 = "RB5 = " + str(RB5) + " Ohms"
    selection6 = "RB6 = " + str(RB6) + " Ohms"
    selection7 = "RB7 = " + str(RB7) + " Ohms"
    selection8 = "RB8 = " + str(RB8) + " Ohms"
    selection9 = "RB9 = " + str(RB9) + " Ohms"
    selection10 = "RB10 = " + str(RB10) + " Ohms"
    selection11 = "M_dist = " + str(M_dist) + " Ohms"
    selection12 = "M_gain " + str(M_gain) + " Ohms"
    print(selection1)
    print(selection2)
    print(selection3)
    print(selection3)
    print(selection4)
    print(selection5)
    print(selection6)
    print(selection7)
    print(selection8)
    print(selection9)
    print(selection10)
    print(selection11)
    print(selection12)
    Parametros = {
    "RB1":str(RB1),     #variable para banda 1
    "RB2":str(RB2),     #variable para banda 2
    "RB3":str(RB3),     #variable para banda 3
    "RB4":str(RB4),     #variable para banda 4
    "RB5":str(RB5),     #variable para banda 5
    "RB6":str(RB6),     #variable para banda 6
    "RB7":str(RB7),     #variable para banda 7
    "RB8":str(RB8),     #variable para banda 8
    "RB9":str(RB9),     #variable para banda 9
    "RB10":str(RB10),     #variable para banda 10
    "M_dist":str(M_dist),     #variable para distorsion
    "M_gain":str(M_gain),     #variable para ganancia
    "transtop":str(5),
    "timestep":str(0.001)
    #.tran 0 {transtop} 0 {timestep} startup
    }
    file = bytes(os.getcwd()+"\param.txt",encoding='utf-8')
    fileflag = os.path.exists(file)
    if(fileflag == True):
        os.remove("param.txt")
   
    with open(os.getcwd()+"\\"+"param.txt", "w") as f:
        for i in Parametros:
            f.write(".param "+i+" "+Parametros[i]+"\n")
    meAbsPath = os.path.dirname(os.path.realpath(__file__))
    LTC = LTCommander(meAbsPath + "\\Proyecto1_EA1.asc")
    #C:\Users\Andy Bonilla\Desktop\Semestres\7mo Semestre\Electrónica analógica 1\Proyecto1
    LTC.add_instructions(
           #".wave \"C:\\Users\\franc\\Desktop\\Analogica\\Proyecto\\MIX1.wav\" 8 1K V(OUTF)"
           ".wave \"C:\\Users\\Andy Bonilla\\Desktop\\Semestres\\7mo Semestre\\Electrónica analógica 1\\Proyecto1\\Output.wav\" 8 1K V(OUT)"
           #".tran 5 startup uic"
           ".save V(OUTF)"
           ".option fastaccess"
           ".include param.txt"
        )
    LTC.reset_netlist()  # This resets all the changes done to the checklist
    LTC.add_instructions() # Changing the simulation file

    LTC.run()
    LTC.wait_completion()

#funciones para explorar archivos a ecualizar
def browseFiles1(): 
    global filename1        #variable global
    #para audio 1
    filename1 = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Archivo WAV", "*.wav*"),("all files","*.*"))) 
    label1_file_explorer.configure(text="File Opened: "+filename1)
    
def browseFiles2(): 
    global filename2        #variable global
    #para audio 2
    filename2 = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Archivo WAV", "*.wav*"),("all files","*.*"))) 
    label2_file_explorer.configure(text="File Opened: "+filename2) 
#funciones para seleccionar modos predeterminados de ecualizacion       
def rock_func ():
    global eq_var
    eq_var=1
    return eq_var

def jazz_func ():
    global eq_var
    eq_var=2
    return eq_var

def reggae_func ():
    global eq_var
    eq_var=3
    return eq_var    

'''------------------------------------------------------------------------------
----------------------------CUERPO DE INTERFAZ-----------------------------------
------------------------------------------------------------------------------'''
#---------FONDO DE LA INTERFAZ
img = PhotoImage(file="fondo2_.png")
label = Label(root,image=img)
label.place(x=0, y=0)

#---------TITULO
titulo=tk.Label(root,text = "Proyecto 1, Electrónica Analógica 1") #texto como titulo de GUI
titulo.place(x=330, y=10)
nombre=tk.Label(root, text="Andy Bonilla - 19451")
nombre.place(x=365,y=30)

#---------TITULO DE VENTANA
root.title("Ten band Equalizer")                   #le pones titulo al objeto
root.minsize(833,450)                              #le decis el tamaño a la ventana

#---------EXPLORADOR DE ARCHIVOS
#---------AUDIO 1
#explorador 1
label1_file_explorer = Label(root,text = "Archivo 1 a importar: ",fg = "black") 
label1_file_explorer.place(x = 80, y=250) 
#boton 1
button1_explore = Button(root, text = "Importar 1",command = browseFiles1)  
button1_explore.place(x = 230, y=220) 
#---------AUDIO 2
#explorador 2
label2_file_explorer = Label(root,text = "Archivo 2 a importar: ",fg = "black") 
label2_file_explorer.place(x = 80, y=270) 
#boton 2       
button2_explore = Button(root, text = "Importar 2",command = browseFiles2)  
button2_explore.place(x = 550, y=220) 

#---------BOTON DE SALIDA
button_exit = Button(root,text = "Salir",command = exit)  
button_exit.place(x = 400, y=400)   

#---------REFERENCIA DE DECIBELES
#label de 3dB
deb3 = Label(root, text="3dB")                      
deb3.pack()
deb3.place(x=sliders1["puntox1"]-30, y=sliders1["puntoy"])

#label de 0dB
deb0 = Label(root, text="0dB")                      
deb0.pack()
deb0.place(x=sliders1["puntox1"]-30, y=sliders1["puntoy"]+45)

#label de -3dB
deb3_ = Label(root, text="-3dB")                      
deb3_.pack()
deb3_.place(x=sliders1["puntox1"]-30, y=sliders1["puntoy"]+90)

#---------SLIDER 1, 31Hz
slider1=Scale(root, from_=3,to=-3,variable =gain1)
slider1.place(x=sliders1["puntox1"], y=sliders1["puntoy"])
#--------
L1 = Label(root, text="31Hz")                      
L1.pack()
L1.place(x=sliders1["puntox1"]+10, y=sliders1["puntoy"]+120)

#---------SLIDER 2, 63Hz
slider2=Scale(root, from_=3,to=-3, variable =gain2 )
slider2.pack()
slider2.place(x=sliders2["puntox2"], y=sliders2["puntoy"])
#--------
L2 = Label(root, text="63Hz")                      
L2.pack()
L2.place(x=sliders2["puntox2"]+10, y=sliders2["puntoy"]+120)

#---------SLIDER 3, 125Hz
slider3=Scale(root, from_=3,to=-3 ,variable =gain3 )
slider3.pack()
slider3.place(x=sliders3["puntox3"], y=sliders3["puntoy"])
#--------
L3 = Label(root, text="125Hz")                      
L3.pack()
L3.place(x=sliders3["puntox3"]+10, y=sliders3["puntoy"]+120)

#---------SLIDER 4, 250Hz
slider4=Scale(root, from_=3,to=-3, variable =gain4)
slider4.pack()
slider4.place(x=sliders4["puntox4"], y=sliders4["puntoy"])
#--------
L4 = Label(root, text="250Hz")                      
L4.pack()
L4.place(x=sliders4["puntox4"]+10, y=sliders4["puntoy"]+120)

#---------SLIDER 5, 500Hz
slider5=Scale(root,from_=3,to=-3,variable =gain5 )
slider5.pack()
slider5.place(x=sliders5["puntox5"], y=sliders4["puntoy"])
#--------
L5 = Label(root, text="500Hz")                      
L5.pack()
L5.place(x=sliders5["puntox5"]+10, y=sliders5["puntoy"]+120)

#---------SLIDER 6, 1kHz
slider6=Scale(root, from_=3,to=-3,variable =gain6)
slider6.pack()
slider6.place(x=sliders6["puntox6"], y=sliders6["puntoy"])
#--------
L6 = Label(root, text="1KHz")                      
L6.pack()
L6.place(x=sliders6["puntox6"]+10, y=sliders1["puntoy"]+120)

#---------SLIDER 7, 2KHz
slider7=Scale(root, from_=3,to=-3 ,variable =gain7)
slider7.pack()
slider7.place(x=sliders7["puntox7"], y=sliders7["puntoy"])
#--------
L7 = Label(root, text="2KHz")                      
L7.pack()
L7.place(x=sliders7["puntox7"]+10, y=sliders7["puntoy"]+120)

#---------SLIDER 8, 4KHz
slider8=Scale(root, from_=3,to=-3, variable =gain8)
slider8.pack()
slider8.place(x=sliders8["puntox8"], y=sliders8["puntoy"])
#--------
L8 = Label(root, text="4KHz")                      
L8.pack()
L8.place(x=sliders8["puntox8"]+10, y=sliders8["puntoy"]+120)

#---------SLIDER 9, 8KHz
slider9=Scale(root, from_=3,to=-3, variable =gain9 )
slider9.pack()
slider9.place(x=sliders9["puntox9"], y=sliders9["puntoy"])
#--------
L9 = Label(root, text="8KHz")                      
L9.pack()
L9.place(x=sliders9["puntox9"]+10, y=sliders9["puntoy"]+120)

#---------SLIDER 10, 16KHz
slider10=Scale(root, from_=3,to=-3, variable =gain10 )
slider10.pack()
slider10.place(x=sliders10["puntox10"], y=sliders10["puntoy"])
#--------
L10 = Label(root, text="16KHz")                      
L10.pack()
L10.place(x=sliders10["puntox10"]+10, y=sliders1["puntoy"]+120)

#---------SLIDER 11, Distorsion
slider11=Scale(root,from_=3,to=-3, variable =gain11)
slider11.pack()
slider11.place(x=sliders11["puntox11"], y=sliders11["puntoy"])
#--------
L11 = Label(root, text="Dist")                      
L11.pack()
L11.place(x=sliders11["puntox11"]+20, y=sliders11["puntoy"]+120)

#---------SLIDER 12, Master gain
slider12=Scale(root, from_=3,to=-3 ,variable =gain12)
slider12.pack()
slider12.place(x=sliders12["puntox12"], y=sliders12["puntoy"])
#--------
L12 = Label(root, text="Main")                      
L12.pack()
L12.place(x=sliders12["puntox12"]+20, y=sliders12["puntoy"]+120)

#---------BOTON DE ACTUALIZAR
b1 = Button(root, text="Ecualizar", command=ecualizar)
b1.place(x=actualizar["puntoxa"]+170, y=actualizar["puntoya"])

#---------BOTON DE MODOS DE ECUALIZACION
mb=Menubutton(root,text="EQ presets")
mb.menu = Menu(mb)
mb["menu"]= mb.menu
mb.menu.add_command(label="Rock", command=rock_func)
mb.menu.add_command(label="Jazz", command=jazz_func)
mb.menu.add_command(label="Reggae", command=reggae_func)
mb.pack()
mb.place(x=actualizar["puntoxa"]-150, y=actualizar["puntoya"])
'''------------------------------------------------------------------------------
------------------------------- PARAMETROS --------------------------------------
------------------------------------------------------------------------------'''

'''------------------------------------------------------------------------------
---------------------------------MAIN LOOP---------------------------------------
------------------------------------------------------------------------------'''
root.mainloop()
