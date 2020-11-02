import socket
import random
import math

# parametros de configuração
ip = ('localhost')
porta = 30000
endereço = (ip, porta)

# criando um socket
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind(endereço)
servidor_socket.listen(10)
print('servidor aguardando conexação...')
conexao, cliente = servidor_socket.accept()
print('conectando com o {}'.format(cliente))

# enviando com o servidor para o cliente
# conexao.send(menu.encode('UTF-8'))

# Mesangem que o Servidor vai enviar pro cliente após a conexão entre eles
welcome = 'Bem vindo ao RPG em Texto.\n\n'
conexao.send(welcome.encode('UTF-8'))

# O sevidor enviará uma mensagem de epílogo ao clientee
epilogo = 'Você acorda em uma pequena vila e nela sua aventura vai começar...\n\n'
conexao.send(epilogo.encode('UTF-8'))

#Opções das classes que o cliente pode escolher
classes = 'Antes de começar a aventura você deve escolher uma classe:\n\n' \
          'Guerreiro: Uma classe com dano físico moderado e alta resistência\n' \
          'Mago: Uma classe com alto dano mágico e residência baixa\n' \
          'Ladino: Uma classe com alto dano físico e pouca resistência\n'
conexao.send(classes.encode('UTF-8'))

#Classe escolhida pelo cliente
classe_escolhida = conexao.recv(1024).decode('UTF-8')
if classe_escolhida == 'Mago' or classe_escolhida == 'mago':
    hp_mago = random.randint(12, 14)
    ataque_mago = random.randint(5, 7)
    defesa_mago = random.randint(6, 8)
if classe_escolhida == 'Guerreiro' or classe_escolhida == 'guerreiro':
    hp_guerreiro = random.randint(25, 30)
    ataque_guerreiro = random.randint(12, 14)
    defesa_guerreiro = random.randint(16, 18)
if classe_escolhida == 'Ladino' or classe_escolhida == 'ladino':
    hp_ladino = random.randint(15, 17)
    ataque_ladino = random.randint(18, 20)
    defesa_ladino = random.randint(10, 12)

#Uma mensagem de missão é enviada ao cliente
missão_carta = 'O líder do vilarejo pede para você entregar uma carta' \
               ',esta carta deve ser entregue ao general do Exército Real'
conexao.send(missão_carta.encode('UTF-8'))

conexao.close()