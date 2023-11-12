import pygame
import sys
import pygame.gfxdraw

# Inicialize o Pygame
pygame.init()

# Defina as configurações da tela
WIDTH, HEIGHT = 800, 585
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GameOver")

# Carregue o background
background = pygame.image.load("src/fundo.png").convert()

# Defina cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 102, 51)
RED = (255, 0, 0)

# Carregue a fonte personalizada
font = pygame.font.Font("src/IrishGrover-Regular.ttf", 22)

# Renderize o texto dos botões com a fonte personalizada
text_instructions_third = font.render("Game Over", True, WHITE)
text_instructions_seven = font.render("Restart", True, WHITE)
text_instructions_menu = font.render("Menu", True, WHITE)

# Carregue a fonte personalizada para o título
font_title = pygame.font.Font("src/IrishGrover-Regular.ttf", 36)
text_title = font_title.render("Salve-se Quem Puder", True, WHITE)
text_title_rect = text_title.get_rect(center=(WIDTH // 2, 50))

# Defina as posições dos botões
button_instructions_rect_third = pygame.Rect(WIDTH // 2 - 400, HEIGHT // 2 - 140, 800, 100)
button_instructions_rect_seven = pygame.Rect(WIDTH // 2 - 250, HEIGHT // 2 - 30, 200, 100)  # Ajuste da posição e tamanho
button_instructions_rect_menu = pygame.Rect(WIDTH // 2 + 50, HEIGHT // 2 - 30, 200, 100)   # Ajuste da posição e tamanho

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

        # Desenhe os botões
        pygame.gfxdraw.box(SCREEN, button_instructions_rect_third, RED)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect_seven, BLUE)
        pygame.gfxdraw.box(SCREEN, button_instructions_rect_menu, BLUE)  # Agora, o botão Menu é azul

        # Posicione o texto nos botões
        text_instructions_rect_third = text_instructions_third.get_rect(
            center=button_instructions_rect_third.center
        )
        text_instructions_rect_seven = text_instructions_seven.get_rect(
            center=button_instructions_rect_seven.center
        )
        text_instructions_rect_menu = text_instructions_menu.get_rect(
            center=button_instructions_rect_menu.center
        )

        SCREEN.blit(text_instructions_third, text_instructions_rect_third)
        SCREEN.blit(text_instructions_seven, text_instructions_rect_seven)
        SCREEN.blit(text_instructions_menu, text_instructions_rect_menu)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
