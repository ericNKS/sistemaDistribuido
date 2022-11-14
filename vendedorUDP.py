# ------------------
# Vendedor Socket UDP
# ------------------

# Importações
import socket
import json

# Definindo ip e porta
HOST = '192.168.0.101'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor estará escutando

# Criando o socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define o endereco do servidor (Ip e porta)
enderecoServidor = (HOST, PORT)


while (True):
	# Aqui começa a conversa
	# Pegando nome do vendedor
	nomeVendedor = input("Digite seu nome, vendedor: ")
	IDLoja = input("Digite a identificação da loja: ")
	dataVenda = input("Data da venda (dd/mm/aaaa): ")
	valueVenda = input("Valor da venda: ")
	print("*************************")
	print("Codigo de Operação")
	print("1 - Venda")
	print("5 - Cancelar")
	print("*************************")
	codOpe = input("Digito o codigo de operação: ")
	if codOpe == '5':
		print("Operação cancelada!!")
		break
	# Enviando mensagem ao servidor
	# Colocando as resposta em um dicionarios
 
	mensagem = {
		'codOpe': codOpe,
		'nomeVendedor': nomeVendedor,
		'IDLoja': IDLoja,
		'dataVenda': dataVenda,
		'valueVenda': valueVenda,
	}
	msgJson = json.dumps(mensagem)
	print(msgJson)
	#print("... Vou mandar uma mensagem para o servidor")
	cliente.connect(enderecoServidor)
	cliente.sendall(bytes(msgJson,encoding="utf-8"))

	# Recebendo resposta do servidor
	msg, endereco = cliente.recvfrom(9000)
	resposta = msg.decode("utf-8")
	print("... O servidor me respondeu:", resposta)

print("... Encerrando o cliente")
cliente.close()
