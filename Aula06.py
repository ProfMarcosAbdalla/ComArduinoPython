import serial
import time
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Inicializa o TKinter
raiz = Tk()
raiz.geometry('1000x500')
# Icone
raiz.iconbitmap('Logo.ico')


# Cria as funçoes dos botoes
def CONFIG():
    global ser
    PTA = COM_txt.get()
    BOU = int(BR_txt.get())
    ser = serial.Serial(PTA, BOU)
    time.sleep(1)
    if ser!=None:
        print('Ok')
    

def LER():
    global y 
    global tx
    global ser
    y = []
    tx = []
    t0 = time.time()
    ts = int(TEMPO_TXT.get())
    t = 0
    while t<ts:
        ser.write(bytes('S', 'UTF-8'))
        arduinoData = ser.readline().decode('ascii')
        tx.append(t)
        y.append(float(arduinoData))
        t = time.time()-t0

        Label(raiz, text = 'Sinal Lido', font = 20).place(x = 250, y = 100)

        var = StringVar()
        txt = Label(raiz, textvariable=var, font = 20, width=10)
        var.set(str(y[-1]))
        txt.place(x = 250, y = 140)

        if y[-1]>=370:
            txt.config(bg = 'green')
        else:
            txt.config(bg = 'red')

        Label(raiz, text = 'Tempo Decorrido (s)', font = 20).place(x = 190, y = 180)
        TD = StringVar()
        TD_TXT = Label(raiz, textvariable=TD, bg = 'white', font = 20, width=10).place(x = 250, y = 220)
        TD.set(str(np.round(t,2)))


        #time.sleep(0.1)
        raiz.update() # Mostrar a variavel de leitura mudando

    fig1, ax1 = plt.subplots()
    ax1.plot(tx,y)
    ax1.set_title('Sinal Coletado')
    ax1.set_xlabel('Tempo')
    ax1.set_ylabel('Amplitude')
    #plt.show()
    img1 = FigureCanvasTkAgg(fig1, QUADRO)
    img1.draw()
    img1.get_tk_widget().pack()
    return tx, y

def FIM():
    global ser
    ser.close()
    raiz.quit()
    raiz.destroy()

def SALVAR():
    global y 
    global tx
    with open("Dados.csv", "w") as out_file:
        for i in range(len(y)):
            out_string = ""
            out_string += str(y[i])
            out_string += "," + str(tx[i])
            out_string += "\n"
            out_file.write(out_string)


# Textos Fixos e Entradas
TXT_COM = Label(raiz, text = 'Porta COM:', font = 20)
TXT_COM.place(x = 20, y = 20)

COM = StringVar()
COM_txt = Entry(raiz, textvariable=COM, width=10)
COM_txt.place(x = 20, y = 60)

TXT_BR = Label(raiz, text = 'Bound rate:', font = 20)
TXT_BR.place(x = 20, y = 100)

BR = StringVar()
BR_txt = Entry(raiz, textvariable=BR, width=10)
BR_txt.place(x = 20, y = 140)

TEMP_TXT = Label(raiz, text = 'Tempo de Ensaio (s)', font = 20)
TEMP_TXT.place(x = 20, y = 180)
TEMPO = IntVar()
TEMPO_TXT = Entry(raiz, textvariable= TEMPO, width=5)
TEMPO_TXT.place(x = 20, y = 220)



# BOTOES
B2 = Button(raiz, text = 'Configurar?',
            font = 20,
            command=CONFIG)
B2.place(x = 20, y = 280)

B3 = Button(raiz, text = 'Ler Dados',
            font = 20,
            command = LER)
B3.place(x = 20, y = 320)

B5 = Button(raiz, text = 'Salvar', command = SALVAR, font = 20)
B5.place(x = 20, y = 360)

B4 = Button(raiz, text = 'Finalizar',
            font = 20,
            command = FIM)
B4.place(x = 20, y = 400)



# AREA DO GRAFICO
QUADRO = Frame(raiz,
               highlightbackground = '#FA8072',
               highlightthickness = 3,
               relief=RAISED)
QUADRO.place(x = 350, y = 10)



raiz.mainloop()
