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

pygame.time.delay(2000)  # Aguarde 2 segundos antes de sair
pygame.quit()


##TO DO: substituir player.png, obstaculo.png, musica_fundo.mp3 e som_colisao.wav 