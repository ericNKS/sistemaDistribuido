# ------------------
# Cliente Socket UDP
# ------------------

import json
import socket
print("Eu sou um CLIENTE UDP!")

# Importando a biblioteca

# Definindo ip e porta
HOST = '192.168.0.101'  # Endereco IP do Servidor
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
		3. Total de vendas em um período
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
        print('''Vendedores:
		1 - Lucas
		2 - Joana
		3- Mateus
		4- Paula''')
        codVend = input('Digite o número do vendedor: ')
        mensagem['nomeVendedor'] = codVend
    if codOpe == '2':
        while (True):
            print('''Lojas:
            1 - Pituba
            2 - Barra
            3- Comércio 
            4- Calçada''')
            codLoja = input('Digite a identificação da loja: ')
        
            if codLoja > 0 or codLoja < 5:
                mensagem['IDLoja'] = codLoja
                break
            else:
                print("Loja inválida")
    if codOpe == '3':
        while (True):
            dataInicial = input(
                'Digite a data inicial de procura (dd/mm/aaaa): ')
            dataFinal = input('Digite a data final de procura (dd/mm/aaaa): ')
            if len(dataInicial) == 10 and len(dataFinal) == 10:
                # Data inicial
                diaInicial = dataInicial[0] + dataInicial[1]
                mesInicial = dataInicial[3] + dataInicial[4]
                anoInicial = dataInicial[6] + dataInicial[7] + \
                    dataInicial[8] + dataInicial[9]
                mensagem['dataInicial'] = f"{anoInicial}-{mesInicial}-{diaInicial}"
                # Data final
                diaFinal = dataFinal[0] + dataFinal[1]
                mesFinal = dataFinal[3] + dataFinal[4]
                anoFinal = dataFinal[6] + dataFinal[7] + \
                    dataFinal[8] + dataFinal[9]
                mensagem['dataFinal'] = f"{anoFinal}-{mesFinal}-{diaFinal}"
                break
            else:
                print("Formato de uma das datas está errada")
    elif codOpe == '6':
        break

    # Enviando mensagem ao servidor

    msgJson = json.dumps(mensagem)
    print(msgJson)
    #print("... Vou mandar uma mensagem para o servidor")
    cliente.connect(enderecoServidor)
    cliente.sendall(bytes(msgJson, encoding="utf-8"))

    # Recebendo resposta do servidor
    msg, endereco = cliente.recvfrom(9000)
    resposta = msg.decode("utf-8")
    print("... O servidor me respondeu:", resposta)

print("... Encerrando o cliente")
cliente.close()
