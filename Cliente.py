import socket
import math
ip_servidor = 'localhost'
porta = 30000
endereco = (ip_servidor, porta)
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Conectando com o servidor...')
cliente_socket.connect(endereco)

# mensagem = input('Digite a mensagem que vai ser enviada: ')
# cliente_socket.send(mensagem.encode('UTF-8'))

# mensagem de boas vindas
welcome = cliente_socket.recv(1024).decode('UTF-8')
print('{}'.format(welcome))

# mensagem de epílogo da história
epilogo = cliente_socket.recv(1024).decode('UTF-8')
print('{}'.format(epilogo))

#Opções de classes que o cliente possui
classes = cliente_socket.recv(1024).decode('UTF-8')
print('{}'.format(classes))

#Classe escolhida pelo cliente
escolha_classe = str(input('Insira a classe de sua escolha: '))
cliente_socket.send(escolha_classe.encode('UTF-8'))

#uma mensagem de missão é recebida pelo servidor
missão_carta = cliente_socket.recv(1024).decode('UTF-8')
print('{}'.format(missão_carta))

cliente_socket.close()