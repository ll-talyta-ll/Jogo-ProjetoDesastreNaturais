import pygame
import sys
import pygame.gfxdraw

# Inicialize o Pygame
pygame.init()

# Defina as configurações da tela
WIDTH, HEIGHT = 1000, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GameOver")

# Carregue o background
background = pygame.image.load("src/fundo.png").convert()

# Defina cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Carregue a fonte personalizada
font = pygame.font.Font("src/IrishGrover-Regular.ttf", 22)

# Renderize o texto dos botões com a fonte personalizada
text_instructions_exit = font.render("Exit", True, WHITE)

# Carregue a fonte personalizada para o título
font_title = pygame.font.Font("src/IrishGrover-Regular.ttf", 36)
text_title = font_title.render("Salve-se Quem Puder", True, WHITE)
text_title_rect = text_title.get_rect(center=(WIDTH // 2, 50))

# Adicione um novo título "Game Over"
font_game_over = pygame.font.Font("src/IrishGrover-Regular.ttf", 48)
text_game_over = font_game_over.render("Game Over", True, WHITE)
text_game_over_rect = text_game_over.get_rect(center=(WIDTH // 2, 120))

# Defina as posições dos botões
button_instructions_rect_exit = pygame.Rect(
    WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50
)  # Novo botão Exit


def game_over(pontos):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_instructions_rect_exit.collidepoint(
                    event.pos
                ):  # Se o botão Exit for clicado
                    pygame.quit()
                    sys.exit()

        SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(text_title, text_title_rect)
        SCREEN.blit(text_game_over, text_game_over_rect)  # Novo título "Game Over"

        pygame.gfxdraw.box(
            SCREEN, button_instructions_rect_exit, BLUE
        )  # Novo botão Exit

        text_instructions_exit_rect = (
            text_instructions_exit.get_rect(  # Novo botão Exit
                center=button_instructions_rect_exit.center
            )
        )

        SCREEN.blit(
            text_instructions_exit, text_instructions_exit_rect
        )  # Novo botão Exit

        # Exibir a pontuação
        text_pontuacao = font.render(f"Pontuação: {pontos}", True, WHITE)
        text_pontuacao_rect = text_pontuacao.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        SCREEN.blit(text_pontuacao, text_pontuacao_rect)

        pygame.display.flip()


if __name__ == "__main__":
    pontos = 123  # Substitua isso pela variável real de pontuação do seu jogo
    game_over(pontos)
