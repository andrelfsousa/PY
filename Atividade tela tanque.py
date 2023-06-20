import pygame

# Inicialização do Pygame
pygame.init()

# Dimensões da tela
largura = 800
altura = 600

# Cores
branco = (255, 255, 255)

# Criando a tela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo do Tanque")

# Carregando e redimensionando a imagem do tanque
novo_largura = 100
novo_altura = 100
tanque_imagem = pygame.image.load("C:/Users/andre/OneDrive/Área de Trabalho/work/PYTHON/tanque.png")
tanque_imagem = pygame.transform.scale(tanque_imagem, (novo_largura, novo_altura))

tanque_posicao = tanque_imagem.get_rect()
tanque_posicao.center = (largura // 2, altura // 2)

# Velocidade do tanque
velocidade = 1

# Loop principal do jogo
executando = True
while executando:
    # Verificar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Verificar teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        tanque_posicao.centery -= velocidade
    if teclas[pygame.K_DOWN]:
        tanque_posicao.centery += velocidade
    if teclas[pygame.K_LEFT]:
        tanque_posicao.centerx -= velocidade
    if teclas[pygame.K_RIGHT]:
        tanque_posicao.centerx += velocidade

    # Limpar a tela
    tela.fill(branco)

    # Desenhar o tanque na tela
    tela.blit(tanque_imagem, tanque_posicao)

    # Atualizar a tela
    pygame.display.flip()

# Encerrar o Pygame
pygame.quit()
