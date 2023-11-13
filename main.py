import pygame
import random
import sys

largura = 1000
altura = 500
frames = 60
solo = 220
velocidade_mapa = 2
gravidade = 1


class Cano(pygame.sprite.Sprite):
    def __init__(self, imagem, is_coin=False):
        super().__init__()
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = 270, largura + random.randint(0, 1000)
        self.is_coin = is_coin

    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)

    def mover(self):
        self.rect.move_ip(-velocidade_mapa, 0)

    def recriar(self):
        if self.rect.left < -400:
            self.rect.top, self.rect.left = 270, largura + random.randint(0, 2000)


class Player(pygame.sprite.Sprite):
    def __init__(self, imagem):
        super().__init__()
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = (solo, 100)

    def mover(self, vx, vy):
        self.rect.move_ip(vx, vy)

    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)


def colisao(player, rect):
    return player.rect.colliderect(rect)


def game_over(tela, pontos):
    fonte = pygame.font.SysFont(None, 70)
    mensagem = fonte.render(f"Game Over - Pontuação: {int(pontos)}", True, "white")
    tela.blit(mensagem, (largura // 4, altura // 3))
    pygame.display.flip()
    pygame.time.wait(2000)


def main(frames, character):
    pygame.init()
    tela = pygame.display.set_mode([largura, altura])

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

    coin = pygame.transform.scale(
        pygame.image.load("src/coin.png").convert_alpha(), (50, 50)
    )
    coin.set_colorkey((0, 0, 0))

    # Grupo para os sprites de canos e moedas
    all_sprites = pygame.sprite.Group()

    vx, vy = 0, 0
    velocidade = 20
    uppress = False
    sair = False
    x = 0
    y = largura

    pontos = 0

    clock = pygame.time.Clock()

    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and jogador.rect.top == solo:
                    uppress = True
                    vy = -velocidade

        # Aplique a gravidade
        vy += gravidade

        if jogador.rect.top < solo:
            jogador.rect.top = solo  # Evite que o jogador vá abaixo do solo
            vy = 0  # Reinicie a velocidade vertical

        jogador.mover(vx, vy)

        # Cria novos canos e moedas aleatoriamente
        if random.randint(0, 100) < 5:  # Ajuste o número conforme necessário
            all_sprites.add(Cano(coin, is_coin=True))
        elif random.randint(0, 100) < 5:  # Ajuste o número conforme necessário
            all_sprites.add(
                Cano(
                    pygame.transform.scale(
                        pygame.image.load("src/fire.png").convert_alpha(), (100, 100)
                    )
                )
            )

        for sprite in all_sprites:
            sprite.mover()
            sprite.update(tela)

            # Colisão com o cano ou moeda
            if colisao(jogador, sprite):
                if sprite.is_coin:
                    pontos += 100
                    sprite.recriar()
                else:
                    game_over(tela, pontos)
                    return

        tela.blit(img_fundo1, (x, 0))
        tela.blit(img_fundo2, (y, 0))
        jogador.update(tela)

        img = pygame.font.SysFont(None, 70).render(
            f"Pontuação: {int(pontos)}", True, "white"
        )
        tela.blit(img, (700, 100))

        all_sprites.update(tela)

        pygame.display.flip()
        clock.tick(frames)

    pygame.quit()


if __name__ == "__main__":
    main(frames, pygame.image.load("src/character.png"))
