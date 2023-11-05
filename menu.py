import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as configurações da tela
WIDTH, HEIGHT = 400, 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Pygame")

# Carregue o background
background = pygame.image.load('fundo.png').convert()

# Carregue as imagens dos botões
button_character = pygame.image.load('girl.png').convert()
button_play = pygame.image.load('mario.png').convert()

# Defina as posições dos botões
button_character_rect = button_character.get_rect(center=(WIDTH//2, HEIGHT//2 - button_character.get_height()//2))
button_play_rect = button_play.get_rect(center=(WIDTH//2, HEIGHT//2 + button_play.get_height()))

# Defina a fonte e o texto
font = pygame.font.Font(None, 15)
text_character = font.render("Escolha o Personagem para iniciar o jogo", True, (255, 0, 0))
text_play = font.render("", True, (255, 0, 0))

text_character_rect = text_character.get_rect(center=(WIDTH//2, HEIGHT//2 - button_character.get_height() - 20))
text_play_rect = text_play.get_rect(center=(WIDTH//2, HEIGHT//2 + button_play.get_height()//2 + 20))

# Defina o loop principal do jogo
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_character_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Botão de Personagem 1 pressionado!")
                    # Adicione a lógica do botão de personagem aqui
                elif button_play_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Botão de de Personagem 2 pressionado!")
                    # Adicione a lógica do botão de jogar aqui

        # Atualize a tela
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(button_character, button_character_rect)
        SCREEN.blit(button_play, button_play_rect)
        SCREEN.blit(text_character, text_character_rect)
        SCREEN.blit(text_play, text_play_rect)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
