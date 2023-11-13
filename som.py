import pygame
import sys

# Inicialize o mixer do pygame
pygame.mixer.init()
pygame.init()

# Defina as configurações da tela
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Configuração do Som")

# Carregue o background
background = pygame.image.load("src/fundo.png").convert()

# Defina cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Carregue a fonte personalizada
font = pygame.font.Font("src/IrishGrover-Regular.ttf", 24)

# Renderize o texto dos botões com a fonte personalizada
font_small = pygame.font.Font("src/IrishGrover-Regular.ttf", 18)

# Renderize o título
font_title = pygame.font.Font("src/IrishGrover-Regular.ttf", 36)
text_title = font_title.render("Configuração do Som", True, WHITE)
text_title_rect = text_title.get_rect(center=(WIDTH // 2, 50))

# Carregue o som de fundo
background_sound = pygame.mixer.Sound("src/som_fundo.mp3")

# Variável para controlar o estado do som de fundo
sound_background_on = True
sound_special_on = True


# Função para ligar/desligar o som de fundo
def toggle_background_sound():
    global sound_background_on
    if sound_background_on:
        background_sound.stop()
        sound_background_on = False
    else:
        background_sound.play(-1)  # -1 indica reprodução em loop
        sound_background_on = True


# Função para iniciar o som de fundo
def start_background_sound():
    global background_sound  # Declare background_sound como global
    if sound_background_on:
        background_sound.play(-1)


# Função para parar o som de fundo
def stop_background_sound():
    background_sound.stop()


# Função para exibir a tela de controle de som
def sound_configuration():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_background_rect.collidepoint(pygame.mouse.get_pos()):
                    toggle_background_sound()  # Ligar/desligar som de fundo

        screen.fill(WHITE)
        # Desenhe o background
        screen.blit(background, (0, 0))
        # Desenhe o título
        screen.blit(text_title, text_title_rect)
        # Desenhe o botão de controle de som de fundo
        button_background_rect = pygame.Rect(100, 100, 200, 50)
        pygame.draw.rect(screen, BLUE, button_background_rect)
        # Renderize o texto no botão de controle de som de fundo
        text_background = font_small.render(
            "Som de Fundo: " + ("Ligado" if sound_background_on else "Desligado"),
            True,
            WHITE,
        )
        button_background_text_rect = text_background.get_rect(
            center=button_background_rect.center
        )
        screen.blit(text_background, button_background_text_rect)

        pygame.display.flip()


if __name__ == "__main__":
    sound_configuration()
