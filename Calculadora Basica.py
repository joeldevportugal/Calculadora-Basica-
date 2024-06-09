from tkinter import *
from tkinter import messagebox

# Funções para a lógica da calculadora -----------------------------------------------------------------
def btn_click(item):
    current = EResultado.get()
    EResultado.delete(0, END)
    EResultado.insert(0, current + str(item))

def Autor():
    messagebox.showinfo("Autor","Autor: Dev Joel 2024 ©\n"+"Pais:Portugal\n"+"Idade:32\n")

def clear():
    EResultado.delete(0, END)

def backspace():
    current = EResultado.get()
    EResultado.delete(0, END)
    EResultado.insert(0, current[:-1])

def calculate():
    expression = EResultado.get()
    try:
        # Substituir 'X' por '*' e ',' por '.'
        expression = expression.replace('X', '*').replace(',', '.')
        # Converter porcentagens
        if '%' in expression:
            # Substituir todas as ocorrências de números seguidos de '%' por sua forma decimal
            while '%' in expression:
                # Encontrar a posição do '%'
                index = expression.index('%')
                # Encontrar o início do número antes do '%'
                start = index - 1
                while start >= 0 and (expression[start].isdigit() or expression[start] == '.'):
                    start -= 1
                # Corrigir o início (para incluir o dígito inicial)
                start += 1
                # Substituir a porcentagem pela divisão por 100
                number = float(expression[start:index]) / 100
                expression = expression[:start] + str(number) + expression[index + 1:]
        result = eval(expression)
        result = round(result, 3)  # Arredondar o resultado a 3 casas decimais
        EResultado.delete(0, END)
        EResultado.insert(0, str(result).replace('.', ','))
    except Exception as e:
        EResultado.delete(0, END)
        EResultado.insert(0, "Erro")

#-------------------------------------------------------------------------------------------------------
# Definir cores a usar --------------------------------------------------------------------------------
co0 = "#F5EFE6"  # cor Cinzento para Janela 
co1 = "#E8E6D4"  # cor Cinza carregado Botões 
# -----------------------------------------------------------------------------------------------------
janela = Tk()
janela.geometry('290x360+100+100')
janela.resizable(False, False)
janela.title('Calculadora dev Joel ©')
janela.config(bg=co0)
janela.iconbitmap('C:\\Users\\HP\\Desktop\\Python\\calculadora\\icon\\icon.ico')
#------------------------------------------------------------------------------------------------------
# Criar o front-end de uma calculadora ---------------------------------------------------------------
EResultado = Entry(janela, width=14, font=('arial 25'), justify=RIGHT)
EResultado.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
#-------------------------------------------------------------------------------------------------------
# Criar os botões ---------------------------------------------------------------------------------------
button_config = {"font": ("Arial 14 bold"), "relief": RAISED, "overrelief": RIDGE, "width": 4, "bg": co1}

BtnModulo = Button(janela, text='%', **button_config, command=lambda: btn_click('%'))
BtnModulo.grid(row=1, column=0, padx=5, pady=5)
Btnclear = Button(janela, text='C', **button_config, command=clear)
Btnclear.grid(row=1, column=1, padx=5, pady=5)
BtnBack = Button(janela, text='⌫', font=("Arial 14 bold"), relief=RAISED, overrelief=RIDGE, width=10, bg=co1, command=backspace)
BtnBack.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

Btnsete = Button(janela, text='7', **button_config, command=lambda: btn_click(7))
Btnsete.grid(row=2, column=0, padx=5, pady=5)
Btnoito = Button(janela, text='8', **button_config, command=lambda: btn_click(8))
Btnoito.grid(row=2, column=1, padx=5, pady=5)
Btnove = Button(janela, text='9', **button_config, command=lambda: btn_click(9))
Btnove.grid(row=2, column=2, padx=5, pady=5)
BtnDiv = Button(janela, text='/', **button_config, command=lambda: btn_click('/'))
BtnDiv.grid(row=2, column=3, padx=5, pady=5)

BtnQuatro = Button(janela, text='4', **button_config, command=lambda: btn_click(4))
BtnQuatro.grid(row=3, column=0, padx=5, pady=5)
Btncinco = Button(janela, text='5', **button_config, command=lambda: btn_click(5))
Btncinco.grid(row=3, column=1, padx=5, pady=5)
Btnseis = Button(janela, text='6', **button_config, command=lambda: btn_click(6))
Btnseis.grid(row=3, column=2, padx=5, pady=5)
BtnMul = Button(janela, text='X', **button_config, command=lambda: btn_click('X'))
BtnMul.grid(row=3, column=3, padx=5, pady=5)

BtnUm = Button(janela, text='1', **button_config, command=lambda: btn_click(1))
BtnUm.grid(row=4, column=0, padx=5, pady=5)
BtnDois = Button(janela, text='2', **button_config, command=lambda: btn_click(2))
BtnDois.grid(row=4, column=1, padx=5, pady=5)
BtnTres = Button(janela, text='3', **button_config, command=lambda: btn_click(3))
BtnTres.grid(row=4, column=2, padx=5, pady=5)
BtnSub = Button(janela, text='-', **button_config, command=lambda: btn_click('-'))
BtnSub.grid(row=4, column=3, padx=5, pady=5)

BtnZero = Button(janela, text='0', **button_config, command=lambda: btn_click(0))
BtnZero.grid(row=5, column=0, padx=5, pady=5)
BtnPonto = Button(janela, text=',', **button_config, command=lambda: btn_click(','))
BtnPonto.grid(row=5, column=1, padx=5, pady=5)
BtnIgual = Button(janela, text='=', **button_config, command=calculate)
BtnIgual.grid(row=5, column=2, padx=5, pady=5)
BtnSoma = Button(janela, text='+', **button_config, command=lambda: btn_click('+'))
BtnSoma.grid(row=5, column=3, padx=5, pady=5)

BtnAutor = Button(janela, text='Autor', relief=RAISED, overrelief=RIDGE, font=('arial 14 bold'), width=21, bg=co1, command=Autor)
BtnAutor.place(x=5, y=310)
#------------------------------------------------------------------------------------------------------
janela.mainloop()
