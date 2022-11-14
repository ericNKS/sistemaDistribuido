# -------------------
# Servidor Socket UDP
# -------------------

# importando a biblioteca
import socket

print("Eu sou o SERVIDOR UDP!")

# definindo ip e porta
HOST = '192.168.0.101'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor ficará escutando


# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST, PORT))

print("Aguardando cliente...")

while (True):
	print("-----")
	# cliente conectou - recuperando informações do cliente
	msg, enderecoCliente = servidor.recvfrom(9000)
	mensagem = msg.splitlines(True)
	for a in mensagem:
		a.replace("b'", "")
		a.replace("\n'", "")
		print(a)
	print(f"Cliente {enderecoCliente} enviou mensagem")
	mensagem = msg.decode("utf-8")
	# tratando a mensagem recebida
	if mensagem == '1':
		print("Cliente pediu frutas")
		resposta = "banana, laranja, abacaxi"
	elif mensagem == '2':
		print("Cliente pediu animais")
		resposta = "gato, cachorro, papagaio"
	elif mensagem == '3':
		print("Cliente pediu objetos")
		resposta = "caneta, sapato, bola"
	else:
		print("Mensagem inválida")
		resposta = "ERRO"
	servidor.sendto(resposta.encode("utf-8"), enderecoCliente)
print("Encerrando o servidor...")
servidor.close()
