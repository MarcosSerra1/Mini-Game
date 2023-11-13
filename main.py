import turtle

turtle.setup(width=800, height=600)
turtle.title("Mini Game")

tartaruga = turtle.Turtle()
tartaruga.pencolor("red")

while True:
    direcao = input('Para qual direção devemos ir? (f: frente / t: trás) ')

    if direcao.lower() == 'f':
        pixels = int(input('quantos pixels devemos movimentar para frente? '))
        rotacao = input('Rotacionar para a (d: direita, e: esquerda, n: não rotacionar) ')
        if rotacao.lower() == 'd':
            graus = int(input('Quanto para a direita devemos rotacionar? '))
            tartaruga.right(graus)  # Gira a tartaruga para a direita em um ângulo de x graus
            tartaruga.forward(pixels)  # Move a tartaruga para frente por x unidades
        elif rotacao.lower() == 'e':
            graus = int(input('Quanto para a esquerda devemos rotacionar? '))
            tartaruga.left(graus)  # Gira a tartaruga para a esquerda em um ângulo de x graus
            tartaruga.forward(pixels)  # Move a tartaruga para frente por x unidades
        else:
            tartaruga.forward(pixels)  # Move a tartaruga para frente por x unidades

    elif direcao.lower() == 't':
        pixels = int(input('quantos pixels devemos movimentar para trás? '))
        rotacao = input('Rotacionar para a (d: direita, e: esquerda, n: não rotacionar) ')
        if rotacao.lower() == 'd':
            graus = int(input('Quanto para a direita devemos rotacionar? '))
            tartaruga.right(graus)  # Gira a tartaruga para a direita em um ângulo de x graus
            tartaruga.backward(pixels)  # Move a tartaruga para trás por x unidades
        elif rotacao.lower() == 'e':
            graus = int(input('Quanto para a esquerda devemos rotacionar? '))
            tartaruga.left(graus)  # Gira a tartaruga para a esquerda em um ângulo de x graus
            tartaruga.backward(pixels)  # Move a tartaruga para trás por x unidades
        else:
            tartaruga.backward(pixels)  # Move a tartaruga para trás por x unidades

    continuar = input("continuar andando (s: sim / n: não): ")
    if continuar.lower() == 'n':
        break
