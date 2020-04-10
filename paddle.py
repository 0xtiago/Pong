import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    # Essa classe representa o paddle, derivando da classe Sprite

    def __init__(self, color, width, height):
        # Chama o construtor da classe pai (Sprite)
        super().__init__()

        # Configura a cor do paddle, sua posição x e y, largura e altura.
        # Configura a cor do fundo and e configura para ser transparente
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Denenha o paddle, que nada mais é do que um retangulo
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Busque o objeto retangular que tenha as dimensões da imagem.
        self.rect = self.image.get_rect()