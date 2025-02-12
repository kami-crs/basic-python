import sys, pygame
# configuracion
pygame.init()
ventana = pygame.display.set_mode((512, 256))
reloj = pygame.time.Clock()
mario_imagen = pygame.image.load("mario.png")
mario_ancho = mario_imagen.get_width()
mario_alto = mario_imagen.get_height()

# player
player = {
    'img': mario_imagen, 
    'w': mario_ancho,
    "h": mario_alto,
    'x': 0,
    'y': 0, 
    'speed': 5,
    'vx': 0,
    'vy': 0,
    'hitbox': pygame.Rect(0, 0, mario_ancho, mario_alto)
}

box = pygame.Rect(256, 128, 64, 64)

def player_update():
    """Esta funcion renderiza el personaje y actualiza su posicion"""
    player['x'] += player['vx']
    player['y'] += player['vy']
    ventana.blit(player['img'], (player['x'], player['y']))
    player['hitbox'].x = player['x']
    player['hitbox'].y = player['y']
    pygame.draw.rect(ventana, '#ff4500', player['hitbox'], 4)

def colision_ventana():
    if player['x'] < 0:
        player['x'] -= player['vx']
        player['x'] = 0
    if player['x'] + player['w'] > ventana.width:
        player['x'] -= player['vx']
        player['x'] = ventana.width - player['w']
        print('Salio de la ventana')
    if player['y'] < 0:
        player['y'] -= player['vy']
        player['y'] = 0
    if player['y'] + player['h'] > ventana.height:
        player['y'] -= player['vy']
        player['y'] = ventana.height - player['h']
 

def update_keyboard(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            player['vx'] = - player['speed']
        if event.key == pygame.K_d:
            player['vx'] = player['speed']
        if event.key == pygame.K_w:
            player['vy'] = - player['speed']
        if event.key == pygame.K_s:
            player['vy'] = player['speed']
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            player['vx'] = 0
        if event.key == pygame.K_d:
            player['vx'] = 0
        if event.key == pygame.K_w:
            player['vy'] = 0
        if event.key == pygame.K_s:
            player['vy'] = 0
# game loop
while True:
    ventana.fill(pygame.Color("#cdcdcd"))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        update_keyboard(event)

    player_update()

    colision = player['hitbox'].colliderect(box)
    if colision:
        player['x'] -= player['vx']
        player['y'] -= player['vy']
       
      
    colision_ventana()

    pygame.draw.rect(ventana, '#ffffff', box)

    pygame.display.flip()
    reloj.tick(60)
