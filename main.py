import pygame
import random

largura = 1000
largura_obstaculo = 2000
altura_obstaculo = 500
altura = 500
frames = 60
# posição do solo
solo = 220
# Campo utilizado para manipular a velocidade do cenário
velocidade_mapa = 2


# Manipulação do obstaculo na base inferior da tela
class Cano(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = 270, largura_obstaculo + random.randint(0, 1000)

    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)

    def mover(self):
        self.rect.move_ip(-velocidade_mapa, 0)

    def recriar(self):
        if self.rect.left < -400:
            self.rect.top, self.rect.left = 270, largura_obstaculo + random.randint(
                0, 2000
            )


class Player(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (solo, 100)

    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)

    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)


def colisao(player, rect):
    if player.rect.colliderect(rect):
        return True
    else:
        return False


def main(frames):
    pygame.init()
    pygame.font.init()
    # pygame.mixer.init()
    # pygame.mixer.music.load('Top Gear.mp3')
    # pygame.mixer.music.play(loops=-1)
    # pygame.mixer.music.set_volume(0.05)

    font = pygame.font.SysFont(None, 70)
    tela = pygame.display.set_mode([largura, altura])

    relogio = pygame.time.Clock()

    img_girl = pygame.transform.scale(
        pygame.image.load("src/girl.png").convert(), (200, 200)
    )
    img_girl.set_colorkey((0, 0, 0))
    jogador = Player(img_girl)

    img_fundo1 = pygame.image.load("src/fundo.png").convert_alpha()
    img_fundo2 = pygame.image.load("src/fundo.png").convert_alpha()
    img_fundo1 = pygame.transform.scale(img_fundo1, (largura, altura))
    img_fundo2 = pygame.transform.scale(img_fundo2, (largura, altura))
    cano = pygame.transform.scale(
        pygame.image.load("src/fire.png").convert(), (100, 100)
    )

    cano.set_colorkey((0, 0, 0))
    vx, vy = 0, 0
    velocidade = 20
    uppress = False
    sair = False
    x = 0
    y = largura
    cano = Cano(cano)
    pontos = 0
    while sair is False:
        if int(pontos) % 50 == 0:
            frames += 1
        pontos += 0.1
        cano.recriar()

        y -= velocidade_mapa
        x -= velocidade_mapa
        if x == -largura:
            x = largura
        if y == -largura:
            y = largura

        if jogador.rect.top < solo:
            vy += 1
        elif jogador.rect.top >= solo:
            vy = 0
            jogador.rect.top = solo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and jogador.rect.top == solo:
                    uppress = True
                    vy = -velocidade

        tela.blit(img_fundo1, (x, 0))
        tela.blit(img_fundo2, (y, 0))
        jogador.update(tela)
        jogador.mover(vx, vy)
        cano.update(tela)
        cano.mover()

        if colisao(jogador, cano):
            sair = True
            print(f"Você fez {int(pontos)} pontos")
            frames = 60
            main(frames)

        img = font.render(f"{int(pontos)} pontos", True, "white")
        tela.blit(img, (700, 100))
        relogio.tick(frames)
        pygame.display.update()
    pygame.quit()


# main(frames)
