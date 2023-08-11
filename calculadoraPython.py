from tkinter import *

def Digitar(num):
    caixaTexto.insert(END, num)
    
def Calcular():
    conta = str(caixaTexto.get())
    resultado = float(eval(conta))
    caixaTexto.delete(0, END)
    caixaTexto.insert(END, resultado)

def apaga():
    caixaTexto.delete(0, END)

def backspace():
    caixaTexto.delete(len(caixaTexto.get())-1,END)
    
window = Tk()
window.geometry("300x400")
window.config(background="black")
window.resizable(width=False, height=False)

caixaTexto = Entry(window, font=("Comic Sans MS",30), width=11, bg="black", fg="white")
#caixaTexto = Text(window, height=2, width=37, font=("Comic Sans MS", 10))
caixaTexto.grid(row=0,column=0, columnspan=4)

bApagar = Button(window, text="AC", height=3, width=20, bg="red", fg="white", command=apaga)
bApagar.grid(row=1, column=0, columnspan=2)
bBackspace = Button(window, text="<-", height=3, width=9, bg="blue", fg="white", command=backspace)
bBackspace.grid(row=1, column= 2)

bSete = Button(window, text=("7"), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar(7))
bSete.grid(row=2, column=0)
bOito = Button(window, text=("8"), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar(8))
bOito.grid(row=2, column=1)
bNove = Button(window, text=("9"), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar(9))
bNove.grid(row=2, column=2)
bDividir = Button(window, text=("/"), height=3, width=9, bg="orange", fg="white", command=lambda:Digitar("/"))
bDividir.grid(row=1, column=3)

bQuatro = Button(window, text=("4"), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar(4))
bQuatro.grid(row=3, column=0)
bCinco = Button(window, text=("5"), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar(5))
bCinco.grid(row=3, column=1)
bSeis = Button(window, text=("6"), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar(6))
bSeis.grid(row=3, column=2)
bMultiplicar = Button(window, text=("*"), height=3, width=9, bg="orange", fg="white", command=lambda:Digitar("*"))
bMultiplicar.grid(row=2, column=3)

bUm = Button(window, text=("1"), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar(1))
bUm.grid(row=4, column=0)
bDois = Button(window, text=("2"), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar(2))
bDois.grid(row=4, column=1)
bTres = Button(window, text=("3"), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar(3))
bTres.grid(row=4, column=2)
bSubtrair = Button(window, text=("-"), height=3, width=9, bg="orange", fg="white", command=lambda:Digitar("-"))
bSubtrair.grid(row=3, column=3)

bZero = Button(window, text=("0"), height=3, width=20, bg="gray", fg="white", command=lambda:Digitar(0))
bZero.grid(row=5, column=0, columnspan=2)
bPonto = Button(window, text=("."), height=3, width=9, bg="gray", fg="white", command=lambda:Digitar("."))
bPonto.grid(row=5, column=2)
bMais = Button(window, text=("+"), height=3, width=9, bg="orange", fg="white", command=lambda:Digitar("+"))
bMais.grid(row=4, column=3)
bIgual = Button(window, text=("="), height=3, width=9, bg="orange", fg="white", command=Calcular)
bIgual.grid(row=5, column=3)



window.mainloop()