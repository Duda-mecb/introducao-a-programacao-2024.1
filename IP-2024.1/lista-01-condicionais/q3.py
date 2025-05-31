pont_charles = int(input())
pont_max = int(input())

if (pont_charles == 0):
    print('Oxe! E vai morrer por causa de 25 pontos?')

else:
    if (pont_charles == 25):
        print('O meu favorito venceu! Pode torar o aco Verstappen')
    elif (pont_charles >= 15):
        print('Esse Charles eh arretado mesmo')
    elif (pont_charles >= 10):
        print('Ele eh desenrolado demais')

    #diferença de pontos
    diferenca = abs(pont_charles - pont_max)
    if (diferenca <= 4):
        print('Ta com a molestia, vai perder para Max Verstappen eh')
    elif (pont_charles > pont_max):
        print('Deu o sangue')
