pont_lewis = int(input())
lugar_lewis = int(input())
pont_max = int(input())
lugar_max = int(input())
pont_bottas = int(input())
lugar_bottas = int(input())

if (lugar_lewis <= 10):
    lewis = pont_lewis + 5
else:
    lewis = pont_lewis

if (lugar_max <= 10):
    verstappen = pont_max + 5
else:
    verstappen = pont_max

if (lugar_bottas <= 10):
    bottas = pont_bottas + 5
else:
    bottas = pont_bottas
 

if((lewis >= verstappen) and (lewis >= bottas)):
    print (f'Lewis Hamilton ganhou a competição com {lewis} pontos!')
elif ((verstappen>lewis) and (verstappen>=bottas)):
    print(f'Max Verstappen ganhou a competição com {verstappen} pontos!')
elif ((bottas>verstappen) and (bottas>lewis)):
    print (f'Valtteri Bottas ganhou a competição com {bottas} pontos!')
    
elif (verstappen==lewis):
    print (f'Lewis Hamilton ganhou a competição com {lewis} pontos!')
elif (verstappen==bottas):
    print (f'Valtteri Bottas ganhou a competição com {bottas} pontos!')
elif (bottas==lewis):
    print(f'Lewis Hamilton ganhou a competição com {lewis} pontos!')
elif (bottas==lewis==verstappen):
    print(f'Lewis Hamilton ganhou a competição com {lewis} pontos!')
  
