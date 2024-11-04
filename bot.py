import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox, simpledialog, Text

# Dicionário com as perguntas editáveis
perguntas = {
    "nome": "Por favor, informe seu nome: ",
    "idade": "Informe sua idade: ",
    "telefone": "Informe seu número de telefone: ",
    "endereco": "Informe seu endereço: ",
    "tipo": "Você será um doador ou receptor de leite materno? ",
    "doacao_local": "Onde você pretende fazer a doação? "
}

def salvar_dados_usuario(nome, idade, telefone, endereco, tipo, doacao_local):
    arquivo_excel = 'usuarios.xlsx'
    if os.path.exists(arquivo_excel):
        df = pd.read_excel(arquivo_excel)
    else:
        df = pd.DataFrame(columns=['Nome', 'Idade', 'Telefone', 'Endereço', 'Tipo', 'Doação Local'])

    dados_usuario = pd.DataFrame({
        'Nome': [nome],
        'Idade': [idade],
        'Telefone': [telefone],
        'Endereço': [endereco],
        'Tipo': [tipo],
        'Doação Local': [doacao_local]
    })
    
    df = pd.concat([df, dados_usuario], ignore_index=True)
    df.to_excel(arquivo_excel, index=False)

def obter_informacoes(topico):
    informacoes = {
        1: "A doação de leite materno traz muitos benefícios para os bebês, como maior imunidade e nutrição.",
        2: "Para se tornar um doador, você deve estar saudável e seguir os critérios estabelecidos pela instituição.",
        3: "Você pode encontrar locais de doação em hospitais, bancos de leite ou organizações locais.",
        4: "A saúde e segurança são prioritárias, e é importante seguir as diretrizes para garantir a qualidade do leite.",
        5: "Existem muitos mitos sobre a doação de leite, como que ela pode prejudicar a saúde da mãe. É importante buscar informações precisas.",
        6: "Você pode fazer a doação em hospitais e bancos de leite. Um exemplo é o Banco de Leite Materno da cidade, que fica localizado na Rua Exemplo, 123, e o telefone para contato é (11) 1234-5678."
    }
    
    return informacoes.get(topico, "Tópico inválido.")

def exibir_informacoes(topico):
    informacao = obter_informacoes(topico)
    messagebox.showinfo("Informação do Tópico", informacao)

def iniciar_chat():
    nome = simpledialog.askstring("Informação", perguntas["nome"])
    idade = simpledialog.askstring("Informação", perguntas["idade"])
    telefone = simpledialog.askstring("Informação", perguntas["telefone"])
    endereco = simpledialog.askstring("Informação", perguntas["endereco"])
    tipo = simpledialog.askstring("Informação", perguntas["tipo"])
    doacao_local = simpledialog.askstring("Informação", perguntas["doacao_local"])

    salvar_dados_usuario(nome, idade, telefone, endereco, tipo, doacao_local)
    messagebox.showinfo("Obrigado", "Seus dados foram salvos com sucesso!")

    while True:
        topicos = {
            1: "Benefícios da doação de leite materno",
            2: "Como se tornar um doador",
            3: "Locais para doação de leite materno",
            4: "Saúde e segurança na doação",
            5: "Mitos e verdades sobre a doação de leite materno",
            6: "Onde posso fazer a doação?"
        }

        escolha = simpledialog.askinteger("Escolha um Tópico", "Digite o número do tópico que deseja saber mais ou '0' para encerrar:\n" + "\n".join([f"{num}. {desc}" for num, desc in topicos.items()]))

        if escolha == 0:
            messagebox.showinfo("Encerramento", "Obrigado por usar o chatbot! Até mais!")
            break

        if escolha in topicos:
            exibir_informacoes(escolha)
        else:
            messagebox.showwarning("Erro", "Por favor, escolha um número válido.")

# Criar a janela principal
root = tk.Tk()
root.title("Chatbot de Doação de Leite Materno")

# Botão para iniciar o chat
botao_iniciar = tk.Button(root, text="Iniciar Chat", command=iniciar_chat)
botao_iniciar.pack(pady=20)

# Iniciar o loop da interface
root.mainloop()
