import tkinter as tk

def calcular():
    # Obter a entrada do usuário
    n1 = int(entry_n1.get())
    n2 = int(entry_n2.get())
    opcao = int(entry_opcao.get())

    # Realizar o cálculo com base na opção escolhida
    if opcao == 1:
        resultado = n1 + n2
    elif opcao == 2:
        resultado = n1 - n2
    elif opcao == 3:
        resultado = n1 * n2
    elif opcao == 4:
        try:
            resultado = n1 / n2
        except ZeroDivisionError:
            resultado = "Não é possível dividir por zero."
    elif opcao == 5:
        resultado = (n1 * n2) / 100

    # Exibir o resultado na janela
    label_resultado.config(text="Resultado: {}".format(resultado))

def reiniciar():
    entry_n1.delete(0, tk.END)
    entry_n2.delete(0, tk.END)
    entry_opcao.delete(0, tk.END)
    label_resultado.config(text="")
    
janela = tk.Tk()
janela.title("Calculadora")

# Frame de boas-vindas
boas_vindas_frame = tk.Frame(janela)
boas_vindas_frame.pack()

nome_label = tk.Label(boas_vindas_frame, text="Olá!\nQual o seu nome?")
nome_label.pack(side=tk.LEFT, padx=10)

nome_entry = tk.Entry(boas_vindas_frame)
nome_entry.pack(side=tk.LEFT)

def cumprimentar():
    nome = nome_entry.get()
    if nome == "Anderson":
        mensagem = f"Bem vindo novamente, {nome}!"
    else:
        mensagem = f"Prazer em conhece-lo, {nome}!\nEm que posso ajudar?"
    boas_vindas_label.config(text=mensagem)

boas_vindas_botao = tk.Button(boas_vindas_frame, text="OK", command=cumprimentar)
boas_vindas_botao.pack(side=tk.LEFT)

boas_vindas_label = tk.Label(janela, text="")
boas_vindas_label.pack(pady=10)

# Frame de cálculo
calculo_frame = tk.Frame(janela)
calculo_frame.pack()

tk.Label(calculo_frame, text="Digite os números e escolha a operação:").pack(padx=10, pady=10)

label_opcao = tk.Label(calculo_frame, text="Escolha a opção desejada:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 5 - Porcentagem")
label_opcao.pack()
entry_opcao = tk.Entry(calculo_frame)
entry_opcao.pack()


n1_label = tk.Label(calculo_frame, text="Primeiro número:")
n1_label.pack(side=tk.LEFT, padx=10)

entry_n1 = tk.Entry(calculo_frame)
entry_n1.pack(side=tk.LEFT)

n2_label = tk.Label(calculo_frame, text="Segundo número:")
n2_label.pack(side=tk.LEFT, padx=10)

entry_n2 = tk.Entry(calculo_frame)
entry_n2.pack(side=tk.LEFT)

opc_label = tk.Label(calculo_frame, text="Operação:")
opc_label.pack(side=tk.LEFT, padx=10)

entry_opcao = tk.Entry(calculo_frame)
entry_opcao.pack(side=tk.LEFT)

calcular_botao = tk.Button(calculo_frame, text="Calcular", command=calcular)
calcular_botao.pack(side=tk.LEFT, padx=10)

label_resultado = tk.Label(calculo_frame, text="")
label_resultado.pack(pady=10)

# Botão de reinício
reiniciar_botao = tk.Button(janela, text="Reiniciar", command=reiniciar)
reiniciar_botao.pack(pady=10)

janela.mainloop()
