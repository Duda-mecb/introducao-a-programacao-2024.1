vel_max = int(input())
tempo = input()

#monaco
if(tempo == 'neblina' and vel_max < 250) or ((tempo == 'ensolarado' or tempo == 'chuvoso') and (250 <= vel_max <= 260)):
    print ('Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!')
#imola
elif (tempo == 'neblina' and vel_max < 260) or ((tempo == 'ensolarado' or tempo == 'chuvoso') and (261 <= vel_max <= 285)):
    print ('Senna corria em Ímola, onde infelizmente fez sua última corrida.')
#spa
elif (tempo == 'neblina' and vel_max < 285) or ((tempo == 'ensolarado' or tempo == 'chuvoso') and (286 <= vel_max <= 310)):
    print ('Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!')
