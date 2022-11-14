# ------------------
# Cliente Socket UDP
# ------------------

print("Eu sou um CLIENTE UDP!")

# Importando a biblioteca
import socket

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
		Escolha:
		1. Total de vendas de um vendedor
		2. Total de vendas de uma loja
		3. Total de vendas da rede de lojas em um período 
		4. Melhor vendedor
		5. Melhor loja
		6. Encerrar cliente
		''')
	mensagem = input("Pedido > ")
	if mensagem == '6':
		break
	# Enviando mensagem ao servidor
	print("... Vou mandar uma mensagem para o servidor")
	cliente.sendto(mensagem.encode("utf-8"), enderecoServidor)

	# Recebendo resposta do servidor
	msg, endereco = cliente.recvfrom(9000)
	resposta = msg.decode("utf-8")
	print("... O servidor me respondeu:", resposta)

print("... Encerrando o cliente")
cliente.close()
