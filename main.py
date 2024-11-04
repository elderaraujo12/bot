import openai
import pandas as pd
import os

# Configurar a chave da API do OpenAI
openai.api_key = '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'

def salvar_dados_usuario(nome, idade, tipo, endereco, telefone, saude=None):
    # Nome do arquivo CSV onde os dados serão armazenados
    arquivo_csv = 'usuarios.csv'
    
    # Verificar se o arquivo CSV já existe; se não, criar com as colunas adequadas
    if os.path.exists(arquivo_csv):
        df = pd.read_csv(arquivo_csv)
    else:
        df = pd.DataFrame(columns=['Nome', 'Idade', 'Tipo', 'Endereço', 'Telefone', 'Saúde'])

    # Criar um DataFrame com os novos dados do usuário
    dados_usuario = pd.DataFrame({
        'Nome': [nome],
        'Idade': [idade],
        'Tipo': [tipo],
        'Endereço': [endereco],
        'Telefone': [telefone],
        'Saúde': [saude if saude else "N/A"]
    })
    
    # Concatenar o novo DataFrame com o DataFrame existente
    df = pd.concat([df, dados_usuario], ignore_index=True)
    
    # Salvar de volta no CSV
    df.to_csv(arquivo_csv, index=False)

def chat_with_gpt():
    print("Bem-vindo ao Chatbot de Doação de Leite Materno!")
    
    # Coleta de dados do usuário
    nome = input("Para começar, por favor, informe seu nome: ")
    idade = input("Informe sua idade: ")
    tipo = input("Você é um doador ou receptor? ")
    endereco = input("Informe seu endereço: ")
    telefone = input("Informe seu número de telefone: ")
    
    # Coleta do estado de saúde se for um doador
    saude = None
    if tipo.lower() == "doador":
        saude = input("Sua saúde está em dia? (sim/não): ")
    
    # Salvar dados do usuário automaticamente
    salvar_dados_usuario(nome, idade, tipo, endereco, telefone, saude)
    print("\nObrigado! Os dados foram salvos com sucesso.")

    # Mensagem inicial do chatbot
    conversation_history = [
        {"role": "system", "content": "Você é um assistente que ajuda com informações sobre doação de leite materno."}
    ]
    
    # Pergunta inicial do chatbot para iniciar a conversa
    print("Bot: O que você deseja saber sobre o assunto?")
    
    # Loop de conversa com o ChatGPT
    while True:
        user_input = input("Você: ")
        
        if user_input.lower() == "sair":
            print("Encerrando o chatbot. Até logo!")
            break
        
        # Adiciona a entrada do usuário ao histórico da conversa
        conversation_history.append({"role": "user", "content": user_input})
        
        try:
            # Envia a conversa para o ChatGPT e obtém a resposta
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Usando gpt-3.5-turbo
                messages=conversation_history
            )
            
            # Extrair e exibir a resposta do bot
            bot_reply = response.choices[0].message.content
            print("Bot:", bot_reply)
            
            # Adiciona a resposta do bot ao histórico
            conversation_history.append({"role": "assistant", "content": bot_reply})
            
            # Adiciona a resposta do bot ao histórico
            conversation_history.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            print(f"Erro ao se comunicar com a API OpenAI: {e}")
            break

if __name__ == "__main__":
    chat_with_gpt()
