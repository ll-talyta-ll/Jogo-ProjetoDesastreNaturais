import pygame
import sys
import os
from menu import main_menu

# Inicialize o Pygame
pygame.init()

# Defina as configurações da tela
WIDTH, HEIGHT = 600, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Pygame")

# Carregue o background
background = pygame.image.load("src/fundo.png").convert()

# Defina as cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Carregue a fonte personalizada para o título
font_title = pygame.font.Font("src/IrishGrover-Regular.ttf", 36)
text_title = font_title.render("Fuga dos Desastres Naturais", True, WHITE)
text_title_rect = text_title.get_rect(center=(WIDTH // 2, HEIGHT // 2))


# Classe para os botões
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.Font("src/IrishGrover-Regular.ttf", 24)

    def draw(self):
        pygame.draw.rect(SCREEN, BLUE, self.rect)  # Define o background como azul
        pygame.draw.rect(SCREEN, WHITE, self.rect, 2)  # Borda branca

        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        SCREEN.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()


# Função para a tela de apresentação
def tela_apresentacao():
    play_button = Button(
        WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, "Jogar", play_game
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            play_button.handle_event(event)

        SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(text_title, text_title_rect)

        # Adicione um texto explicativo
        font_explanation = pygame.font.Font("src/IrishGrover-Regular.ttf", 18)
        explanation_text = font_explanation.render(
            "Você está em uma floresta em chamas. Evite as bolas de fogo e colete o máximo de água possível!",
            True,
            WHITE,
        )
        explanation_rect = explanation_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 100)
        )
        SCREEN.blit(explanation_text, explanation_rect)

        play_button.draw()

        pygame.display.flip()


# Função para iniciar o jogo
def play_game():
    main_menu()
    print("Iniciando o jogo!")


if __name__ == "__main__":
    tela_apresentacao()
