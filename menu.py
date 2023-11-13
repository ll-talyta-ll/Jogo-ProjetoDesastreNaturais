import pygame
import sys
import pygame.gfxdraw
import os
from telaapresentacao import tela_apresentacao
from instructions import instructions
from som import start_background_sound, sound_configuration
from main import main

# from som import sound_configuration

# Inicialize o Pygame
pygame.init()

# Defina as configurações da tela
WIDTH, HEIGHT = 1000, 500
pygame.display.set_caption("Menu Pygame")

# Carregue o background
background = pygame.image.load("src/fundo.png").convert()

# Defina cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Carregue a fonte personalizada
font = pygame.font.Font("src/IrishGrover-Regular.ttf", 24)

# Renderize o texto dos botões com a fonte personalizada
text_character = font.render("Iniciar partida", True, WHITE)
text_instructions = font.render("Instruções", True, WHITE)
text_sound = font.render("Som", True, WHITE)

# Carregue a fonte personalizada para o título
font_title = pygame.font.Font("src/IrishGrover-Regular.ttf", 36)
text_title = font_title.render("Salve-se Quem Puder", True, WHITE)
text_title_rect = text_title.get_rect(center=(WIDTH // 2, 50))
background = pygame.image.load("src/fundo.png").convert()

# Defina cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Carregue a fonte personalizada
font = pygame.font.Font("src/IrishGrover-Regular.ttf", 24)

# Renderize o texto dos botões com a fonte personalizada
text_character = font.render("Iniciar partida", True, WHITE)
text_instructions = font.render("Instruções", True, WHITE)
text_sound = font.render("Som", True, WHITE)

# Carregue a fonte personalizada para o título
font_title = pygame.font.Font("src/IrishGrover-Regular.ttf", 36)
text_title = font_title.render("Salve-se Quem Puder", True, WHITE)
text_title_rect = text_title.get_rect(center=(WIDTH // 2, 50))

# Defina as posições dos botões
button_character_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 50, 300, 50)
button_instructions_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 10, 300, 50)
button_sound_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 70, 300, 50)


# Função para a tela de menu
def main_menu():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    while True:
        start_background_sound()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_character_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Botão de Iniciar Partida pressionado!")
                    # Abrir a tela de seleção de personagem em um novo processo
                    tela_apresentacao()
                elif button_instructions_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Botão de Instruções pressionado!")
                    instructions()
                    # Adicione a lógica para exibir as instruções aqui
                elif button_sound_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Botão de Ligar/Desligar Som pressionado!")
                    sound_configuration()
                    # Adicione a lógica para ligar/desligar o som aqui

        SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(text_title, text_title_rect)
        pygame.gfxdraw.box(SCREEN, button_character_rect, BLUE)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect, BLUE)
        pygame.gfxdraw.box(SCREEN, button_sound_rect, BLUE)
        text_character_rect = text_character.get_rect(
            center=button_character_rect.center
        )
        text_instructions_rect = text_instructions.get_rect(
            center=button_instructions_rect.center
        )
        text_sound_rect = text_sound.get_rect(center=button_sound_rect.center)
        SCREEN.blit(text_title, text_title_rect)
        pygame.gfxdraw.box(SCREEN, button_character_rect, BLUE)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect, BLUE)
        pygame.gfxdraw.box(SCREEN, button_sound_rect, BLUE)
        text_character_rect = text_character.get_rect(
            center=button_character_rect.center
        )
        text_instructions_rect = text_instructions.get_rect(
            center=button_instructions_rect.center
        )
        text_sound_rect = text_sound.get_rect(center=button_sound_rect.center)
        SCREEN.blit(text_character, text_character_rect)
        SCREEN.blit(text_instructions, text_instructions_rect)
        SCREEN.blit(text_sound, text_sound_rect)
        SCREEN.blit(text_instructions, text_instructions_rect)
        SCREEN.blit(text_sound, text_sound_rect)
        pygame.display.flip()


if __name__ == "__main__":
    main_menu()
