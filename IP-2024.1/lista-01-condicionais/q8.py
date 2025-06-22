clima = input()
temp_pista = input()
desempenho_treino = input()
posicao = int(input())

print('Estratégia de prova de Max Verstappen!')

#clima e temperatura

if (clima == 'ensolarado'):
    if (temp_pista == 'alta'):
        print('Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!')
    else:
        print('Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.')

elif (clima == 'nublado'):
    if (temp_pista == 'alta'):
        print('Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!')
    else:
        print('Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!')

elif (clima == chuvoso):
    pista_molhada = bool(input())
    if pista_molhada :
        print('Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.')
    else:
        print ('Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!')



#abordagem max

if(posicao == 1):
    if (desempenho_treino == 'bom'):
        print('Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.')
    else:
        print('Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.')
elif(posicao <= 12):
    print('Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.')
elif(posicao >12):
    print('Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.')
