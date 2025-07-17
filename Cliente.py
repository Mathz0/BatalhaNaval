import socket

# Conecta ao servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 10000))

# Recebe identificação do servidor (Jogador 1 ou 2)
identificacao = cliente.recv(1024).decode()
print(identificacao)

try:
    while True:
        # Aguarda instrução do servidor
        mensagem = cliente.recv(1024).decode()
        print(mensagem)

        # Se o jogo acabou, sai do loop
        if "venceu" in mensagem or "atingido" in mensagem:
            break

        if "Sua vez" in mensagem:
            jogada = input("Coordenada (linha,coluna): ")
            cliente.sendall(jogada.encode())

except KeyboardInterrupt:
    print("\nEncerrando jogo...")

cliente.close()
