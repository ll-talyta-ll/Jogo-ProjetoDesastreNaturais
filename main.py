import pygame
import random
from gameover import game_over
from som import start_special_sound, special_sound

largura = 1000
largura_obstaculo = 2000
altura_obstaculo = 500
altura = 500
frames = 60
# posição do solo
solo = 220
# Campo utilizado para manipular a velocidade do cenário
velocidade_mapa = 2


# Manipulação do obstáculo na base inferior da tela
class Cano(pygame.sprite.Sprite):
    def __init__(self, imagem, som_colisao):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = 270, largura_obstaculo + random.randint(0, 1000)
        self.som_colisao = som_colisao

    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)

    def mover(self):
        self.rect.move_ip(-velocidade_mapa, 0)

    def recriar(self):
        if self.rect.left < -400:
            self.rect.top, self.rect.left = 270, largura_obstaculo + random.randint(
                0, 2000
            )

    def reproduzir_som_colisao(self):
        pygame.mixer.Sound.play(self.som_colisao)
        start_special_sound()  # Chama a função para iniciar o som especial


# Nova classe para representar moedas
class Moeda(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.visible = True
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = random.randint(
            100, 500
        ), largura_obstaculo + random.randint(0, 1000)

    def update(self, superficie):
        if self.visible:  # Only update and blit if the coin is visible
            superficie.blit(self.imagem, self.rect)

    def mover(self):
        if self.visible:
            self.rect.move_ip(-velocidade_mapa, 0)

    def recriar(self):
        if self.rect.left < -400:
            self.rect.top, self.rect.left = random.randint(
                100, 500
            ), largura_obstaculo + random.randint(0, 2000)
            self.visible = True  # Reset visibility when re-created


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


def main(frames, character):
    pygame.init()
    pygame.font.init()

    font = pygame.font.SysFont(None, 70)
    tela = pygame.display.set_mode([largura, altura])

    relogio = pygame.time.Clock()

    if character == "girl":
        img_girl = pygame.transform.scale(
            pygame.image.load("src/girl.png").convert(), (200, 200)
        )
        img_girl.set_colorkey((0, 0, 0))
        jogador = Player(img_girl)
    else:
        img_boy = pygame.transform.scale(
            pygame.image.load("src/mario.png").convert(), (200, 200)
        )
        img_boy.set_colorkey((0, 0, 0))
        jogador = Player(img_boy)

    img_fundo1 = pygame.image.load("src/fundo.png").convert_alpha()
    img_fundo2 = pygame.image.load("src/fundo.png").convert_alpha()
    img_fundo1 = pygame.transform.scale(img_fundo1, (largura, altura))
    img_fundo2 = pygame.transform.scale(img_fundo2, (largura, altura))
    cano = pygame.transform.scale(pygame.image.load("src/fire.png").convert(), (30, 30))
    moeda = pygame.transform.scale(
        pygame.image.load("src/coin.png").convert(), (50, 50)
    )

    cano.set_colorkey((0, 0, 0))
    moeda.set_colorkey((0, 0, 0))

    vx, vy = 0, 0
    velocidade = 25
    uppress = False
    sair = False
    x = 0
    y = largura
    cano = Cano(cano, special_sound)
    moeda = Moeda(moeda)
    pontos = 0
    while sair is False:
        if int(pontos) % 50 == 0:
            frames += 1
        pontos += 1
        cano.recriar()
        moeda.recriar()

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
        moeda.update(tela)
        moeda.mover()

        if colisao(jogador, cano):
            sair = True
            print(f"Você fez {int(pontos)} pontos")
            cano.reproduzir_som_colisao()
            frames = 60
            game_over(pontos)

        if colisao(jogador, moeda):
            pontos += 10
            moeda.visible = False

        img = font.render(f"{int(pontos)} pontos", True, "white")
        tela.blit(img, (700, 100))
        relogio.tick(frames)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main(frames, "girl")
