import pygame
import sys
import pygame.gfxdraw
import os

# from som import sound_configuration

# Inicialize o Pygame
pygame.init()

# Defina as configurações da tela
WIDTH, HEIGHT = 800, 585
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Instrucoes")

# Carregue o background
background = pygame.image.load("src/fundo.png").convert()

# Defina cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 102, 51)

# Carregue a fonte personalizada
font = pygame.font.Font("src/IrishGrover-Regular.ttf", 22)

# Renderize o texto dos botões com a fonte personalizada
text_instructions = font.render("Instruções:", True, WHITE)
text_instructions_second = font.render("1* Você deve selecionar o seu personagem", True, WHITE)
text_instructions_third = font.render("2* Você deve selecionar o nível do jogo", True, WHITE)
text_instructions_forty = font.render("3* Com sua agilidade e reflexos você deverá sobreviver a desastres naturais", True, WHITE)
text_instructions_five = font.render("4* Não Esqueça de se divertir e boa sorte no jogo ! ●▂● ", True, WHITE)
text_instructions_six = font.render("", True, WHITE)
text_instructions_seven = font.render("Voltar Para Menu", True, WHITE)


# Carregue a fonte personalizada para o título
font_title = pygame.font.Font("src/IrishGrover-Regular.ttf", 36)
text_title = font_title.render("Salve-se Quem Puder", True, WHITE)
text_title_rect = text_title.get_rect(center=(WIDTH // 2, 50))
text_title_rect_second = text_title.get_rect(center=(WIDTH // 2, 50))
text_title_rect_third = text_title.get_rect(center=(WIDTH // 2, 50))
text_title_rect_forty = text_title.get_rect(center=(WIDTH // 2, 50))
text_title_rect_five = text_title.get_rect(center=(WIDTH // 2, 50))
text_title_rect_six = text_title.get_rect(center=(WIDTH // 2, 50))
text_title_rect_seven = text_title.get_rect(center=(WIDTH // 2, 50))

# Defina as posições dos botões
button_instructions_rect = pygame.Rect(WIDTH // 2 - 400, HEIGHT // 2 - 200, 800, 100)
button_instructions_rect_second = pygame.Rect(WIDTH // 2 - 400, HEIGHT // 2 - 140, 800, 100)
button_instructions_rect_third = pygame.Rect(WIDTH // 2 - 400, HEIGHT // 2 - 80, 800, 100)
button_instructions_rect_forty = pygame.Rect(WIDTH // 2 - 400, HEIGHT // 2 - 20, 800, 100)
button_instructions_rect_five = pygame.Rect(WIDTH // 2 - 400, HEIGHT // 2 - -40, 800, 100)
button_instructions_rect_six = pygame.Rect(WIDTH // 2 - 400, HEIGHT // 2 - -120, 800, 100)
button_instructions_rect_seven = pygame.Rect(WIDTH // 2 - 140, HEIGHT // 2 - -130, 300, 50)


# Função para a tela de menu
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(text_title, text_title_rect)
        SCREEN.blit(text_title, text_title_rect_second)
        SCREEN.blit(text_title, text_title_rect_third)
        SCREEN.blit(text_title, text_title_rect_forty)
        SCREEN.blit(text_title, text_title_rect_five)
        SCREEN.blit(text_title, text_title_rect_six)
        SCREEN.blit(text_title, text_title_rect_seven)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect, GREEN)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect_second, GREEN)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect_third, GREEN)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect_forty, GREEN)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect_five, GREEN)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect_six, GREEN)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect_seven, BLUE)
        text_instructions_rect = text_instructions.get_rect(
            center=button_instructions_rect.center
        )
        text_instructions_rect_second = text_instructions_second.get_rect(
            center=button_instructions_rect_second.center
        )
        text_instructions_rect_third = text_instructions_third.get_rect(
            center=button_instructions_rect_third.center
        )
        text_instructions_rect_forty = text_instructions_forty.get_rect(
            center=button_instructions_rect_forty.center
        )
        text_instructions_rect_five = text_instructions_five.get_rect(
            center=button_instructions_rect_five.center
        )
        text_instructions_rect_six = text_instructions_six.get_rect(
            center=button_instructions_rect_six.center
        )
        text_instructions_rect_seven = text_instructions_seven.get_rect(
            center=button_instructions_rect_seven.center
        )
        SCREEN.blit(text_instructions, text_instructions_rect)
        SCREEN.blit(text_instructions_second, text_instructions_rect_second)
        SCREEN.blit(text_instructions_third, text_instructions_rect_third)
        SCREEN.blit(text_instructions_forty, text_instructions_rect_forty)
        SCREEN.blit(text_instructions_five, text_instructions_rect_five)
        SCREEN.blit(text_instructions_six, text_instructions_rect_six)
        SCREEN.blit(text_instructions_seven, text_instructions_rect_seven)
        pygame.display.flip()



if _name_ == "_main_":
    main_menu()
