# ------------------
# Vendedor Socket UDP
# ------------------

# Importações
import socket
import json

# Definindo ip e porta
HOST = '192.168.0.102'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor estará escutando

# Criando o socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereco do servidor (Ip e porta)
enderecoServidor = (HOST, PORT)


while (True):
    # Aqui começa a conversa
    print('''
       	*******************
		Codigos de Operação
		1. Realizar Venda
		5. Encerrar Cliente
  		*******************
		''')
    codOpe = input("Digito o codigo de operação: ")
    if codOpe == '5':
        print("Operação cancelada!!")
        break
    mensagem = {
        'codOpe': codOpe,
    }
    while (True):
        print('''Vendedores:
        1 - Lucas 
        2 - Joana
        3- Mateus
        4- Paula''')
        codVend = input("Produto vendido por: (Digite o número): ")

        if int(codVend) > 0 or int(codVend) < 5:
            mensagem['nomeVendedor'] = codVend
            break
        else:
            print("Vendedor inválido")
            
    while (True):
        print('''Lojas:
            1 - Pituba
            2 - Barra
            3- Comércio 
            4- Calçada''')
        codLoja = input('Produto vendido pela loja: (Digite o número da identificação): ')

        if int(codLoja) > 0 or int(codLoja) < 5:
            mensagem['IDLoja'] = codLoja
            break
        else:
            print("Loja inválida")
            
    while (True):
        dataVenda = input("Data da venda (dd/mm/aaaa): ")
        if len(dataVenda) == 10:
            mensagem['diaVenda'] = dataVenda[:2]
            mensagem['mesVenda'] = dataVenda[3:5]
            mensagem['anoVenda'] = dataVenda[6:11]
            break
        else:
            print("O formato da data está errada")
    valueVenda = input("Valor da venda: ")
    mensagem['valorVenda'] = valueVenda
    # Enviando mensagem ao servidor
    # Colocando as resposta em um dicionarios

    
    print(
        f"{mensagem['diaVenda']}/{mensagem['mesVenda']}/{mensagem['anoVenda']}")
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
