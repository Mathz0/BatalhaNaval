
# 🧩 Jogo Batalha Naval – Cliente/Servidor com TCP

Este é um jogo de **Batalha Naval distribuído**, implementado em **Python** com o modelo **cliente-servidor** usando **socket TCP** para garantir confiabilidade e controle das jogadas em tempo real. Dois jogadores se conectam ao servidor e jogam em turnos, tentando acertar o navio escondido do adversário.

## 🎯 Objetivo

Acertar a posição do navio inimigo em um tabuleiro 5x5. O primeiro jogador a atingir o navio do oponente vence.

## 🚀 Como executar

### 1. Clone o projeto ou baixe os arquivos

```bash
git clone https://github.com/Mathz0/BatalhaNaval.git
```

### 2. Execute o servidor

Abra um terminal:

```bash
python Servidor.py
```

### 3. Execute os clientes (jogador 1 e jogador 2)

Em dois terminais diferentes:

```bash
python Cliente.py  # jogador 1
python Cliente.py  # jogador 2
```

## 🧱 Estrutura do Projeto

- `Servidor.py`: gerencia o jogo, tabuleiros e alternância de turnos.
- `Cliente.py`: permite o jogador interagir com o servidor.
- `README.md`: este arquivo.

## ✅ Requisitos

- **Linguagem:** Python 3.x
- **Módulos utilizados:** `socket`, `random`, `threading` (nativo do Python)
- **Plataforma:** Qualquer SO com terminal (Windows, Linux, Mac)
- **Execução:** 
  - Um terminal para `Servidor.py`
  - Dois terminais para `Cliente.py` (Jogador 1 e Jogador 2)

## 📌 Observações

- O jogo roda em localhost, mas pode ser adaptado para rede local/internet.
    -Para rodar em diferente maquinas (servidor.py em uma e cliente.py em outra ) alterar:

    `Servidor.py`
     ```bash
        server.bind(('localhost', 10000))
    ```
    Para:
    ```bash
        server.bind(('0.0.0.0', 10000))
    ```
    `Cliente.py`
    ```bash
        client.connect(('localhost', 10000))
    ```
    Para:
    ```bash
        client.connect(('192.168.0.10', 10000))
    ```
    - Para obter o IP local do servidor use o comando no terminal:
        - Windows: ipconfig
        - Linux/macOS: ifconfig ou ip a
- Cada jogador só vê suas instruções. O tabuleiro inimigo é oculto.

## 📜 Protocolo de Aplicação

- O jogo segue um protocolo próprio da camada de aplicação.
- Inicia com identificação dos jogadores.
- Jogadas e respostas são trocadas por mensagens como: `"ACERTOU!"`, `"ERROU!"`, `"Você venceu!"`, etc.

## 📡 Arquitetura

- Modelo: Cliente-Servidor
- Protocolo de transporte: TCP/IP
- Quantidade de jogadores: 2
- Modo de jogo: turnos alternados
- Comunicação: texto puro codificado em UTF-8
- Formato de entrada: "linha,coluna" (ex: "2,3")

## 🔄 Fluxo Geral da Comunicação

### 1. Conexão

- O servidor aguarda duas conexões TCP.
- Quando os dois jogadores conectam, o jogo começa.

| Origem   | Destino   | Mensagem                  | Significado          |
| -------- | --------- | ------------------------- | -------------------- |
| Servidor | Cliente 1 | `"Você é o Jogador 1"`    | Identifica o cliente |
| Servidor | Cliente 2 | `"Você é o Jogador 2"`    | Identifica o cliente |

### 2. Inicialização

- O servidor cria dois tabuleiros 5x5 com um navio em posição aleatória para cada jogador.
- Os jogadores não conhecem a posição dos navios.

### 3. Rodadas por Turno

O servidor alterna entre os jogadores e envia:

| Origem   | Destino        | Mensagem                                          | Significado               |
| -------- | -------------- | ------------------------------------------------- | ---------------------     |
| Servidor | Jogador da vez | `"Sua vez! Envie coordenadas (linha,coluna):"`    | Indica que é sua vez      |
| Cliente  | Servidor       | `"x,y"` (ex: `"2,3"`)                             | Jogada enviada            |

### 4. Respostas do Servidor

Após o servidor processar a jogada, ele responde com base no resultado:

| Situação                                      | Mensagem enviada                                |
| --------------------------------------------- | ----------------------------------------------- |
| Acertou o navio                               | `"*BOOM* ACERTOU! Você venceu!"`                |
| Acertado pelo adversário                      | `"Seu navio foi atingido! Jogador X venceu."`   |
| Errou                                         | `"*SPLASH* ERROU!"`                             |
| Coordenada repetida (já jogada)               | `"Ponto já atingido! Tente outro."`             |
| Coordenada fora dos limites                   | `"Coordenada fora do tabuleiro (0-4)."`         |
| Entrada malformada (sem vírgula, texto, etc.) | `"Formato inválido. Use linha,coluna."`         |

### 5. Estado de Vitória

Quando um jogador acerta o navio do outro, o servidor envia mensagens de encerramento para os dois:

| Destinatário       | Mensagem                                      |
| ------------------ | --------------------------------------------- |
| Jogador que venceu | `"*BOOM* ACERTOU! Você venceu!"`              |
| Jogador que perdeu | `"Seu navio foi atingido! Jogador X venceu."` |

O servidor encerra a conexão com ambos os clientes logo após o envio das mensagens de fim de jogo.

## ✅ Propriedades do Protocolo

| Característica                 | Valor                              |
| ------------------------------ | ---------------------------------- |
| Confiabilidade                 | Alta (usa TCP)                     |
| Tipo de protocolo de aplicação | Texto simples (linha-coluna)       |
| Tolerância a erros             | Parcial (verifica formato/limites) |
| Número de clientes             | 2 por partida                      |
| Ordem garantida de mensagens   | Sim (TCP)                          |

## 🚚 Escolha do Protocolo de Transporte – TCP

### ✅ Motivações:
- **Confiabilidade:** o TCP garante que as mensagens cheguem na ordem correta e sem perda.
- **Controle de Fluxo:** evita sobrecarga no envio das jogadas.
- **Facilidade de Implementação:** ideal para jogos por turno, com tráfego baixo e necessidade de confirmação.

### ❌ Nao uso do UDP:
- Não oferece confiabilidade, podendo causar perda ou duplicação de pacotes.
- Requer implementação manual de controle de sessão e retransmissão, o que não é necessário neste projeto.

---

## 🧑🧑‍💻 Autores

Matheus Capuchinho e Gabriel Prado – Redes
