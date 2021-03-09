# Authors: Vitor Figueiredo / Lindrielton Barbosa
# Date: 26/02/2021

import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
from sys import exit

# Inicia a biblioteca Pygame
pygame.init()

# Cria a tela do jogo com resolução de 600 x 600, fixa e com 32bits de cores
display = pygame.display.set_mode((600, 600), 0, 32)
# Adiciona uma imagem de fundo
# bg = pygame.image.load('images/bg.jpg')
# display.blit(bg, [0, 0])

# Adiciona o titulo da janela do jogo
pygame.display.set_caption('Bertie The Brain')

# Musica do jogo
pygame.mixer_music.load('sounds/Tetris Theme A.ogg')
pygame.mixer_music.set_volume(0.00)
pygame.mixer.music.play(-1, 0.0)

# Variaveis fundamentais
status = 'PLAYING' # Para verificar se o tabuleiro estar ativo
time = 'PLAYER1'   # Qual jogador esta jogando no momento
choose = 'X'       # Para definir o x sempre que for o x
tie = 0            # Para quando der empate

# Indices do tabuleiro
board_positions = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

# Função para criar um retangulo na coordenada desejada
# Posição incial, posição final, tamanho innicial, tamanho final
rect1 = Rect((0, 0), (200, 200))
rect2 = Rect((200, 0), (200, 200))
rect3 = Rect((400, 0), (200, 200))
rect4 = Rect((0, 200), (200,200))
rect5 = Rect((200, 200), (200, 200))
rect6 = Rect((400, 200), (200, 200))
rect7 = Rect((0, 400), (200, 200))
rect8 = Rect((200, 400), (200, 200))
rect9 = Rect((400, 400), (200, 200))

# Lista com todos os rects
rec = [
    rect1, rect2, rect3, rect4,
    rect5, rect6, rect7, rect8, rect9,
]

# Função para desenhar o tabuleiro
def design_board():
    # Cria uma linha (tela, cor, posição incial, posição final, espessura da linha)
    pygame.draw.line(display, (255, 255, 255), (200, 0), (200, 600), 10)
    pygame.draw.line(display, (255, 255, 255), (400, 0), (400, 600), 10)
    pygame.draw.line(display, (255, 255, 255), (0, 200), (600, 200), 10)
    pygame.draw.line(display, (255, 255, 255), (0, 400), (600, 400), 10)

# Função para desenhar a peça do jogo
def design_part(pos):
    # importa a variavel 'time'
    global time
    # Descompacta a tupla
    x, y = pos
    # Testa quando for a vez do jogador 2
    if time == 'PLAYER2':
        # Desenha o circulo
        # pygame.draw.circle(display, (0, 0, 255), pos, 50)
        imgO = pygame.image.load('images/o.png').convert_alpha()
        imgT = pygame.transform.scale(imgO, (130, 130))
        display.blit(imgT, (x - 65, y - 65))
    else:
        # Carrega a imagem do 'x'
        img = pygame.image.load('images/x.png').convert_alpha()
        # Rendmensiona a imagem para um tamanho mais adequado
        imgR = pygame.transform.scale(img, (100, 100))
        # Desenha a imagem centralizada no Rect escolhido
        display.blit(imgR, (x - 50, y - 50))

# Função para testar em que posução está
def pos_test():
    # Percorre a matriz de Rects
    for r in rec:
        # Testa se há algum clique do mouse e pega a posição do clique
        if event.type == MOUSEBUTTONDOWN and r.collidepoint(mouse_pos):
            # Verifica em qual rect foi o clique e desenha o 'x' ou o 'o'
            if r == rect1:
                confirm(0, [100, 100])
            if r == rect2:
                confirm(1, [300, 100])
            if r == rect3:
                confirm(2, [500, 100])
            if r == rect4:
                confirm(3, [100, 300])
            if r == rect5:
                confirm(4, [300, 300])
            if r == rect6:
                confirm(5, [500, 300])
            if r == rect7:
                confirm(6, [100, 500])
            if r == rect8:
                confirm(7, [300, 500])
            if r == rect9:
                confirm(8, [500, 500])

# Funçãp que desenha e evita mais de um desenho na mesma posição quando já ocupado
def confirm (indice, pos):
    global choose, time, tie
    if board_positions[indice] == 'X':
        print('X')
    elif board_positions[indice] == 'O':
        print('O')
    else:
        board_positions[indice] = choose
        design_part(pos)
        print(board_positions)
        # Troca a vez de um jogador para o outro
        if time == 'PLAYER1':
            time = 'PLAYER2'
        else:
            time = 'PLAYER1'
        tie += 1

# Função para testar se alguém ganhou o jogo
def game_win(l):
    return ((board_positions[0] == l and board_positions[1] == l and board_positions[2] == l) or
        (board_positions[3] == l and board_positions[4] == l and board_positions[5] == l) or
        (board_positions[6] == l and board_positions[7] == l and board_positions[8] == l) or
        (board_positions[0] == l and board_positions[3] == l and board_positions[6] == l) or
        (board_positions[1] == l and board_positions[4] == l and board_positions[7] == l) or
        (board_positions[2] == l and board_positions[5] == l and board_positions[8] == l) or
        (board_positions[0] == l and board_positions[4] == l and board_positions[8] == l) or
        (board_positions[2] == l and board_positions[4] == l and board_positions[6] == l))

# Menssagem de quando um jogador ganhar
def text_win(w):
    arial = pygame.font.SysFont('arial', 70)
    message = 'JOGADOR {} VENCEU!'.format(w)

    if w == 'TIE':
        Tk().wm_withdraw() #to hide the main window
        messagebox.showinfo('DEU VELHA','O JOGO DEU VELHA!')
        # mens_win = arial.render('DEU VELHA', True, (255, 255, 255), 0)
        # display.blit(mens_win, (115, 265))
    else:
        Tk().wm_withdraw() #to hide the main window
        messagebox.showinfo(message, message)
        # mens_win = arial.render(message, True, (255, 255, 255), 0)
        # display.blit(mens_win, (0, 265))

# Função para resetar o jogo
def reset():
    global choose, status, time, board_positions, tie
    status = 'PLAYING'
    time = 'PLAYER1'
    choose = 'X'
    tie = 0

    board_positions = [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8
    ]
    display.fill(0)

# Loop principal do game
while True:
    # Variavel que guarda e atualiza a posição do mouse atual
    mouse_pos = pygame.mouse.get_pos()
    if status == 'PLAYING':
        design_board()
        # Esse 'for' irá percorrer toda a lista de eventos que o pygame gerar
        for event in pygame.event.get():
            # Verifica se a um evento tipo 'quit' no game
            if event.type == QUIT:
                # Para o pygame
                pygame.quit()
                # Fecha a janela
                exit()
            # Verifica se o botão do mouse foi pressionado
            if event.type == MOUSEBUTTONDOWN:
                if time == 'PLAYER1':
                    choose = 'X'
                    pos_test()
                else:
                    choose = 'O'
                    pos_test()
        # Testa quem foi o ganhador
        if game_win('X'):
            print('X VENCEU')
            text_win('X')
            status = 'RESET'

        elif game_win('O'):
            print('O VENCEU')
            text_win('O')
            status = 'RESET'

        elif tie >= 9:
            print('EMPATE')
            text_win('TIE')
            status = 'RESET'
    
    else:
        for u in pygame.event.get():
            if u.type == QUIT:
                pygame.quit()
                exit()
            if u.type == MOUSEBUTTONDOWN:
                reset()

    pygame.display.flip()