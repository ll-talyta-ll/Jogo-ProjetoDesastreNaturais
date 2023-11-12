# import pygame
# import sys

# # Inicialize o Pygame
# pygame.init()

# # Defina as configurações da tela
# WIDTH, HEIGHT = 400, 300
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Configuração de Som")

# # Carregue o background da tela de configuração de som
# background = pygame.image.load("src/fundo.png").convert()

# # Carregue as imagens dos botões (som de fundo e efeitos sonoros)
# # sound_background_on = pygame.image.load("src/sound_background_on.png").convert()
# # sound_background_off = pygame.image.load("src/sound_background_off.png").convert()
# # sound_effects_on = pygame.image.load("src/sound_effects_on.png").convert()
# # sound_effects_off = pygame.image.load("src/sound_effects_off.png").convert()

# # Defina as posições dos botões
# # sound_background_rect = sound_background_on.get_rect(center=(WIDTH // 2, HEIGHT // 3))
# # sound_effects_rect = sound_effects_on.get_rect(center=(WIDTH // 2, 2 * HEIGHT // 3))

# # Inicialize as variáveis para controlar o estado do som
# sound_background_enabled = True
# sound_effects_enabled = True


# # Função para a tela de configuração de som
# def sound_configuration():
#     # while True:
#     #     for event in pygame.event.get():
#     #         if event.type == pygame.QUIT:
#     #             pygame.quit()
#     #             sys.exit()
#     #         if event.type == pygame.MOUSEBUTTONDOWN:
#     #             # if sound_background_rect.collidepoint(pygame.mouse.get_pos()):
#     #             #     sound_background_toggle()
#     #             # elif sound_effects_rect.collidepoint(pygame.mouse.get_pos()):
#     #             #     sound_effects_toggle()

#     #     SCREEN.fill((255, 255, 255))
#     #     SCREEN.blit(background, (0, 0))

#     #     # # Desenhe os botões de som de fundo
#     #     # if sound_background_enabled:
#     #     #     SCREEN.blit(sound_background_on, sound_background_rect)
#     #     # else:
#     #     #     SCREEN.blit(sound_background_off, sound_background_rect)

#     #     # # Desenhe os botões de efeitos sonoros
#     #     # if sound_effects_enabled:
#     #     #     SCREEN.blit(sound_effects_on, sound_effects_rect)
#     #     # else:
#     #     #     SCREEN.blit(sound_effects_off, sound_effects_rect)

#     # pygame.display.flip()


# def sound_background_toggle():
#     global sound_background_enabled
#     sound_background_enabled = not sound_background_enabled
#     # Adicione a lógica para ligar/desligar o som de fundo aqui


# def sound_effects_toggle():
#     global sound_effects_enabled
#     sound_effects_enabled = not sound_effects_enabled
#     # Adicione a lógica para ligar/desligar os efeitos sonoros aqui


# if __name__ == "__main__":
#     sound_configuration()
