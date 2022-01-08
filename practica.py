import pygame
import random
import sys 
import time
#Pantalla
ANCHO = 1200
ALTO = 600
color_rojo = (255,0,0)
color_negro = (0,0,0)
color_azul = (0,0,255)
color_blanco = (255,255,255)
color_gris = (125,125,125)
color_gris_osc = (25,25,25)
color_verde_bajo = (0,200,0)
color_verde = (50,200,200)

Buno = 10
Bdos = 10
Btres = 10
Bcuatro = 10
Bcinco = 10
Bseis = 10
Bciete = 10
Bocho = 10
Bnueve = 10
Bdies = 10

lado = 0
ladoDos = 0
ladoTres = 0
ladoCuat = 0
ladoCinc = 0
ladoSeis = 0
ladoSiet = 0
ladoOch = 0
ladoNuev = 0
ladoDies = 0

camb_lado = 0
camb_ladoDos = 0
camb_ladoTres = 0
camb_ladoCuat = 0
camb_ladoCinc = 0
camb_ladoSeis = 0
camb_ladoSiet = 0
camb_ladoOch = 0
camb_ladoNiev = 0
camb_ladoDies = 0

pygame.init()
#Crear ventana de juegos

ventaja = pygame.display.set_mode((ANCHO, ALTO)) #Creando la ventana
tamano = pygame.font.Font(None, 20)
fuente_game_over = pygame.font.Font(None, 50)
text_finihs = "Game over"
contador = 0
texto = "Puntuación"

texto_count = tamano.render(texto, 2, (255, 255, 255))
finish = fuente_game_over.render(text_finihs, 2, (255, 0, 0))

#Crear jugador
jugador_size = 60
jugador_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
jugadorDos_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
jugadorTres_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
jugadorCuat_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
jugadorCinc_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
jugadorSeis_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
jugadorSiet_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
jugadorOch_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
jugadorNuev_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
jugadorDies_pos = [random.randint(0, ANCHO - jugador_size), ALTO - jugador_size - 30]
#crear enemigo

enemigo_size = 50
enemigo_pos = [random.randint(0, ANCHO - enemigo_size), 60]
game_over = False

clock = pygame.time.Clock() #Iniciando
def detectar_colision(jugador_pos, jugadorDos_pos, jugadorTres_pos, jugadorCuat_pos, jugadorCinc_pos, jugadorSeis_pos, jugadorSiet_pos, jugadorOch_pos, jugadorNuev_pos, jugadorDies_pos, enemigo_pos):
    jx = jugador_pos[0]
    jy = jugador_pos[1]
    dx = jugadorDos_pos[0]
    dy = jugadorDos_pos[1]
    tx = jugadorTres_pos[0]
    ty = jugadorTres_pos[1]
    cx = jugadorCuat_pos[0]
    cy = jugadorCuat_pos[1]
    Cx = jugadorCinc_pos[0]
    Cy = jugadorCinc_pos[1]
    sx = jugadorSeis_pos[0]
    sy = jugadorSeis_pos[1]
    Six = jugadorSiet_pos[0]
    Siy = jugadorSiet_pos[1]
    Ohx = jugadorOch_pos[0]
    Ohy = jugadorOch_pos[1]
    Nx = jugadorNuev_pos[0]
    Ny = jugadorNuev_pos[1]
    Dx = jugadorDies_pos[0]
    Dy = jugadorDies_pos[1]
    ex = enemigo_pos[0]
    ey = enemigo_pos[1]
    if(ex >= jx and ex <(jx + jugador_size)) or (jx >=ex and jx<(ex + enemigo_size)):
        if (ey >= jy and ey>(jy + jugador_size)) or (jy >= ey and jy<(ey + enemigo_size)):
            return True
        return False
    #Validar jugador dos
    if contador > 0:
        if(ex >= dx and ex <(dx + jugador_size)) or (dx >=ex and dx<(ex + enemigo_size)):
            if (ey >= dy and ey>(dy + jugador_size)) or (dy >= ey and dy<(ey + enemigo_size)):
                return True
            return False
    if contador >= 2:
        if(ex >= tx and ex <(tx + jugador_size)) or (tx >=ex and tx<(ex + enemigo_size)):
            if (ey >= ty and ey>(ty + jugador_size)) or (ty >= ey and ty<(ey + enemigo_size)):
                return True
            return False
    if contador >= 3:
        if(ex >= cx and ex <(cx + jugador_size)) or (cx >=ex and cx<(ex + enemigo_size)):
            if (ey >= cy and ey>(cy + jugador_size)) or (cy >= ey and cy<(ey + enemigo_size)):
                return True
            return False
    if contador >= 4:
        if(ex >= Cx and ex <(Cx + jugador_size)) or (Cx >=ex and Cx<(ex + enemigo_size)):
            if (ey >= Cy and ey>(Cy + jugador_size)) or (Cy >= ey and Cy<(ey + enemigo_size)):
                return True
            return False
    if contador >= 5:
        if(ex >= sx and ex <(sx + jugador_size)) or (sx >=ex and sx<(ex + enemigo_size)):
            if (ey >= sy and ey>(sy + jugador_size)) or (sy >= ey and sy<(ey + enemigo_size)):
                return True
            return False
    if contador >= 6:
        if(ex >= Six and ex <(Six + jugador_size)) or (Six >=ex and Six<(ex + enemigo_size)):
            if (ey >= Siy and ey>(Siy + jugador_size)) or (Siy >= ey and Siy<(ey + enemigo_size)):
                return True
            return False
    if contador >= 7:
        if(ex >= Ohx and ex <(Ohx + jugador_size)) or (Ohx >=ex and Ohx<(ex + enemigo_size)):
            if (ey >= Ohy and ey>(Ohy + jugador_size)) or (Ohy >= ey and Ohy<(ey + enemigo_size)):
                return True
            return False
    if contador >= 8:
        if(ex >= Nx and ex <(Nx + jugador_size)) or (Nx >=ex and Nx<(ex + enemigo_size)):
            if (ey >= Ny and ey>(Ny + jugador_size)) or (Ny >= ey and Ny<(ey + enemigo_size)):
                return True
            return False
    if contador >= 9:
        if(ex >= Dx and ex <(Dx + jugador_size)) or (Dx >=ex and Dx<(ex + enemigo_size)):
            if (ey >= Dy and ey>(Dy + jugador_size)) or (Dy >= ey and Dy<(ey + enemigo_size)):
                return True
            return False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = enemigo_pos[0]
            if event.key == pygame.K_LEFT:
                x -= enemigo_size
            if event.key == pygame.K_RIGHT:
                x += enemigo_size
            enemigo_pos[0] = x

    ventaja.fill(color_negro)
    ventaja.blit(texto_count, (15, 10))
    if enemigo_pos[1] >=0 and enemigo_pos[1] < ALTO:
        enemigo_pos[1] += 10
    else:
        enemigo_pos[0] = random.randint(0, ANCHO - enemigo_size)
        enemigo_pos[1] = 60
        contador +=1
    if detectar_colision(jugador_pos, jugadorDos_pos, jugadorTres_pos, jugadorCuat_pos, jugadorCinc_pos, jugadorSeis_pos, jugadorSiet_pos, jugadorOch_pos, jugadorNuev_pos, jugadorDies_pos, enemigo_pos):
        ventaja.blit(finish, (ANCHO / 2 - 60, ALTO / 2 - 30))
        game_over = True 
    #Control del jugador unon

    if camb_lado == 25:
        lado = random.randint(0,1)
        camb_lado = 0
    else:
        camb_lado += 1
    if jugador_pos[0] < 0:
        lado = 0
    if jugador_pos[0] > ANCHO - 60:
        lado = 1

    if contador >= 10:
        Buno = 20
    if contador >= 11:
        Bdos = 20
    if contador >= 12:
        Btres = 20
    if contador >= 13:
        Bcuatro = 20
    if contador >= 14:
        Bciete = 20
    if contador >= 15:
        Bseis = 20
    if contador >= 16:
        Bciete = 20
    if contador >= 17:
        Bocho = 20
    if contador >= 18:
        Bnueve = 20
    if contador >= 19:
        Bdies = 20

    if lado == 1:
        jugador_pos[0] -= Buno
    else:
        jugador_pos[0] += Buno

    #Control de jugador dos    
    if camb_ladoDos == 20:
        ladoDos = random.randint(0,1)
        camb_ladoDos = 0
    else:
        camb_ladoDos += 1
    if jugadorDos_pos[0] < 0:
        ladoDos = 0
    if jugadorDos_pos[0] > ANCHO - 60:
        ladoDos = 1
    if ladoDos == 1:
        jugadorDos_pos[0] -= Bdos 
    else:
        jugadorDos_pos[0] += Bdos

    #Control de jugador tres    
    if camb_ladoTres == 25:
        ladoTres = random.randint(0,1)
        camb_ladoTres = 0
    else:
        camb_ladoTres += 1
    if jugadorTres_pos[0] < 0:
        ladoTres = 0
    if jugadorTres_pos[0] > ANCHO - 60:
        ladoTres = 1
    if ladoTres == 1:
        jugadorTres_pos[0] -= Btres 
    else:
        jugadorTres_pos[0] += Btres

    #cuatro
    if camb_ladoCuat == 30:
        ladoCuat = random.randint(0,1)
        camb_ladoCuat = 0
    else:
        camb_ladoCuat += 1
    if jugadorCuat_pos[0] < 0:
        ladoCuat = 0
    if jugadorCuat_pos[0] > ANCHO - 60:
        ladoCuat = 1
    if ladoCuat == 1:
        jugadorCuat_pos[0] -= Bcuatro 
    else:
        jugadorCuat_pos[0] += Bcuatro

    #Cinco
    if camb_ladoCinc == 35:
        ladoCinc = random.randint(0,1)
        camb_ladoCinc = 0
    else:
        camb_ladoCinc += 1
    if jugadorCinc_pos[0] < 0:
        ladoCinc = 0
    if jugadorCinc_pos[0] > ANCHO - 60:
        ladoCinc = 1
    if ladoCinc == 1:
        jugadorCinc_pos[0] -= Bcinco 
    else:
        jugadorCinc_pos[0] += Bcinco

     #seis
    if camb_ladoSeis == 40:
        ladoSeis = random.randint(0,1)
        camb_ladoSeis = 0
    else:
        camb_ladoSeis += 1
    if jugadorSeis_pos[0] < 0:
        ladoSeis = 0
    if jugadorSeis_pos[0] > ANCHO - 60:
        ladoSeis = 1
    if ladoSeis == 1:
        jugadorSeis_pos[0] -= Bseis 
    else:
        jugadorSeis_pos[0] += Bseis

    if camb_ladoSiet == 45:
        ladoSiet = random.randint(0,1)
        camb_ladoSiet = 0
    else:
        camb_ladoSiet += 1
    if jugadorSeis_pos[0] < 0:
        ladoSiet = 0
    if jugadorSiet_pos[0] > ANCHO - 60:
        ladoSiet = 1
    if ladoSiet == 1:
        jugadorSiet_pos[0] -= Bciete
    else:
        jugadorSiet_pos[0] += Bciete

    if camb_ladoOch == 50:
        ladoOch = random.randint(0,1)
        camb_ladoOch = 0
    else:
        camb_ladoOch += 1
    if jugadorOch_pos[0] < 0:
        ladoOch = 0
    if jugadorOch_pos[0] > ANCHO - 60:
        ladoOch = 1
    if ladoOch == 1:
        jugadorOch_pos[0] -= Bocho 
    else:
        jugadorOch_pos[0] += Bocho

    if camb_ladoNiev == 55:
        ladoNuev = random.randint(0,1)
        camb_ladoNiev = 0
    else:
        camb_ladoNiev += 1
    if jugadorNuev_pos[0] < 0:
        ladoNuev = 0
    if jugadorNuev_pos[0] > ANCHO - 60:
        ladoNuev = 1
    if ladoNuev == 1:
        jugadorNuev_pos[0] -= Bnueve
    else:
        jugadorNuev_pos[0] += Bnueve

    if camb_ladoDies == 60:
        ladoDies = random.randint(0,1)
        camb_ladoDies = 0
    else:
        camb_ladoDies += 1
    if jugadorDies_pos[0] < 0:
        ladoDies = 0
    if jugadorDies_pos[0] > ANCHO - 60:
        ladoDies = 1
    if ladoDies == 1:
        jugadorDies_pos[0] -= Bdies
    else:
        jugadorDies_pos[0] += Bdies

    mensaje = tamano.render(str(contador), 2, (255, 255, 255))
    ventaja.blit(mensaje, (40, 30))
    #Jugador uno
    pygame.draw.rect(ventaja, color_azul, 
        (jugador_pos[0], jugador_pos[1], 
        jugador_size, jugador_size))
    #Jugador dos
    if contador >= 1:
        pygame.draw.rect(ventaja, color_verde, 
            (jugadorDos_pos[0], jugadorDos_pos[1], 
            jugador_size, jugador_size))
    if contador >= 2:
        pygame.draw.rect(ventaja, color_blanco,
            (jugadorTres_pos[0], jugadorTres_pos[1],
            jugador_size, jugador_size))
    if contador >= 3:
        pygame.draw.rect(ventaja, color_gris,
            (jugadorCuat_pos[0], jugadorCuat_pos[1],
            jugador_size, jugador_size))
    if contador >= 4:
        pygame.draw.rect(ventaja, color_gris_osc,
            (jugadorCinc_pos[0], jugadorCinc_pos[1],
            jugador_size, jugador_size))
    if contador >= 5:
        pygame.draw.rect(ventaja, color_blanco,
            (jugadorSeis_pos[0], jugadorSeis_pos[1],
            jugador_size, jugador_size))
    if contador >= 6:
        pygame.draw.rect(ventaja, color_verde,
            (jugadorSiet_pos[0], jugadorSiet_pos[1],
            jugador_size, jugador_size))
    if contador >= 7:
        pygame.draw.rect(ventaja, color_gris,
            (jugadorOch_pos[0], jugadorOch_pos[1],
            jugador_size, jugador_size))
    if contador >= 8:
        pygame.draw.rect(ventaja, color_gris_osc,
            (jugadorNuev_pos[0], jugadorNuev_pos[1],
            jugador_size, jugador_size))
    if contador >= 9:
        pygame.draw.rect(ventaja, color_rojo,
            (jugadorDies_pos[0], jugadorDies_pos[1],
            jugador_size, jugador_size))
    #Enemigo
    pygame.draw.rect(ventaja, color_rojo, 
        (enemigo_pos[0], enemigo_pos[1], 
        enemigo_size, enemigo_size))
    clock.tick(20)
    pygame.display.update()
time.sleep(3)