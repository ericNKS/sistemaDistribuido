# ------------------
# Cliente Socket UDP
# ------------------

print("Eu sou um CLIENTE UDP!")

# Importando a biblioteca
import socket

# Definindo ip e porta
HOST = '192.168.15.187'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor estará escutando

# Criando o socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereco do servidor (Ip e porta)
enderecoServidor = (HOST, PORT)

print("Vou começar a mandar mensagens para o servidor.")

while (True):
	# Aqui começa a conversa
	print('''
		Nome do vendedor
		''')
	nomeVendedor = input("Vendedor > ")
	if nomeVendedor == '5':
		break
	# Enviando mensagem ao servidor
	print("... Vou mandar uma mensagem para o servidor")
	cliente.sendto(nomeVendedor.encode("utf-8"), enderecoServidor)

	# Recebendo resposta do servidor
	msg, endereco = cliente.recvfrom(9000)
	resposta = msg.decode("utf-8")
	print("... O servidor me respondeu:", resposta)

print("... Encerrando o cliente")
cliente.close()
