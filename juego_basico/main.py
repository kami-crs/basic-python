import pygame

# la funcion init() sirve para inicializar el modulo pygame
pygame.init()
# display.set_mode sirve para crear la pantalle con un ancho y alto
pantalla = pygame.display.set_mode((640, 480))

# running se usa como bandera para mantener activo el while
running = True
while running:
    # pantalla.fill sirve para elegir el color de la pantalla en RGB
    pantalla.fill((205, 205, 205))
    # pymage.event.get() devuelve una lista de eventos pueden ser teclados o mouse
    for event in pygame.event.get():
        # determina que el evento es de tipo teclado presionado
        if event.type == pygame.KEYDOWN:
            # compara si la tecla es igual a "q"
            if event.key == pygame.K_q:
                running = False
    # flip() sirve para pintar la pantalla
    pygame.display.flip()

