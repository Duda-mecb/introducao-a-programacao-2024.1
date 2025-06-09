piloto_a = input()
tempo_a = float(input())
piloto_b = input()
tempo_b = float(input())
piloto_c = input()
tempo_c = float(input())

print('E o Pódio do GP de Mônaco é:')

#A ganha
if((tempo_a < tempo_b) and (tempo_a < tempo_c)):
    primeiro = piloto_a
    tempo_primeiro = tempo_a
    if(tempo_b < tempo_c):
        segundo = piloto_b
        tempo_segundo = tempo_b
        terceiro = piloto_c
        tempo_terceiro = tempo_c
    else:
        segundo = piloto_c
        tempo_segundo = tempo_c
        terceiro = piloto_b
        tempo_terceiro = tempo_b

#B ganha
elif((tempo_b < tempo_a) and (tempo_b < tempo_c)):
    primeiro = piloto_b
    tempo_primeiro = tempo_b
    if(tempo_a < tempo_c):
        segundo = piloto_a
        tempo_segundo = tempo_a
        terceiro = piloto_c
        tempo_terceiro = tempo_c
    else:
        segundo = piloto_c
        tempo_segundo = tempo_c
        terceiro = piloto_a
        tempo_terceiro = tempo_a

#C ganha
elif((tempo_c < tempo_a) and (tempo_c < tempo_b)):
    primeiro = piloto_c
    tempo_primeiro = tempo_c
    if(tempo_a < tempo_b):
        segundo = piloto_a
        tempo_segundo = tempo_a
        terceiro = piloto_b
        tempo_terceiro = tempo_b
    else:
        segundo = piloto_b
        tempo_segundo = tempo_b
        terceiro = piloto_a
        tempo_terceiro = tempo_a
        


print(f'{primeiro} está no lugar mais alto do pódio com tempo de {tempo_primeiro} horas de corrida.\n{segundo} está no segundo lugar do pódio com tempo de {tempo_segundo} horas de corrida.\n{terceiro} está no terceiro lugar do pódio com tempo de {tempo_terceiro} horas de corrida.')

print(f'Galvão, temos um momento histórico da Fórmula 1, {primeiro} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempo_primeiro} horas de prova.')
