# -------------------
# Servidor Socket UDP
# -------------------

# importando a biblioteca
import socket
import json

print("Eu sou o SERVIDOR UDP!")

# definindo ip e porta
HOST = '192.168.0.102'  # Endereco IP do Servidor
PORT = 9000              # Porta que o Servidor ficará escutando

# criando o socket e associando ao endereço e porta
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST, PORT))

print("Aguardando cliente...")

# Criando lista da loja

loja = [
	{'codOpe': '1','nomeVendedor': '1','IDLoja': '1','dataVenda': '2022-01-31','valorVenda': '350'},
 	{'codOpe': '1','nomeVendedor': '1','IDLoja': '1','dataVenda': '2022-01-31','valorVenda': '350'},
	{'codOpe': '1','nomeVendedor': '2','IDLoja': '2','dataVenda': '2022-03-10','valorVenda': '350'},
	{'codOpe': '1','nomeVendedor': '2','IDLoja': '2','dataVenda': '2022-03-10','valorVenda': '500'},
 	{'codOpe': '1','nomeVendedor': '3','IDLoja': '3','dataVenda': '2022-07-21','valorVenda': '350'},
	{'codOpe': '1','nomeVendedor': '4','IDLoja': '4','dataVenda': '2022-12-01','valorVenda': '350'}
]


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
		if mensagem_dict['nomeVendedor'] == "" or mensagem_dict['IDLoja'] == "" or int(mensagem_dict['diaVenda']) == 0 or int(mensagem_dict['diaVenda']) > 31 or int(mensagem_dict['mesVenda']) > 12 or int(mensagem_dict['mesVenda']) == 0 or int(mensagem_dict['anoVenda']) <= 1900 or mensagem_dict['valorVenda'] == "":
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
		resposta = "Chegou na parte de ver vendas com um filtro de data"
  
	elif mensagem_dict['codOpe'] == '4g':
		totalVendedor = [
			0,
			0,
			0,
			0
		]
		for vendedor in loja:
			if vendedor['nomeVendedor'] == '1':
				valor_de_venda = float(vendedor['valorVenda'])
				soma = float(totalVendedor[0]) + valor_de_venda
				totalVendedor[0] = soma
			
			if vendedor['nomeVendedor'] == '2':
				valor_de_venda = float(vendedor['valorVenda'])
				soma = float(totalVendedor[1]) + valor_de_venda
				totalVendedor[1] = soma
			
			if vendedor['nomeVendedor'] == '3':
				valor_de_venda = float(vendedor['valorVenda'])
				soma = float(totalVendedor[2]) + valor_de_venda
				totalVendedor[2] = soma
			
			if vendedor['nomeVendedor'] == '4':
				valor_de_venda = float(vendedor['valorVenda'])
				soma = float(totalVendedor[3]) + valor_de_venda
				totalVendedor[3] = soma
    
		index = totalVendedor.index(max(totalVendedor))
		if index == 0:
			resposta = "Lucas foi o melhor vendedor"
		if index == 1:
			resposta = "Joana foi o melhor vendedor"
		if index == 2:
			resposta = "Mateus foi o melhor vendedor"
		if index == 3:
			resposta = "Paula foi o melhor vendedor"
  
	elif mensagem_dict['codOpe'] == '5g':
		totalVendedor = [
			0,
			0,
			0,
			0
		]
		for vendedor in loja:
			if vendedor['IDLoja'] == '1':
				valor_de_venda = float(vendedor['valorVenda'])
				soma = float(totalVendedor[0]) + valor_de_venda
				totalVendedor[0] = soma
			
			if vendedor['IDLoja'] == '2':
				valor_de_venda = float(vendedor['valorVenda'])
				soma = float(totalVendedor[1]) + valor_de_venda
				totalVendedor[1] = soma
			
			if vendedor['IDLoja'] == '3':
				valor_de_venda = float(vendedor['valorVenda'])
				soma = float(totalVendedor[2]) + valor_de_venda
				totalVendedor[2] = soma
			
			if vendedor['IDLoja'] == '4':
				valor_de_venda = float(vendedor['valorVenda'])
				soma = float(totalVendedor[3]) + valor_de_venda
				totalVendedor[3] = soma
    
		index = totalVendedor.index(max(totalVendedor))
		if index == 0:
			resposta = "Pituba foi a melhor loja"
		if index == 1:
			resposta = "Barra foi a melhor loja"
		if index == 2:
			resposta = "Comércio foi a melhor loja"
		if index == 3:
			resposta = "Calçada foi a melhor loja"
     
					
	else:
		print("Mensagem inválida")
		resposta = "ERRO"
  
	
	servidor.sendto(resposta.encode("utf-8"), enderecoCliente)
print("Encerrando o servidor...")
servidor.close()
