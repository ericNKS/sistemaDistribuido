# ------------------
# Cliente Socket UDP
# ------------------

import json
import socket
print("Eu sou um CLIENTE UDP!")

# Importando a biblioteca

# Definindo ip e porta
HOST = '192.168.0.102'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor estará escutando

# Criando o socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereco do servidor (Ip e porta)
enderecoServidor = (HOST, PORT)

print("Vou começar a mandar mensagens para o servidor.")

while (True):
    # Aqui começa a conversa
    print('''
       	*************************************************
		Codigos de Operação
		1. Total de vendas de um vendedor
		2. Total de vendas de uma loja
		3. Total de vendas em um período de ano
		4. Melhor vendedor
		5. Melhor loja
		6. Encerrar cliente
  		*************************************************
		''')
    codOpe = input(
        "Digito o codigo de operação: ")  # Colocando as resposta em um dicionarios
    mensagem = {
        'codOpe': codOpe + "g",
    }
    if codOpe == '1':
        while(True):
            print('''Vendedores:
            1 - Lucas
            2 - Joana
            3- Mateus
            4- Paula''')
            codVend = input('Digite o número do vendedor: ')
            if int(codVend) > 0 and int(codVend) < 5:
                mensagem['nomeVendedor'] = codVend
                break
            else:
                print("Vendedor inválido")
    if codOpe == '2':
        while (True):
            print('''Lojas:
            1 - Pituba
            2 - Barra
            3- Comércio 
            4- Calçada''')
            codLoja = input('Digite a identificação da loja: ')
        
            if int(codLoja) > 0 and int(codLoja) < 5:
                mensagem['IDLoja'] = codLoja
                break
            else:
                print("Loja inválida")
    if codOpe == '3':
        while (True):
            dataInicial = input(
                'Digite o ano inicial de procura: ')
            dataFinal = input('Digite o ano final de procura: ')
            if len(dataInicial) == 4 and len(dataFinal) == 4:
                # Data inicial
                mensagem['dataInicial'] = dataInicial
                # Data final
                mensagem['dataFinal'] = dataFinal
                break
            else:
                print("O ano esta errado")
    elif codOpe == '6':
        break

    # Enviando mensagem ao servidor

    msgJson = json.dumps(mensagem)
    #print("... Vou mandar uma mensagem para o servidor")
    cliente.connect(enderecoServidor)
    cliente.sendall(bytes(msgJson, encoding="utf-8"))

    # Recebendo resposta do servidor
    msg, endereco = cliente.recvfrom(9000)
    resposta = msg.decode("utf-8")
    print("... O servidor me respondeu:", resposta)

print("... Encerrando o cliente")
cliente.close()
