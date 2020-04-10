# Importando libs e iniciando jogo
import pygame
from paddle import Paddle

pygame.init()

#Definindo cores
BLACK = (0,0,0)
WHITE = (255,255,255)


# Abrindo janela
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong v1")

# Configuração dos paddles
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# Lista de todos os sprites (elementos graficos) que utilizaremos no jogo
all_sprites_list = pygame.sprite.Group()

# Adicionando os paddles a esta lista de elementos graficos
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

# Bool para continuar o jogo até o fechamento da janela
carryOn = True

# O clock será utilizado para controlar  a velocidade dos refreshes de tela
clock = pygame.time.Clock()

# Loop principal
while carryOn:
    # --- Loop de evento principal
    for event in pygame.event.get():  # Observa comandos do usuario
        if event.type == pygame.QUIT:  # Se o usuário sai do jogo
            carryOn = False  # Muda a flag para Falso e sai do jogo
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Pressionando q o usuário sairá do jogo
                carryOn = False

    # --- Lógica do jogo
    all_sprites_list.update()

    # --- Desenho do jogo
    # Primeiro,atualiza tela para black.
    screen.fill(BLACK)
    # Desenha as bordas
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # desenha todos os sprites de uma vez.
    all_sprites_list.draw(screen)

    # --- Atualiza a tela com os novos eventos que ocorreram
    pygame.display.flip()

    # --- Limite de 60 frames por segundo
    clock.tick(60)

# Uma vez que saimos do loop principal, podemos parar a engine do jogo:
pygame.quit()