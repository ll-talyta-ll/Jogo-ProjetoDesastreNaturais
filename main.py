import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo de Subir Obstáculos")

# Cores
branco = (255, 255, 255)

# Personagem
player_image = pygame.image.load('player.png')
player_x = largura_tela // 2 - 25
player_y = altura_tela - 100
player_velocidade = 5

# Obstáculos
obstaculos = []
obstaculo_image = pygame.image.load('obstaculo.png')
obstaculo_velocidade = 3
obstaculo_respawn_timer = 100

# Sons
pygame.mixer.music.load('musica_fundo.mp3')
pygame.mixer.music.play(-1)
som_colisao = pygame.mixer.Sound('som_colisao.wav')

# Pontuação
pontuacao = 0
fonte = pygame.font.Font(None, 36)

# Função para desenhar a pontuação na tela
def mostrar_pontuacao():
    texto = fonte.render(f'Pontuação: {pontuacao}', True, branco)
    tela.blit(texto, (10, 10))

# Loop do jogo
jogando = True
while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and player_x > 0:
        player_x -= player_velocidade
    if teclas[pygame.K_RIGHT] and player_x < largura_tela - 50:
        player_x += player_velocidade

    # Movimentação dos obstáculos
    for obstaculo in obstaculos:
        obstaculo[1] += obstaculo_velocidade
        if obstaculo[1] > altura_tela:
            obstaculos.remove(obstaculo)
            pontuacao += 1

    # Respawn de obstáculos
    obstaculo_respawn_timer -= 1
    if obstaculo_respawn_timer == 0:
        obstaculos.append([random.randint(0, largura_tela - 50), 0])
        obstaculo_respawn_timer = 100

    # Verificação de colisão com obstáculos
    for obstaculo in obstaculos:
        if (player_x < obstaculo[0] < player_x + 50 or player_x < obstaculo[0] + 50 < player_x + 50) and player_y < obstaculo[1] + 50:
            som_colisao.play()
            jogando = False

    # Desenhar na tela
    tela.fill((0, 0, 0))
    tela.blit(player_image, (player_x, player_y))
    mostrar_pontuacao()
    for obstaculo in obstaculos:
        tela.blit(obstaculo_image, (obstaculo[0], obstaculo[1]))

    pygame.display.update()

# Tela de Game Over
tela.fill((0, 0, 0))
texto_gameover = fonte.render("Game Over", True, branco)
tela.blit(texto_gameover, (largura_tela // 2 - 100, altura_tela // 2 - 50))
mostrar_pontuacao()
pygame.display.update()



# IMPLEMENTAÇÃO

import pygame
import random

largura = 1000
altura = 700
frames = 60
cor_branca = (255, 255, 255)
cor_vermelho = (255, 0, 0)
cor_prata = (192, 192, 192)
cor_amarelo = (255, 255, 0)
cor_verde = (0, 255, 0)
solo = 250
velocidade_mapa = 10


class Cano(pygame.sprite.Sprite):
    def __init__(self, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.top, self.rect.left = 320, largura + random.randint(0, 1000)

    def update(self, superficie):
        superficie.blit(self.imagem, self.rect)

    def mover(self):
        self.rect.move_ip(-velocidade_mapa, 0)

    def recriar(self):
        if self.rect.left < -200:
            self.rect.top, self.rect.left = 320, largura + random.randint(0, 2000)


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
    #pygame.mixer.init()
    #pygame.mixer.music.load('Top Gear.mp3')
    #pygame.mixer.music.play(loops=-1)
    #pygame.mixer.music.set_volume(0.05)

    font = pygame.font.SysFont(None, 70)
    tela = pygame.display.set_mode([largura, altura])

    relogio = pygame.time.Clock()

    img_girl = pygame.image.load('girl.png').convert_alpha()
    jogador = Player(img_girl)

    img_fundo1 = pygame.image.load('fundo.png').convert_alpha()
    img_fundo2 = pygame.image.load('fundo.png').convert_alpha()
    cano = pygame.image.load('cano.png').convert_alpha()

    vx, vy = 0, 0
    velocidade = 2
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
                    vy = - velocidade

        tela.blit(img_fundo1, (x, 0))
        tela.blit(img_fundo2, (y, 0))
        jogador.update(tela)
        jogador.mover(vx, vy)
        cano.update(tela)
        cano.mover()

        if colisao(jogador, cano):
            sair = True
            print(f'voce fez {int(pontos)} pontos')
            frames = 60
            main(frames)

        img = font.render(f'{int(pontos)} pontos', True, 'white')
        tela.blit(img, (700, 100))
        relogio.tick(frames)
        pygame.display.update()
    pygame.quit()


main(frames)

pygame.time.delay(2000)  # Aguarde 2 segundos antes de sair
pygame.quit()


##TO DO: substituir player.png, obstaculo.png, musica_fundo.mp3 e som_colisao.wav 
