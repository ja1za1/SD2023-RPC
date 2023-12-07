from tkinter import *
from rpc.cliente.Client import Client

CLIENTE = Client('localhost', 38500)

def limpar_frame(frame: Frame):
    for elemento in frame.winfo_children():
        elemento.destroy()

def validar_float(action, valor):
    if action == '1':  
        try:
            float(valor)
            return True
        except ValueError:
            return False
    return True

def validar_int(action, valor):
    if action == '1': 
        try:
            int(valor)
            return True
        except ValueError:
            return False
    return True

def validar_input_cpf(texto):
    return texto == "" or (texto.isdigit() and len(texto) <= 11)


def gerar_layout_divisao(frame_pai):
    label_titulo_divisao = Label(frame_pai, text="Dividir: ")
    label_titulo_divisao.config(foreground="white",bg="#212529", font=("Roboto", 16, "bold"))
    label_titulo_divisao.grid(row = 3, column=0, padx=10, pady=40)

    input_valor1 = frame_pai.register(validar_float)
    input_valor1 = Entry(frame_pai, validate="key", validatecommand=(input_valor1, '%d', '%P'), font=("Roboto", 16, "bold"))
    input_valor1.grid(row=3, column=1, padx=10)

    label_simbolo_divisao = Label(frame_pai, text="/")
    label_simbolo_divisao.config(foreground="white",bg="#212529", font=("Roboto", 24, "bold"))
    label_simbolo_divisao.grid(row = 3, column=2)

    input_valor2 = frame_pai.register(validar_float)
    input_valor2 = Entry(frame_pai, validate="key", validatecommand=(input_valor2, '%d', '%P'), font=("Roboto", 16, "bold"))
    input_valor2.grid(row=3, column=3, padx=10)

    botao_resultado = Button(frame_pai, text="=", font=("Roboto", 12, "bold"), command=lambda: enviar_operacao_mult(input_valor1, input_valor2,label_resultado), width=7, height=2)
    botao_resultado.config(bg="#0d6efd")
    botao_resultado.grid(row=3, column=4, padx=10)

    label_resultado = Label(frame_pai, foreground="white",bg="#212529", text="", font=("Roboto", 12, "bold"))
    label_resultado.grid(row=3, column=5)

def gerar_layout_multiplicacao(frame_pai):
    label_titulo_multiplicacao = Label(frame_pai, text="Multiplicar: ")
    label_titulo_multiplicacao.config(foreground="white",bg="#212529", font=("Roboto", 16, "bold"))
    label_titulo_multiplicacao.grid(row = 2, column=0, padx=10, pady=40)

    input_valor1 = frame_pai.register(validar_float)
    input_valor1 = Entry(frame_pai, validate="key", validatecommand=(input_valor1, '%d', '%P'), font=("Roboto", 16, "bold"))
    input_valor1.grid(row=2, column=1, padx=10)

    label_simbolo_multiplicacao = Label(frame_pai, text="x")
    label_simbolo_multiplicacao.config(foreground="white",bg="#212529", font=("Roboto", 24, "bold"))
    label_simbolo_multiplicacao.grid(row = 2, column=2)

    input_valor2 = frame_pai.register(validar_float)
    input_valor2 = Entry(frame_pai, validate="key", validatecommand=(input_valor2, '%d', '%P'), font=("Roboto", 16, "bold"))
    input_valor2.grid(row=2, column=3, padx=10)

    botao_resultado = Button(frame_pai, text="=", font=("Roboto", 12, "bold"), command=lambda: enviar_operacao_mult(input_valor1, input_valor2,label_resultado), width=7, height=2)
    botao_resultado.config(bg="#0d6efd")
    botao_resultado.grid(row=2, column=4, padx=10)

    label_resultado = Label(frame_pai, foreground="white",bg="#212529", text="", font=("Roboto", 12, "bold"))
    label_resultado.grid(row=2, column=5)

def gerar_layout_subtracao(frame_pai):
    label_titulo_subtracao = Label(frame_pai, text="Subtrair: ")
    label_titulo_subtracao.config(foreground="white",bg="#212529", font=("Roboto", 16, "bold"))
    label_titulo_subtracao.grid(row = 1, column=0, padx=10, pady=40)

    input_valor1 = frame_pai.register(validar_float)
    input_valor1 = Entry(frame_pai, validate="key", validatecommand=(input_valor1, '%d', '%P'), font=("Roboto", 16, "bold"))
    input_valor1.grid(row=1, column=1, padx=10)

    label_simbolo_soma = Label(frame_pai, text="-")
    label_simbolo_soma.config(foreground="white",bg="#212529", font=("Roboto", 24, "bold"))
    label_simbolo_soma.grid(row = 1, column=2)

    input_valor2 = frame_pai.register(validar_float)
    input_valor2 = Entry(frame_pai, validate="key", validatecommand=(input_valor2, '%d', '%P'), font=("Roboto", 16, "bold"))
    input_valor2.grid(row=1, column=3, padx=10)

    botao_resultado = Button(frame_pai, text="=", font=("Roboto", 12, "bold"), command=lambda: enviar_operacao_sub(input_valor1, input_valor2,label_resultado), width=7, height=2)
    botao_resultado.config(bg="#0d6efd")
    botao_resultado.grid(row=1, column=4, padx=10)

    label_resultado = Label(frame_pai, foreground="white",bg="#212529", text="", font=("Roboto", 12, "bold"))
    label_resultado.grid(row=1, column=5)

def gerar_layout_soma(frame_pai):
    label_titulo_soma = Label(frame_pai, text="Somar: ")
    label_titulo_soma.config(foreground="white",bg="#212529", font=("Roboto", 16, "bold"))
    label_titulo_soma.grid(row = 0, column=0, padx=10, pady=40)

    input_valor1 = frame_pai.register(validar_float)
    input_valor1 = Entry(frame_pai, validate="key", validatecommand=(input_valor1, '%d', '%P'), font=("Roboto", 16, "bold"))
    input_valor1.grid(row=0, column=1, padx=10)

    label_simbolo_soma = Label(frame_pai, text="+")
    label_simbolo_soma.config(foreground="white",bg="#212529", font=("Roboto", 24, "bold"))
    label_simbolo_soma.grid(row = 0, column=2)

    input_valor2 = frame_pai.register(validar_float)
    input_valor2 = Entry(frame_pai, validate="key", validatecommand=(input_valor2, '%d', '%P'), font=("Roboto", 16, "bold"))
    input_valor2.grid(row=0, column=3, padx=10)

    botao_resultado = Button(frame_pai, text="=", font=("Roboto", 12, "bold"), command=lambda: enviar_operacao_sum(input_valor1, input_valor2,label_resultado), width=7, height=2)
    botao_resultado.config(bg="#0d6efd")
    botao_resultado.grid(row=0, column=4, padx=10)

    label_resultado = Label(frame_pai, foreground="white",bg="#212529", text="", font=("Roboto", 12, "bold"))
    label_resultado.grid(row=0, column=5)

def gerar_layout_is_prime(frame_pai):
    label_titulo_is_prime = Label(frame_pai, text="Verificar se é primo: ")
    label_titulo_is_prime.config(foreground="white",bg="#212529", font=("Roboto", 16, "bold"))
    label_titulo_is_prime.grid(row = 0, column=0, padx=10, pady=40)

    input_valor1 = frame_pai.register(validar_int)
    input_valor1 = Entry(frame_pai, validate="key", validatecommand=(input_valor1, '%d', '%P'), font=("Roboto", 10, "bold"))
    input_valor1.grid(row=0, column=1, padx=5)

    botao_resultado = Button(frame_pai, text="Checar", font=("Roboto", 12, "bold"), command=lambda: enviar_operacao_is_prime(input_valor1, label_resultado), width=7, height=2)
    botao_resultado.config(bg="#0d6efd")
    botao_resultado.grid(row=0, column=2, padx=10)

    label_resultado = Label(frame_pai, bg="#212529", text="", font=("Roboto", 12, "bold"))
    label_resultado.grid(row=0, column=3)

def gerar_layout_primes_in_range(frame_pai):
    label_titulo_primes_in_range = Label(frame_pai, wraplength=200,text="Primos em range (inclusivo): ")
    label_titulo_primes_in_range.config(foreground="white",bg="#212529", font=("Roboto", 16, "bold"))
    label_titulo_primes_in_range.grid(row = 1, column=0, padx=10, pady=20)

    input_valor1 = frame_pai.register(validar_int)
    input_valor1 = Entry(frame_pai, validate="key", validatecommand=(input_valor1, '%d', '%P'), font=("Roboto", 12, "bold"))
    input_valor1.grid(row=1, column=1, padx=10)

    input_valor2 = frame_pai.register(validar_int)
    input_valor2 = Entry(frame_pai, validate="key", validatecommand=(input_valor2, '%d', '%P'), font=("Roboto", 12, "bold"))
    input_valor2.grid(row=1, column=2, padx=10)

    botao_resultado = Button(frame_pai, text="Verificar primos", font=("Roboto", 12, "bold"), command=lambda: enviar_operacao_primes_in_range(input_valor1, input_valor2,label_resultado), width=14, height=2)
    botao_resultado.config(bg="#0d6efd")
    botao_resultado.grid(row=1, column=3, padx=10)

    label_resultado = Label(frame_pai, foreground="white",bg="#212529", text="", font=("Roboto", 12, "bold"))
    label_resultado.grid(row=2, column=0)

def gerar_layout_contas_basicas(frame_pai):
    limpar_frame(frame_pai)
    gerar_layout_soma(frame_pai)
    gerar_layout_subtracao(frame_pai)
    gerar_layout_multiplicacao(frame_pai)
    gerar_layout_divisao(frame_pai)

def gerar_layout_numeros_primos(frame_pai):
    limpar_frame(frame_pai)
    gerar_layout_is_prime(frame_pai)
    gerar_layout_primes_in_range(frame_pai)

def gerar_layout_noticias(frame_pai):
    limpar_frame(frame_pai)

    label_titulo_noticias = Label(frame_pai, text="Obter notícias: ")
    label_titulo_noticias.config(foreground="white",bg="#212529", font=("Roboto", 16, "bold"))
    label_titulo_noticias.grid(row = 0, column=0, padx=10, pady=40)

    input_valor1 = frame_pai.register(validar_int)
    input_valor1 = Entry(frame_pai, validate="key", validatecommand=(input_valor1, '%d', '%P'), font=("Roboto", 16, "bold"))
    input_valor1.grid(row=0, column=1, padx=10)

    botao_resultado = Button(frame_pai, text="Obter", font=("Roboto", 12, "bold"), command=lambda: enviar_operacao_last_news(input_valor1, label_resultado), width=7, height=2)
    botao_resultado.config(bg="#0d6efd")
    botao_resultado.grid(row=0, column=2, padx=10)

    label_resultado = Label(frame_pai, bg="#212529", text="", font=("Roboto", 12, "bold"))
    label_resultado.grid(row=0, column=3)

def gerar_layout_validar_cpf(frame_pai):
    limpar_frame(frame_pai)

    label_titulo_validar_cpf = Label(frame_pai, text="Validar CPF: ")
    label_titulo_validar_cpf.config(foreground="white",bg="#212529", font=("Roboto", 16, "bold"))
    label_titulo_validar_cpf.grid(row = 0, column=0, padx=10, pady=40)

    input_cpf = frame_pai.register(validar_input_cpf)
    input_cpf = Entry(frame_pai, validate="key", validatecommand=(input_cpf, '%P'), font=("Roboto", 16, "bold"))
    input_cpf.grid(row=0, column=1, padx=10)

    botao_resultado = Button(frame_pai, text="Validar", font=("Roboto", 12, "bold"), command=lambda: enviar_operacao_validate_cpf(input_cpf, label_resultado), width=7, height=2)
    botao_resultado.config(bg="#0d6efd")
    botao_resultado.grid(row=0, column=2, padx=10)

    label_resultado = Label(frame_pai, bg="#212529", text="", font=("Roboto", 12, "bold"))
    label_resultado.grid(row=0, column=3)

def enviar_operacao_sum(input1: Entry, input2: Entry, label_resultado: Label):
    valor1 = input1.get()
    valor2 = input2.get()
    resultado = CLIENTE.sum(valor1 if valor1 != "" else 0, valor2 if valor2 != "" else 0)
    exibir_resultado_dois_inputs(resultado, input1, input2, label_resultado)

def enviar_operacao_sub(input1: Entry, input2: Entry, label_resultado: Label):
    valor1 = input1.get()
    valor2 = input2.get()
    resultado = CLIENTE.sub(valor1 if valor1 != "" else 0, valor2 if valor2 != "" else 0)
    exibir_resultado_dois_inputs(resultado, input1, input2, label_resultado)

def enviar_operacao_mult(input1: Entry, input2: Entry, label_resultado: Label):
    valor1 = input1.get()
    valor2 = input2.get()
    resultado = CLIENTE.mult(valor1 if valor1 != "" else 0, valor2 if valor2 != "" else 0)
    exibir_resultado_dois_inputs(resultado, input1, input2, label_resultado)

def enviar_operacao_div(input1: Entry, input2: Entry, label_resultado: Label):
    valor1 = input1.get()
    valor2 = input2.get()
    resultado = CLIENTE.div(valor1 if valor1 != "" else 0, valor2 if valor2 != "" else 0)
    exibir_resultado_dois_inputs(resultado, input1, input2, label_resultado)

def enviar_operacao_primes_in_range(input1: Entry, input2: Entry, label_resultado: Label):
    valor1 = input1.get().replace(" ", "")
    valor2 = input2.get().replace(" ", "")
    resultado = CLIENTE.show_primes_in_range_mp(valor1 if valor1 != "" else 0, valor2 if valor2 != "" else 0)
    if not resultado:
        resultado = "Nenhum primo encontrado"
        label_resultado.config(foreground="red")
        exibir_resultado_dois_inputs(resultado, input1, input2, label_resultado)
    else:
        exibir_resultado_primes_in_range(resultado, input1, input2,label_resultado)
        
def enviar_operacao_is_prime(input: Entry, label_resultado: Label):
    valor1 = input.get().replace(" ","")
    resultado = CLIENTE.is_prime(valor1 if valor1 != "" else 0)[0]
    print(resultado)
    if resultado == True:
        resultado = "É primo"
        label_resultado.config(foreground="green")
        exibir_resultado_um_input(resultado, input,label_resultado)
    else:
        resultado = "Não é primo"
        label_resultado.config(foreground="red")
        exibir_resultado_um_input(resultado, input,label_resultado)

def enviar_operacao_last_news(input: Entry, label_resultado: Label):
    valor1 = input.get().replace(" ", "")
    resultado = CLIENTE.last_news_if_barbacena(valor1 if valor1 != "" else 0)
    if not resultado:
        resultado = "Nenhuma notícia encontrada"
        label_resultado.config(foreground="red")
        exibir_resultado_um_input(resultado, input, label_resultado)
    else:
        exibir_resultado_last_news(resultado, input, label_resultado)

def enviar_operacao_validate_cpf(input: Entry, label_resultado: Label):
    cpf = input.get()
    if len(cpf) == 11:
        resultado = CLIENTE.validate_cpf(cpf)
        print(resultado)
        if resultado == True:
            resultado = "CPF válido"
            label_resultado.config(foreground="green")
            exibir_resultado_um_input(resultado, input,label_resultado)
        else:
            resultado = "CPF inválido"
            label_resultado.config(foreground="red")
            exibir_resultado_um_input(resultado, input,label_resultado)
    else:
        resultado = "CPF deve ter 11 dígitos"
        label_resultado.config(foreground="red")
        exibir_resultado_um_input(resultado, input,label_resultado)

def exibir_resultado_dois_inputs(resultado, input1: Entry, input2: Entry, label_resultado: Label):
    print("Result:", resultado)
    label_resultado.config(text="")
    label_resultado.config(text=resultado)
    input1.delete(0, END) 
    input2.delete(0, END)

def exibir_resultado_um_input(resultado, input: Entry, label_resultado: Label):
    print("Result:", resultado)
    label_resultado.config(text="")
    label_resultado.config(text=resultado)
    input.delete(0, END)

def exibir_resultado_primes_in_range(resultado, input1: Entry, input2: Entry, label_resultado: Label):
    label_resultado.config(text="")
    resultado = ", ".join(map(str, resultado))
    janela_resultado = Toplevel()
    janela_resultado.title('Resultado')
    Label(janela_resultado, text=f"Números primos entre {input1.get().replace(' ', '')} e {input2.get().replace(' ', '')}: ",font=("Roboto", 12, "bold")).pack()
    Label(janela_resultado, text=resultado, wraplength=500, font=("Roboto", 12,)).pack()
    input1.delete(0, END)
    input2.delete(0, END)

def exibir_resultado_last_news(resultado, input: Entry, label_resultado: Label):
    noticias = ['- ' + noticia for noticia in resultado]
    resultado = "\n".join(noticias)
    
    label_resultado.config(text="")
    janela_resultado = Toplevel()
    janela_resultado.title('Resultado')
    Label(janela_resultado, text=f"Notícias encontradas: ",font=("Roboto", 12, "bold"), anchor='w').pack()
    Label(janela_resultado, text=resultado, wraplength=500, font=("Roboto", 12,)).pack()
    input.delete(0, END)


def main():
    root = Tk()  
    root.title("Cliente RPC")  
    root.config(bg="#212529") 
    root.geometry("1100x600")
    root.minsize(1100,600)
    root.resizable(True, False)

    menu_operacoes = Frame(root)
    menu_operacoes.config(bg="#6c757d")
    menu_operacoes.pack(side="left", fill=BOTH,)

    conteudo_operacoes = Frame(root)
    conteudo_operacoes.config(bg="#212529")
    conteudo_operacoes.pack(side="right", fill=BOTH, expand=True)

    label_titulo_operacoes = Label(menu_operacoes, text="Operações")
    label_titulo_operacoes.config(bg="#6c757d", font=("Roboto", 16, "bold"))
    label_titulo_operacoes.grid(row = 0, column=0, padx=10, pady=10)

    botao_contas_basicas = Button(menu_operacoes, text="Contas básicas", font=("Roboto", 14, "bold"), command=lambda: gerar_layout_contas_basicas(conteudo_operacoes), width=14, height=2)
    botao_contas_basicas.config(bg="#0d6efd")
    botao_contas_basicas.grid(row=1, column=0, padx=10, pady=10)

    botao_numeros_primos = Button(menu_operacoes, text="Números primos", font=("Roboto", 14, "bold"), command=lambda: gerar_layout_numeros_primos(conteudo_operacoes), width=14, height=2)
    botao_numeros_primos.config(bg="#0d6efd")
    botao_numeros_primos.grid(row=2, column=0, padx=10, pady=10)

    botao_noticias = Button(menu_operacoes, text="Notícias", font=("Roboto", 14, "bold"), command=lambda: gerar_layout_noticias(conteudo_operacoes), width=14, height=2)
    botao_noticias.config(bg="#0d6efd")
    botao_noticias.grid(row=3, column=0, padx=10, pady=10)

    botao_validar_cpf = Button(menu_operacoes, text="Validar CPF", font=("Roboto", 14, "bold"), command=lambda: gerar_layout_validar_cpf(conteudo_operacoes), width=14, height=2)
    botao_validar_cpf.config(bg="#0d6efd")
    botao_validar_cpf.grid(row=4, column=0, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()