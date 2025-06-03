frase_1 = input()
if(frase_1 == 'Tem uma curva vindo aí, me ajuda!'):
    frase_curva1 = input()

#primeiro input

if (frase_1 == 'TÔ EM ÚLTIMO!'):
    print ('PISA FUNDO')
elif (frase_1 == 'Amiga, calma! Tem um pit stop na tua frente…'):
   print('Ultrapassa ele agora!')
elif (frase_1 == 'MEU PNEU FUROU SOCORRO!'):
    print('Amiga, calma! Tem um pit stop na tua frente…')
elif (frase_1 == 'Esse cara não sai da minha frente...'):
    print('Ultrapassa ele agora!')
elif ((frase_1 == 'Tem uma curva vindo aí, me ajuda!') and (frase_curva1 == 'DIREITA')):
   print('FREIA AGORA E ME DIZ PARA QUE LADO É')
   print ('ENTÃO VIRA LOGO!')
elif ((frase_1 == 'Tem uma curva vindo aí, me ajuda!') and (frase_curva1 == 'ESQUERDA')):
    print('FREIA AGORA E ME DIZ PARA QUE LADO É')
    print ('É SÓ VIRAR!')
elif ((frase_1 == 'Tem uma curva vindo aí, me ajuda!') and ((frase_curva1 != 'ESQUERDA') and (frase_curva1 != 'DIREITA'))):
    print('FREIA AGORA E ME DIZ PARA QUE LADO É')
    print ('Assim não tem como te ajudar, amiga')
else:
    print('Eita, não entendi nada…')


frase_2 = input()
if(frase_2 == 'Tem uma curva vindo aí, me ajuda!'):
    frase_curva2 = input()

#segundo input 

if (frase_2 == 'TÔ EM ÚLTIMO!'):
    print ('PISA FUNDO')
elif (frase_2 == 'Amiga, calma! Tem um pit stop na tua frente…'):
   print('Ultrapassa ele agora!')
elif (frase_2 == 'MEU PNEU FUROU SOCORRO!'):
    print('Amiga, calma! Tem um pit stop na tua frente…')
elif (frase_2 == 'Esse cara não sai da minha frente...'):
    print('Ultrapassa ele agora!')
elif ((frase_2 == 'Tem uma curva vindo aí, me ajuda!') and (frase_curva2 == 'DIREITA')):
   print('FREIA AGORA E ME DIZ PARA QUE LADO É')
   print ('ENTÃO VIRA LOGO!')
elif ((frase_2 == 'Tem uma curva vindo aí, me ajuda!') and (frase_curva2 == 'ESQUERDA')):
    print('FREIA AGORA E ME DIZ PARA QUE LADO É')
    print ('É SÓ VIRAR!')
elif ((frase_2 == 'Tem uma curva vindo aí, me ajuda!') and ((frase_curva2 != 'ESQUERDA') and (frase_curva2 != 'DIREITA'))):
    print('FREIA AGORA E ME DIZ PARA QUE LADO É')
    print ('Assim não tem como te ajudar, amiga')
else:
    print('Eita, não entendi nada…')


print ("LET'S RIDE!")
