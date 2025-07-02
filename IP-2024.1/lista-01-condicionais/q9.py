voltas = int(input())
clima = input()
dif = input()
pneu = input()

desgaste = int(0)

if clima == 'sol':
    if pneu == 'chuva':
       desgaste = abs(voltas * 15 - 50)
    elif (pneu == 'macio') and (dif != 'alta'):
	      desgaste = abs(voltas * 2 - 50)	
    elif (pneu == 'médio') and (dif != 'alta'):
	      desgaste = abs(voltas * 2 - 70)
    elif (pneu == 'macio') and (dif == 'alta'):
	      desgaste = abs(voltas * 3 - 50)
    elif (pneu == 'duro') and (dif == 'alta'):
	      desgaste = abs(voltas - 90)

else:
    if (pneu == 'chuva') and (dif == 'baixa'):
	      desgaste = abs(50 - voltas)
    elif (pneu == 'chuva') and (dif == 'média'):
	      desgaste = abs(voltas * 2 - 50)
    elif (pneu == 'chuva') and (dif == 'alta'):
	      desgaste = abs(voltas * 3 - 50)
    elif pneu == 'duro':
	      desgaste = abs(voltas * 15 - 90)
    elif pneu == 'médio':
	      desgaste = abs(voltas * 15 - 70)
    elif pneu == 'macio':
	      desgaste = abs(voltas * 15 - 50)
	
if desgaste >= 20 :
    print(f'A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {desgaste}.')
else:
    print(f'Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {desgaste} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.')
