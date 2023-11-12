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
button_character = pygame.image.load('nivel1s.png').convert()
button_play = pygame.image.load('nivel2s.png').convert()
button_level3 = pygame.image.load('nivel3s.png').convert()

# Defina a distância vertical entre os botões
button_gap = 30

# Defina as posições dos botões
button_character_rect = button_character.get_rect(center=(WIDTH//2, HEIGHT//2 - button_character.get_height() - button_gap))
button_play_rect = button_play.get_rect(center=(WIDTH//2, HEIGHT//2))
button_level3_rect = button_level3.get_rect(center=(WIDTH//2, HEIGHT//2 + button_play.get_height() + button_gap))

# Defina a fonte e o texto
font = pygame.font.Font(None, 15)
text_character = font.render("Escolha o Nível para iniciar o jogo", True, (255, 0, 0))

# Calcule a posição para centralizar o texto
text_character_rect = text_character.get_rect(center=(WIDTH//2, 20))

text_play = font.render("", True, (255, 0, 0))
text_level3 = font.render("", True, (255, 0, 0))

text_play_rect = text_play.get_rect(center=(WIDTH//2, HEIGHT//2 + button_play.get_height()//2))
text_level3_rect = text_level3.get_rect(center=(WIDTH//2, HEIGHT//2 + button_play.get_height()//2 + button_gap + 20))

# Defina o loop principal do jogo
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_character_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Botão do Nível 1 pressionado!")
                    # Adicione a lógica do botão de personagem aqui
                elif button_play_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Botão do Nível 2 pressionado!")
                    # Adicione a lógica do botão de jogar aqui
                elif button_level3_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Botão do Nível 3 pressionado!")

        # Atualize a tela
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(button_character, button_character_rect)
        SCREEN.blit(button_play, button_play_rect)
        SCREEN.blit(button_level3, button_level3_rect)
        SCREEN.blit(text_character, text_character_rect)
        SCREEN.blit(text_play, text_play_rect)
        SCREEN.blit(text_level3, text_level3_rect)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()