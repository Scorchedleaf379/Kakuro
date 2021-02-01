from tkinter import *
from tkinter import messagebox
from random import *
import os
Bandera_Guardar_Configuracion=False
def ACERCA_DE():
    messagebox.showerror(message = "Creador: Gabriel Ruiz - Fecha 31/01/2021- Version 1.0")

def Inicia_Juego(Boton_1,Boton_2,Boton_3,Boton_4,Boton_5,Boton_6,Boton_7,Boton_8,Boton_9,Terminar_Juego,Deshacer_Jugada,Rehacer_Jugada,Borrar_Casilla,Nombre):
    if len(Nombre)<1 or len(Nombre)>30:
        messagebox.showerror(message = "NOMBRE DEBE SER DE 1 A 30 CARACTERES")
    else:
        Boton_1["state"]="normal"
        Boton_2["state"]="normal"
        Boton_3["state"]="normal"
        Boton_4["state"]="normal"
        Boton_5["state"]="normal"
        Boton_6["state"]="normal"
        Boton_7["state"]="normal"
        Boton_8["state"]="normal"
        Boton_9["state"]="normal"
        Terminar_Juego["state"]="normal"
        Deshacer_Jugada["state"]="normal"
        Rehacer_Jugada["state"]="normal"
        Borrar_Casilla["state"]="normal"
        
        
def VentanaInicial():
    Ventana_Inicial=Tk()
    Ventana_Inicial.geometry('{}x{}+{}+{}'.format(600,600,350,0))
    Ventana_Inicial.configure(bg="black")
    Boton_Jugar=Button(Ventana_Inicial,width=13,height=2, text="JUGAR",bg="white",command=lambda:VentanaJuego())
    Boton_Jugar.place(x=250,y=200)
    Boton_Configuracion=Button(Ventana_Inicial,width=13,height=2, text="CONFIGURACIÓN",bg="white",command=lambda:VentanaConfiguracion(Ventana_Inicial))
    Boton_Configuracion.place(x=250,y=250)
    Boton_Manual=Button(Ventana_Inicial,width=13,height=2, text="MANUAL",bg="white")
    Boton_Manual.place(x=250,y=300)
    Boton_Acerca=Button(Ventana_Inicial,width=13,height=2, text="ACERCA DE",bg="white",command=lambda:ACERCA_DE())
    Boton_Acerca.place(x=250,y=350)

    
def VentanaConfiguracion(Ventana_Inicial):
    Ventana_Configuracion=Tk()
    Ventana_Configuracion.geometry('{}x{}+{}+{}'.format(600,600,350,0))
    Ventana_Inicial.withdraw()
    Variable_Dificultad=IntVar(Ventana_Configuracion)
    Facil=Radiobutton(Ventana_Configuracion, text="Fácil",variable=Variable_Dificultad,value=1)
    Facil.place (x=10, y=55)
    Medio=Radiobutton(Ventana_Configuracion, text="Medio",variable=Variable_Dificultad,value=2)
    Medio.place (x=10, y=75)
    Dificil=Radiobutton(Ventana_Configuracion, text="Dificil",variable=Variable_Dificultad,value=3)
    Dificil.place (x=10, y=95)

    Variable_Reloj=IntVar(Ventana_Configuracion)
    Cronometro_Si=Radiobutton(Ventana_Configuracion, text="Si", variable=Variable_Reloj, value=1)
    Cronometro_Si.place(x=10,y=165)
    Cronometro_No=Radiobutton(Ventana_Configuracion, text="No", variable=Variable_Reloj, value=2)
    Cronometro_No.place(x=10,y=185)
    Timer=Radiobutton(Ventana_Configuracion, text="Timer", variable=Variable_Reloj, value=3)
    Timer.place(x=10,y=205)

    boton_ACEPTAR=Button(Ventana_Configuracion, text="ACEPTAR",bg="green",command=lambda:aceptar_configuracion())
    boton_ACEPTAR.place(x=540,y=575)

    if Bandera_Guardar_Configuracion:
        Variable_Dificultad.set(Variable_Guardar_Dificultad)
        Variable_Reloj.set(Variable_Guardar_Reloj)
    else:
        Facil.select()
        Cronometro_Si.select()
        
def aceptar_configuracion():
    global Variable_Guardar_Dificultad,Variable_Guardar_Reloj
    Variable_Guardar_Dificultad=Variable_Dificultad
    Variable_Guardar_Reloj=Variable_Reloj
    Bandera_Guardar_Configuracion=True
    

def VentanaJuego():
    Ventana_Juego=Tk()
    Ventana_Juego.geometry('{}x{}+{}+{}'.format(600,600,350,0))
    KAKURO=Label(Ventana_Juego,text="KAKURO",font=60,bg="red")
    KAKURO.place(x=0,y=0)
    Nombre=Entry(Ventana_Juego,width= 45)
    Nombre.place(x=320,y=0)
    Nombre_Jugador=Label(Ventana_Juego,text="Jugador:")
    Nombre_Jugador.place(x=265,y=0)
    #botones de selección de número
    Boton_1=Button(Ventana_Juego,width=3,height=2,text="1")
    Boton_1.place(x=560,y=25)
    Boton_2=Button(Ventana_Juego,width=3,height=2,text="2")
    Boton_2.place(x=560,y=65)
    Boton_3=Button(Ventana_Juego,width=3,height=2,text="3")
    Boton_3.place(x=560,y=105)
    Boton_4=Button(Ventana_Juego,width=3,height=2,text="4")
    Boton_4.place(x=560,y=145)
    Boton_5=Button(Ventana_Juego,width=3,height=2,text="5")
    Boton_5.place(x=560,y=185)
    Boton_6=Button(Ventana_Juego,width=3,height=2,text="6")
    Boton_6.place(x=560,y=225)
    Boton_7=Button(Ventana_Juego,width=3,height=2,text="7")
    Boton_7.place(x=560,y=265)
    Boton_8=Button(Ventana_Juego,width=3,height=2,text="8")
    Boton_8.place(x=560,y=305)
    Boton_9=Button(Ventana_Juego,width=3,height=2,text="9")
    Boton_9.place(x=560,y=345)

    Boton_1["state"]="disable"
    Boton_2["state"]="disable"
    Boton_3["state"]="disable"
    Boton_4["state"]="disable"
    Boton_5["state"]="disable"
    Boton_6["state"]="disable"
    Boton_7["state"]="disable"
    Boton_8["state"]="disable"
    Boton_9["state"]="disable"
    

    Top_10=Button(Ventana_Juego,width=14,height=2,text="Top 10",bg="yellow")
    Top_10.place(x=490,y=450)
    Guardar_Juego=Button(Ventana_Juego,width=14,height=2,text="Guardar Juego",bg="darkorange3")
    Guardar_Juego.place(x=490,y=490)
    Cargar_Juego=Button(Ventana_Juego,width=14,height=2,text="Cargar Juego 10",bg="orangered4")
    Cargar_Juego.place(x=490,y=530)
    Borrar_Casilla=Button(Ventana_Juego,width=14,height=2,text="Borrar Casilla",bg="snow4")
    Borrar_Casilla.place(x=380,y=450)
    Borrar_Juego=Button(Ventana_Juego,width=14,height=2,text="Borrar Juego",bg="skyblue3")
    Borrar_Juego.place(x=380,y=490)
    Terminar_Juego=Button(Ventana_Juego,width=14,height=2,text="Terminar Juego",bg="forestgreen")
    Terminar_Juego.place(x=380,y=530)
    Deshacer_Jugada=Button(Ventana_Juego,width=14,height=2,text="Deshacer Jugada",bg="honeydew3")
    Deshacer_Jugada.place(x=270,y=450)
    Rehacer_Jugada=Button(Ventana_Juego,width=14,height=2,text="Rehacer Jugada",bg="cyan3")
    Rehacer_Jugada.place(x=270,y=490)
    Iniciar_Juego=Button(Ventana_Juego,width=14,height=2,text="Iniciar Juego",bg="deeppink",command=lambda:Inicia_Juego(Boton_1,Boton_2,Boton_3,Boton_4,Boton_5,Boton_6,Boton_7,Boton_8,Boton_9,Terminar_Juego,Deshacer_Jugada,Rehacer_Jugada,Borrar_Casilla,Nombre.get()))
    Iniciar_Juego.place(x=50,y=450)

    Terminar_Juego["state"]="disable"
    Deshacer_Jugada["state"]="disable"
    Rehacer_Jugada["state"]="disable"
    Borrar_Casilla["state"]="disable"
    
    #botnoes Tablero
    A1=Button(Ventana_Juego,width=3,height=2,text="")
    A1.place(x=40,y=50)
    A2=Button(Ventana_Juego,width=3,height=2,text="")
    A2.place(x=40,y=90)
    A3=Button(Ventana_Juego,width=3,height=2,text="")
    A3.place(x=40,y=130)
    A4=Button(Ventana_Juego,width=3,height=2,text="")
    A4.place(x=40,y=170)
    A5=Button(Ventana_Juego,width=3,height=2,text="")
    A5.place(x=40,y=210)
    A6=Button(Ventana_Juego,width=3,height=2,text="")
    A6.place(x=40,y=250)
    A7=Button(Ventana_Juego,width=3,height=2,text="")
    A7.place(x=40,y=290)
    A8=Button(Ventana_Juego,width=3,height=2,text="")
    A8.place(x=40,y=330)
    A9=Button(Ventana_Juego,width=3,height=2,text="")
    A9.place(x=40,y=370)
    Columna_A=Label(Ventana_Juego,text="A")
    Columna_A.place(x=50,y=30)
    

    B1=Button(Ventana_Juego,width=3,height=2,text="")
    B1.place(x=70,y=50)
    B2=Button(Ventana_Juego,width=3,height=2,text="")
    B2.place(x=70,y=90)
    B3=Button(Ventana_Juego,width=3,height=2,text="")
    B3.place(x=70,y=130)
    B4=Button(Ventana_Juego,width=3,height=2,text="")
    B4.place(x=70,y=170)
    B5=Button(Ventana_Juego,width=3,height=2,text="")
    B5.place(x=70,y=210)
    B6=Button(Ventana_Juego,width=3,height=2,text="")
    B6.place(x=70,y=250)
    B7=Button(Ventana_Juego,width=3,height=2,text="")
    B7.place(x=70,y=290)
    B8=Button(Ventana_Juego,width=3,height=2,text="")
    B8.place(x=70,y=330)
    B9=Button(Ventana_Juego,width=3,height=2,text="")
    B9.place(x=70,y=370)
    Columna_B=Label(Ventana_Juego,text="B")
    Columna_B.place(x=80,y=30)

    C1=Button(Ventana_Juego,width=3,height=2,text="")
    C1.place(x=100,y=50)
    C2=Button(Ventana_Juego,width=3,height=2,text="")
    C2.place(x=100,y=90)
    C3=Button(Ventana_Juego,width=3,height=2,text="")
    C3.place(x=100,y=130)
    C4=Button(Ventana_Juego,width=3,height=2,text="")
    C4.place(x=100,y=170)
    C5=Button(Ventana_Juego,width=3,height=2,text="")
    C5.place(x=100,y=210)
    C6=Button(Ventana_Juego,width=3,height=2,text="")
    C6.place(x=100,y=250)
    C7=Button(Ventana_Juego,width=3,height=2,text="")
    C7.place(x=100,y=290)
    C8=Button(Ventana_Juego,width=3,height=2,text="")
    C8.place(x=100,y=330)
    C9=Button(Ventana_Juego,width=3,height=2,text="")
    C9.place(x=100,y=370)
    Columna_C=Label(Ventana_Juego,text="C")
    Columna_C.place(x=110,y=30)

    D1=Button(Ventana_Juego,width=3,height=2,text="")
    D1.place(x=130,y=50)
    D2=Button(Ventana_Juego,width=3,height=2,text="")
    D2.place(x=130,y=90)
    D3=Button(Ventana_Juego,width=3,height=2,text="")
    D3.place(x=130,y=130)
    D4=Button(Ventana_Juego,width=3,height=2,text="")
    D4.place(x=130,y=170)
    D5=Button(Ventana_Juego,width=3,height=2,text="")
    D5.place(x=130,y=210)
    D6=Button(Ventana_Juego,width=3,height=2,text="")
    D6.place(x=130,y=250)
    D7=Button(Ventana_Juego,width=3,height=2,text="")
    D7.place(x=130,y=290)
    D8=Button(Ventana_Juego,width=3,height=2,text="")
    D8.place(x=130,y=330)
    D9=Button(Ventana_Juego,width=3,height=2,text="")
    D9.place(x=130,y=370)
    Columna_D=Label(Ventana_Juego,text="D")
    Columna_D.place(x=140,y=30)

    E1=Button(Ventana_Juego,width=3,height=2,text="")
    E1.place(x=160,y=50)
    E2=Button(Ventana_Juego,width=3,height=2,text="")
    E2.place(x=160,y=90)
    E3=Button(Ventana_Juego,width=3,height=2,text="")
    E3.place(x=160,y=130)
    E4=Button(Ventana_Juego,width=3,height=2,text="")
    E4.place(x=160,y=170)
    E5=Button(Ventana_Juego,width=3,height=2,text="")
    E5.place(x=160,y=210)
    E6=Button(Ventana_Juego,width=3,height=2,text="")
    E6.place(x=160,y=250)
    E7=Button(Ventana_Juego,width=3,height=2,text="")
    E7.place(x=160,y=290)
    E8=Button(Ventana_Juego,width=3,height=2,text="")
    E8.place(x=160,y=330)
    E9=Button(Ventana_Juego,width=3,height=2,text="")
    E9.place(x=160,y=370)
    Columna_E=Label(Ventana_Juego,text="E")
    Columna_E.place(x=170,y=30)

    F1=Button(Ventana_Juego,width=3,height=2,text="")
    F1.place(x=190,y=50)
    F2=Button(Ventana_Juego,width=3,height=2,text="")
    F2.place(x=190,y=90)
    F3=Button(Ventana_Juego,width=3,height=2,text="")
    F3.place(x=190,y=130)
    F4=Button(Ventana_Juego,width=3,height=2,text="")
    F4.place(x=190,y=170)
    F5=Button(Ventana_Juego,width=3,height=2,text="")
    F5.place(x=190,y=210)
    F6=Button(Ventana_Juego,width=3,height=2,text="")
    F6.place(x=190,y=250)
    F7=Button(Ventana_Juego,width=3,height=2,text="")
    F7.place(x=190,y=290)
    F8=Button(Ventana_Juego,width=3,height=2,text="")
    F8.place(x=190,y=330)
    F9=Button(Ventana_Juego,width=3,height=2,text="")
    F9.place(x=190,y=370)
    Columna_F=Label(Ventana_Juego,text="F")
    Columna_F.place(x=200,y=30)

    G1=Button(Ventana_Juego,width=3,height=2,text="")
    G1.place(x=220,y=50)
    G2=Button(Ventana_Juego,width=3,height=2,text="")
    G2.place(x=220,y=90)
    G3=Button(Ventana_Juego,width=3,height=2,text="")
    G3.place(x=220,y=130)
    G4=Button(Ventana_Juego,width=3,height=2,text="")
    G4.place(x=220,y=170)
    G5=Button(Ventana_Juego,width=3,height=2,text="")
    G5.place(x=220,y=210)
    G6=Button(Ventana_Juego,width=3,height=2,text="")
    G6.place(x=220,y=250)
    G7=Button(Ventana_Juego,width=3,height=2,text="")
    G7.place(x=220,y=290)
    G8=Button(Ventana_Juego,width=3,height=2,text="")
    G8.place(x=220,y=330)
    G9=Button(Ventana_Juego,width=3,height=2,text="")
    G9.place(x=220,y=370)
    Columna_G=Label(Ventana_Juego,text="G")
    Columna_G.place(x=230,y=30)

    H1=Button(Ventana_Juego,width=3,height=2,text="")
    H1.place(x=250,y=50)
    H2=Button(Ventana_Juego,width=3,height=2,text="")
    H2.place(x=250,y=90)
    H3=Button(Ventana_Juego,width=3,height=2,text="")
    H3.place(x=250,y=130)
    H4=Button(Ventana_Juego,width=3,height=2,text="")
    H4.place(x=250,y=170)
    H5=Button(Ventana_Juego,width=3,height=2,text="")
    H5.place(x=250,y=210)
    H6=Button(Ventana_Juego,width=3,height=2,text="")
    H6.place(x=250,y=250)
    H7=Button(Ventana_Juego,width=3,height=2,text="")
    H7.place(x=250,y=290)
    H8=Button(Ventana_Juego,width=3,height=2,text="")
    H8.place(x=250,y=330)
    H9=Button(Ventana_Juego,width=3,height=2,text="")
    H9.place(x=250,y=370)
    Columna_H=Label(Ventana_Juego,text="H")
    Columna_H.place(x=260,y=30)

    I1=Button(Ventana_Juego,width=3,height=2,text="")
    I1.place(x=280,y=50)
    I2=Button(Ventana_Juego,width=3,height=2,text="")
    I2.place(x=280,y=90)
    I3=Button(Ventana_Juego,width=3,height=2,text="")
    I3.place(x=280,y=130)
    I4=Button(Ventana_Juego,width=3,height=2,text="")
    I4.place(x=280,y=170)
    I5=Button(Ventana_Juego,width=3,height=2,text="")
    I5.place(x=280,y=210)
    I6=Button(Ventana_Juego,width=3,height=2,text="")
    I6.place(x=280,y=250)
    I7=Button(Ventana_Juego,width=3,height=2,text="")
    I7.place(x=280,y=290)
    I8=Button(Ventana_Juego,width=3,height=2,text="")
    I8.place(x=280,y=330)
    I9=Button(Ventana_Juego,width=3,height=2,text="")
    I9.place(x=280,y=370)
    Columna_I=Label(Ventana_Juego,text="I")
    Columna_I.place(x=290,y=30)

    Fila_1=Label(Ventana_Juego,text="1")
    Fila_1.place(x=25,y=60)
    Fila_2=Label(Ventana_Juego,text="2")
    Fila_2.place(x=25,y=100)
    Fila_3=Label(Ventana_Juego,text="3")
    Fila_3.place(x=25,y=140)
    Fila_4=Label(Ventana_Juego,text="4")
    Fila_4.place(x=25,y=180)
    Fila_5=Label(Ventana_Juego,text="5")
    Fila_5.place(x=25,y=220)
    Fila_6=Label(Ventana_Juego,text="6")
    Fila_6.place(x=25,y=260)
    Fila_7=Label(Ventana_Juego,text="7")
    Fila_7.place(x=25,y=300)
    Fila_8=Label(Ventana_Juego,text="8")
    Fila_8.place(x=25,y=340)
    Fila_9=Label(Ventana_Juego,text="9")
    Fila_9.place(x=25,y=380)

    VentanaJuego.mainloop()
    
VentanaInicial()
