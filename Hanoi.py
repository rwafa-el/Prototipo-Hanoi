import Torre as t
import os
import click
import sys

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    n = int(input("Com quantos pinos deseja jogar?\n\n-> "))

    torreA = t.Torre(n)
    torreB = t.Torre(n)
    torreC = t.Torre(n)

    torres = {
        "A": torreA,
        "B": torreB,
        "C": torreC
    }

    for i in range(n,0,-1):
        torreA.empilhar(i)

    while not torreC.jogadorVenceu(n):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Objetivo:\nMover todos os discos da torre A para a torre C.\n")
        print("Regras:\nApenas um disco pode ser movido por vez.\nNão é permitido colocar um disco maior sobre um menor.\n\n")

        for nome, torre in torres.items():
            print(f"Estado atual da torre {nome}: ", end=" ")
            torre.mostrarTorre()

        print("\nDigite seu movimento (origem destino ou 'X X' para reiniciar): ", end="")
        letra = input()
        letra = letra.upper().replace(" ", "")
        if len(letra) != 2:
            print("\nEntrada inválida! Use o formato 'A B' para mover de A para B ou 'X X' para reiniciar.\n")
            print("Pressione qualquer coisa para tentar novamente...\n")
            char = click.getchar()
            continue

        origem, destino = letra[0], letra[1]

        if origem.lower() == 'x' and destino.lower() == 'x':
            print("\nReiniciando o desafio...\n")
            print("Pressione qualquer coisa...\n")
            char = click.getchar()
            torreA = t.Torre(n)
            torreB = t.Torre(n)
            torreC = t.Torre(n)
            for i in range(n,0,-1):
                torreA.empilhar(i)
            torres = {
                "A": torreA,
                "B": torreB,
                "C": torreC
            }
            continue

        torreOrigem = torres.get(origem.upper())
        torreDestino = torres.get(destino.upper())

        if not torreOrigem or not torreDestino:
            print("\nTorre inválida! Use apenas A, B ou C.\n")
            print("Pressione qualquer coisa para tentar novamente...\n")
            char = click.getchar()
            continue

        discoMovido = torreOrigem.desempilhar()
        if discoMovido == -1:
            print("\nMovimento inválido: torre de origem vazia!\n")
            print("Pressione qualquer coisa para tentar novamente...\n")
            char = click.getchar()
            continue

        if not torreDestino.torreVazia() and torreDestino.topoTorre() < discoMovido:
            print("\nMovimento inválido: não pode colocar disco maior sobre menor.\n")
            torreOrigem.empilhar(discoMovido)
            print("Pressione qualquer coisa para tentar novamente...\n")
            char = click.getchar()
            continue

        torreDestino.empilhar(discoMovido)
    
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for nome, torre in torres.items():
        print(f"Estado final da torre {nome}: ", end=" ")
        torre.mostrarTorre()

    print("\nVOCÊ CONCLUIU O DESAFIO.\n")
    char = click.getchar()

    sys.exit() 

    
main()