# -------------------
# Servidor Socket UDP
# -------------------

# importando a biblioteca
import socket
import json

print("Eu sou o SERVIDOR UDP!")

# definindo ip e porta
HOST = '192.168.0.101'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor ficará escutando

# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST, PORT))

print("Aguardando cliente...")

# Criando lista da loja

loja = []

while (True):
	print("-----")
	# cliente conectou - recuperando informações do cliente
	msg, enderecoCliente = servidor.recvfrom(9000)
	print(f"Cliente {enderecoCliente} enviou mensagem")
	mensagem = msg.decode("utf-8")
	print(mensagem)
	mensagem_dict = json.loads(mensagem)
	
	# tratando a mensagem recebida
	if mensagem_dict['codOpe'] == '1':
		loja.append(mensagem_dict)
		resposta = "OK"
	elif mensagem_dict['codOpe'] == '2':
		print("Cliente pediu animais")
		resposta = "gato, cachorro, papagaio"
	elif mensagem_dict['codOpe'] == '3':
		print("Cliente pediu objetos")
		resposta = "caneta, sapato, bola"
	else:
		print("Mensagem inválida")
		resposta = "ERRO"
	print(len(loja))
	servidor.sendto(resposta.encode("utf-8"), enderecoCliente)
print("Encerrando o servidor...")
servidor.close()
