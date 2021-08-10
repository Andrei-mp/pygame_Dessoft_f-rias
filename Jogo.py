# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal

WIDTH = 1300 # Largura
HEIGHT = 650 # Altura

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Nave')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT or event.type == pygame.KEYUP :
            game = False

    # ----- Gera saídas
    window.fill((255, 255, 255))  # Preenche com a cor branca

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados