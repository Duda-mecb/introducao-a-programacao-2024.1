construtor1 = input()
posicao1 = int(input())
salario1 = int(input())
construtor2 = input()
posicao2 = int(input())
salario2 = int(input())

pontos1 = 0
if construtor1 == "Red Bull":
    pontos1 = 3
elif construtor1 == "McLaren":
    pontos1 = 2
elif construtor1 == "Mercedes": 
    pontos1 = 1
elif construtor1 == "Aston Martin": 
    pontos1 = 1
if posicao1 == 1:
    pontos1 = pontos1 + 3
elif posicao1 == 2:
    pontos1 = pontos1 + 2
if posicao1 != 3:
    pontos1 = pontos1 + salario1 // 4

pontos2 = 0
if construtor2 == "Red Bull":
    pontos2 = 3
elif construtor2 == "McLaren":
    pontos2 = 2
elif construtor2 == "Mercedes": 
    pontos2 = 1
elif construtor2 == "Aston Martin": 
    pontos2 = 1
if posicao2 == 1:
    pontos2 = pontos2 + 3
elif posicao2 == 2:
    pontos2 = pontos2 + 2
if posicao2 != 3:
    pontos2 = pontos2 + salario2 // 4


if construtor1 == "Ferrari" or ((posicao1 != 1) and (posicao1 != 2) and (posicao1 != 3)) or (construtor1 != "Red Bull" and posicao1 == 3):
    pontos1 = -1
if construtor2 == "Ferrari" or ((posicao2 != 1) and (posicao2 != 2) and (posicao2 != 3)) or (construtor2 != "Red Bull" and posicao2 == 3):
    pontos2 = -1

if pontos1 == -1 and pontos2 == -1:
    print("Depois de tantas temporadas, o Sainz vai descançar em 2025.")
elif pontos1 > pontos2:
    print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor1}, que pontuou {pontos1}.")
elif pontos2 > pontos1:
    print(f"SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor2}, que pontuou {pontos2}.")
else:
    print("As duas são ótimas opções! Vamos, Sainz!!")
