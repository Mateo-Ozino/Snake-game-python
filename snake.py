import turtle
import time
import random

posponer = 0.08

# Puntaje
score = 0
high_score = 0

# Configuración de la ventana
window = turtle.Screen()
window.title('Snake🐍')
window.bgcolor('black')
window.setup(width = 600, height = 600)
window.tracer(0)

# Cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Comida
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('red')
food.penup()
food.goto(0, 100)

# Cuerpo de la serpiente
segmentos = []

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write(f'Score: {score}    High Score: {high_score}', align = 'center', font = ('Montserrat', 24, 'bold'))

# Funciones
def go_up():
    if not head.direction == 'down':
        head.direction = 'up'
def go_down():
    if not head.direction == 'up':
        head.direction = 'down'
def go_left():
    if not head.direction == 'right':
        head.direction = 'left'
def go_right():
    if not head.direction == 'left':
        head.direction = 'right'

def movimiento():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

# Limpieza de texto game over
def limpieza_game_over():
    texto_game_over.clear()

# Teclado
window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_left, 'Left')
window.onkeypress(go_right, 'Right')
window.onkeypress(limpieza_game_over)


while True:
    window.update()
    
    # Colisiones con los bordes
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction = 'stop'
        
        # Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(2000,2000)
        
        # Limpiar lista de segmentos
        segmentos.clear()
        
        # Limpiar score
        score = 0
        texto.clear()
        texto.write(f'Score: {score}    High Score: {high_score}', align = 'center', font = ('Montserrat', 24, 'bold'))
        
        # Texto game over
        texto_game_over = turtle.Turtle()
        texto_game_over.speed(0)
        texto_game_over.color('white')
        texto_game_over.penup()
        texto_game_over.hideturtle()
        texto_game_over.goto(0, 20)
        texto_game_over.write(f'Perdiste😓', align = 'center', font = ('Montserrat', 20, 'normal'))
        texto_game_over.goto(0, -40)
        texto_game_over.write(f'Tocá Enter para volver a jugar', align = 'center', font = ('Montserrat', 20, 'normal'))

# Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = 'stop'

            # Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(2000,2000)
            
            # Limpiar lista de segmentos
            segmentos.clear()
            
            # Limpiar score
            score = 0
            texto.clear()
            texto.write(f'Score: {score}    High Score: {high_score}', align = 'center', font = ('Montserrat', 24, 'bold'))
            
            # Texto game over
            texto_game_over = turtle.Turtle()
            texto_game_over.speed(0)
            texto_game_over.color('white')
            texto_game_over.penup()
            texto_game_over.hideturtle()
            texto_game_over.goto(0, 20)
            texto_game_over.write(f'Perdiste😓', align = 'center', font = ('Montserrat', 20, 'normal'))
            texto_game_over.goto(0, -40)
            texto_game_over.write(f'Tocá Enter para volver a jugar', align = 'center', font = ('Montserrat', 20, 'normal'))
    
    # Colisiones con la comida
    if head.distance(food) < 20:
        x = random.randint(-280, 260)
        y = random.randint(-280, 260)
        food.goto(x,y)
        
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.color('gray')
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        
        # Aumentar score
        score += 10
        
        if score > high_score:
            high_score = score
        
        texto.clear()
        texto.write(f'Score: {score}    High Score: {high_score}', align = 'center', font = ('Montserrat', 24, 'bold'))
    
    # Movimiento del cuerpo de la serpiente
    total_segmentos = len(segmentos)
    for i in range(total_segmentos - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x,y)
    
    if total_segmentos > 0:
        x = head.xcor()
        y = head.ycor()
        segmentos[0].goto(x,y)
    
    movimiento()
    time.sleep(posponer)