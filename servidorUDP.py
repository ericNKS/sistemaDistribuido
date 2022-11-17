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
		# Conferindo se tem algum item vazio
		if mensagem_dict['nomeVendedor'] == "" or mensagem_dict['IDLoja'] == "" or mensagem_dict['dataVenda'] == "" or mensagem_dict['valorVenda'] == "":
			resposta = "ERRO"
		else:
			loja.append(mensagem_dict)
			resposta = "OK"
	elif mensagem_dict['codOpe'] == '1g':
		if len(loja) != 0:
			vendaTotal = 0.0
			resposta = "Vendedor não encontrado" # Resposta padrão para o cliente
			for venda in loja:
				if venda['nomeVendedor'] == mensagem_dict['nomeVendedor']:
					vendaTotal = vendaTotal + float(venda['valorVenda'])
					resposta = f"R${vendaTotal} vendido" # Resposta caso encontre o vendedor
		else:
			resposta = "Nenhuma venda realizada"
   
	elif mensagem_dict['codOpe'] == '2g':
		if len(loja) != 0:
			vendaTotal = 0.0
			resposta = "Loja não encontrada" # Resposta padrão para o cliente
			for venda in loja:
				if venda['IDLoja'] == mensagem_dict['IDLoja']:
					vendaTotal = vendaTotal + float(venda['valorVenda'])
					resposta = f"R${vendaTotal} vendido" # Resposta caso encontre a loja
		else:
			resposta = "Nenhuma venda realizada"
   
	elif mensagem_dict['codOpe'] == '3g':
		for a in loja:
			print(a)
	else:
		print("Mensagem inválida")
		resposta = "ERRO"
  
	
	servidor.sendto(resposta.encode("utf-8"), enderecoCliente)
print("Encerrando o servidor...")
servidor.close()
