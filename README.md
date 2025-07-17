
# 🧩 Jogo Batalha Naval – Cliente/Servidor com TCP

Este é um jogo de **Batalha Naval distribuído**, implementado em **Python** com o modelo **cliente-servidor** usando **socket TCP**. Dois jogadores se conectam ao servidor e jogam em turnos, tentando acertar o navio escondido do adversário.

## 🎯 Objetivo

Acertar a posição do navio inimigo em um tabuleiro 5x5. O primeiro jogador a atingir o navio do oponente vence.

## 🚀 Como executar

### 1. Clone o projeto ou baixe os arquivos

```bash
git clone <repositorio-ou-baixe-os-arquivos>
```

### 2. Execute o servidor

Abra um terminal:

```bash
python servidor.py
```

### 3. Execute os clientes (jogador 1 e jogador 2)

Em dois terminais diferentes:

```bash
python cliente.py  # jogador 1
python cliente.py  # jogador 2
```

## 🔗 Comunicação

- As mensagens são trocadas entre servidor e cliente usando **texto puro UTF-8**.
- As jogadas são enviadas no formato: `"linha,coluna"` (exemplo: `"2,3"`).

## 🧱 Estrutura do Projeto

- `servidor.py`: gerencia o jogo, tabuleiros e alternância de turnos.
- `cliente.py`: permite o jogador interagir com o servidor.
- `README.md`: este arquivo.
- Protocolo da camada de aplicação: incluído na documentação.

## 📜 Protocolo de Comunicação

- O jogo segue um protocolo próprio da camada de aplicação.
- Inicia com identificação dos jogadores.
- Jogadas e respostas são trocadas por mensagens como: `"ACERTOU!"`, `"ERROU!"`, `"Você venceu!"`, etc.

## ✅ Requisitos

- Python 3.x
- Terminal

## 📌 Observações

- O jogo roda em localhost, mas pode ser adaptado para rede local/internet.
- Cada jogador só vê suas instruções. O tabuleiro inimigo é oculto.

## 🧑‍💻 Autor

Matheus – Projeto de Sistemas Distribuídos / Redes
