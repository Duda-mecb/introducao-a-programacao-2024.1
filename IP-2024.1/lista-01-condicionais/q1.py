piloto = input()
dist = float(input())
tempo = float(input())

vel_media = dist / tempo

if vel_media > 227:
    print(f'{piloto} se deu muito bem na prova de hoje!!')
elif vel_media == 227:
    print(f'{piloto} teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!')
else:
    print(f'{piloto} não se deu tão bem. É preciso melhorar isso!')