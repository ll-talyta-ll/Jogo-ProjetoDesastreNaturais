import pygame
import sys
from main import main

# Inicialize o Pygame
pygame.init()

# Defina as configurações da tela
WIDTH, HEIGHT = 400, 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seleção de Personagem")

# Carregue o background da tela de seleção de personagem
background = pygame.image.load("src/fundo.png").convert()

# Carregue as imagens dos personagens que o jogador pode selecionar (redimensionadas e com fundos transparentes)
character1 = pygame.transform.scale(
    pygame.image.load("src/girl.png").convert(), (100, 100)
)
character2 = pygame.transform.scale(
    pygame.image.load("src/mario.png").convert(), (120, 120)
)

# Defina a cor preta como a cor transparente nas imagens dos personagens
character1.set_colorkey((0, 0, 0))
character2.set_colorkey((0, 0, 0))

# Defina as posições dos personagens na tela
character1_rect = character1.get_rect(center=(WIDTH // 3, HEIGHT // 2))
character2_rect = character2.get_rect(center=(WIDTH // 1.3, HEIGHT // 2))

# Defina o botão de voltar como um triângulo inclinado
button_back = pygame.Surface((30, 30), pygame.SRCALPHA)
pygame.draw.polygon(button_back, (0, 0, 255), [(10, 30), (0, 30), (10, 30)])
button_back_rect = button_back.get_rect(topleft=(10, 10))

# Carregue a fonte personalizada
font_title = pygame.font.Font("src/IrishGrover-Regular.ttf", 24)

# Renderize o texto "SELECIONE SEU PERSONAGEM"
text_select_character = font_title.render("Selecione seu personagem", True, (0, 0, 0))
text_select_character_rect = text_select_character.get_rect(center=(WIDTH // 2, 30))


# Função para a tela de seleção de personagem
def select_character():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if character1_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Personagem 1 selecionado!")
                    main(60)
                elif character2_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Personagem 2 selecionado!")
                    main(60)
                elif button_back_rect.collidepoint(pygame.mouse.get_pos()):
                    return  # Retorne ao menu

        SCREEN.fill((255, 255, 255))
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(character1, character1_rect)
        SCREEN.blit(character2, character2_rect)

        # Desenhe o botão de voltar (triângulo)
        SCREEN.blit(button_back, button_back_rect)

        # Desenhe o texto "SELECIONE SEU PERSONAGEM"
        SCREEN.blit(text_select_character, text_select_character_rect)

        pygame.display.flip()


if __name__ == "__main__":
    select_character()
