import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as configurações da tela
WIDTH, HEIGHT = 1000, 500
pygame.display.set_caption("Instrucoes")

# Defina cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Carregue o background
background = pygame.image.load("src/fundo.png").convert()

# Carregue a fonte personalizada
font = pygame.font.Font("src/IrishGrover-Regular.ttf", 21)

# Renderize o texto dos botões com a fonte personalizada
text_instructions = font.render("Instruções:", True, WHITE)
text_instructions_second = font.render(
    "1* Você deve selecionar o seu personagem: menina ou menino", True, WHITE
)
text_instructions_third = font.render(
    "2* Você deve selecionar o nível do jogo: fácil, médio ou difícil", True, WHITE
)
text_instructions_forty = font.render(
    "3* Com sua agilidade e reflexos você deverá sobreviver a desastres naturais",
    True,
    WHITE,
)
text_instructions_five = font.render(
    "Utilize as teclas de seta do seu teclado para isso!", True, WHITE
)
text_instructions_seven = font.render(
    "4* Não Esqueça de se divertir e boa sorte no jogo ! ●▂●", True, WHITE
)

# Carregue a fonte personalizada para o título
font_title = pygame.font.Font("src/IrishGrover-Regular.ttf", 25)
text_title = font_title.render("Salve-se Quem Puder", True, WHITE)
text_title_rect = text_title.get_rect(center=(WIDTH // 2, 40))

# Adicione uma margem ao redor do background verde
margin = 10

# Calcule a altura total necessária para o texto
total_text_height = (
    text_instructions.get_height()
    + text_instructions_second.get_height()
    + text_instructions_third.get_height()
    + text_instructions_forty.get_height()
    + text_instructions_five.get_height()
    + text_instructions_seven.get_height()
    + 5 * margin  # Adiciona margens entre as linhas
)

# Centralize e defina o tamanho do botão com margem
button_instructions_rect = pygame.Rect(
    WIDTH // 2 - 700 // 2 - margin,
    HEIGHT // 2 - 350 // 2 - margin,
    300 + 2 * margin,
    total_text_height + 2 * margin,
)


# Função para a tela de menu
def instructions():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back_rect.collidepoint(pygame.mouse.get_pos()):
                    return  # Voltar ao Menu

        SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(text_title, text_title_rect)

        # Atualize as posições dos textos dentro da área do background verde
        current_height = button_instructions_rect.top + margin
        for text in [
            text_instructions,
            text_instructions_second,
            text_instructions_third,
            text_instructions_forty,
            text_instructions_five,
            text_instructions_seven,
        ]:
            SCREEN.blit(text, (button_instructions_rect.left + margin, current_height))
            current_height += (
                text.get_height() + margin
            )  # Adiciona uma margem entre as linhas

        # Desenhe o botão "Voltar ao Menu"
        button_back_rect = pygame.Rect(WIDTH // 2 - 80, HEIGHT - 200, 200, 40)
        pygame.draw.rect(SCREEN, BLUE, button_back_rect, border_radius=5)
        text_back = font.render("Voltar ao Menu", True, WHITE)
        button_back_text_rect = text_back.get_rect(center=button_back_rect.center)
        SCREEN.blit(text_back, button_back_text_rect)

        pygame.display.flip()


if __name__ == "_main_":
    instructions()
