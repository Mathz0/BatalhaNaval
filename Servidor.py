import socket
from random import randint

# Função para criar tabuleiro com navio aleatório
def criar_tabuleiro():
    x, y = randint(0, 4), randint(0, 4)
    tabuleiro = [["~"] * 5 for _ in range(5)]
    tabuleiro[x][y] = "N"
    return tabuleiro, (x, y)

# Criação do socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 10000))
server.listen(2)

print("Servidor aguardando 2 jogadores para iniciar o jogo...")

# Aceita conexões dos dois jogadores
conn1, addr1 = server.accept()
print(f"Jogador 1 conectado de {addr1}")
conn1.sendall("Você é o Jogador 1".encode())

conn2, addr2 = server.accept()
print(f"Jogador 2 conectado de {addr2}")
conn2.sendall("Você é o Jogador 2".encode())

# Cria tabuleiros dos dois jogadores
tabuleiro1, navio1 = criar_tabuleiro()
tabuleiro2, navio2 = criar_tabuleiro()

# Inicia o jogo com jogador 1
jogador_atual = 1
vencedor = None

# Loop do jogo
while not vencedor:
    # Define jogador da vez e oponente
    if jogador_atual == 1:
        conn = conn1
        adversario_tabuleiro = tabuleiro2
        adversario_navio = navio2
        nome = "Jogador 1"
    else:
        conn = conn2
        adversario_tabuleiro = tabuleiro1
        adversario_navio = navio1
        nome = "Jogador 2"

    # Solicita jogada
    conn.sendall("Sua vez! Envie coordenadas (linha,coluna):".encode())
    dados = conn.recv(1024)
    if not dados:
        break
    try:
        x, y = map(int, dados.decode().split(','))
    except:
        conn.sendall("❌ Formato inválido. Use linha,coluna.".encode())
        continue

    # Verifica jogada
    if 0 <= x < 5 and 0 <= y < 5:
        if adversario_tabuleiro[x][y] == "N":
            adversario_tabuleiro[x][y] = "X"
            conn.sendall("*BOOM* ACERTOU! Você venceu!".encode())
            if jogador_atual == 1:
                conn2.sendall("Seu navio foi atingido! Jogador 1 venceu.".encode())
            else:
                conn1.sendall("Seu navio foi atingido! Jogador 2 venceu.".encode())
            vencedor = jogador_atual
            break
        elif adversario_tabuleiro[x][y] == "X":
            conn.sendall("Ponto já atingido! Tente outro.".encode())
            continue
        else:
            adversario_tabuleiro[x][y] = "O"
            conn.sendall("*SPLASH* ERROU!".encode())
    else:
        conn.sendall("Coordenada fora do tabuleiro (0-4).".encode())
        continue

    # Alterna jogador
    jogador_atual = 2 if jogador_atual == 1 else 1

# Encerra conexões
conn1.close()
conn2.close()
server.close()
print("Jogo encerrado. Obrigado por jogar!")