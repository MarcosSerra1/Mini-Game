import turtle

turtle.setup(width=800, height=600)
turtle.title("Mini Game")

tartaruga = turtle.Turtle()
tartaruga.pencolor("red")

def movimentar():
   movimentar_turtle = int(input('quantos pixels devemos movimentar? '))
   return movimentar_turtle

def rotacionar_direita():
    graus = int(input('Quantos graus para a direita devemos rotacionar? '))
    tartaruga.right(graus)  # Gira a tartaruga para a direita em um ângulo de x graus
    return tartaruga

def rotacionar_esquerda():
    graus = int(input('Quanto para a esquerda devemos rotacionar? '))
    tartaruga.left(graus)  # Gira a tartaruga para a esquerda em um ângulo de x graus


while True:
    direcao = input('Para qual direção devemos ir? (f: frente / t: trás) ')

    if direcao.lower() == 'f':  # Frente
        pixels = movimentar()
        rotacao = input('Rotacionar para a (d: direita, e: esquerda, n: não rotacionar) ')
        if rotacao.lower() == 'd':
            rotacionar_direita()
        elif rotacao.lower() == 'e':
            rotacionar_esquerda()
        tartaruga.forward(pixels)  # Move a tartaruga para frente por x unidades

    elif direcao.lower() == 't':  # Trás
        pixels = movimentar()
        rotacao = input('Rotacionar para a (d: direita, e: esquerda, n: não rotacionar) ')
        if rotacao.lower() == 'd':
            rotacionar_direita()
        elif rotacao.lower() == 'e':
            rotacionar_esquerda()
        tartaruga.backward(pixels)  # Move a tartaruga para trás por x unidades

    continuar = input("continuar andando (s: sim / n: não): ")
    if continuar.lower() == 'n':
        break
