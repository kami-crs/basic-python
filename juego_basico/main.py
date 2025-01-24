import pygame

# la funcion init() sirve para inicializar el modulo pygame
pygame.init()
# display.set_mode sirve para crear la pantalle con un ancho y alto
pantalla = pygame.display.set_mode((640, 480))

# font.Font sirve para crear la fuente
fuente = pygame.font.Font(None, size=30)

# cargar imagen
mario_imagen = pygame.image.load("mario.png").convert_alpha()
mario_imagen = pygame.transform.scale(mario_imagen, (64, 64))
# cargar imagen de dogo
dogo_imagen = pygame.image.load("dogo.jpg")
dogo_imagen = pygame.transform.scale(dogo_imagen, (100, 100))

# running se usa como bandera para mantener activo el while
running = True
while running:
    # pantalla.fill sirve para elegir el color de la pantalla en RGB
    pantalla.fill((205, 205, 205))
    # mostrar texto
    texto = fuente.render("Hello world", True, pygame.Color("#ff4500"))
    pantalla.blit(texto, (250, 200))
    # mostrar imagen de mario
    pantalla.blit(mario_imagen, (0, 0))
    # mostrar imagen de dogo
    pantalla.blit(dogo_imagen, (100, 100))
    # pymage.event.get() devuelve una lista de eventos pueden ser teclados o mouse
    for event in pygame.event.get():
        # determina que el evento es de tipo teclado presionado
        if event.type == pygame.KEYDOWN:
            # compara si la tecla es igual a "q"
            if event.key == pygame.K_q:
                running = False
    # flip() sirve para pintar la pantalla
    pygame.display.flip()

