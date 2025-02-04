import sys, pygame
# configuracion
pygame.init()
ventana = pygame.display.set_mode((512, 256))
reloj = pygame.time.Clock()


# game loop
while True:
    ventana.fill(pygame.Color("#cdcdcd"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    reloj.tick(60)
