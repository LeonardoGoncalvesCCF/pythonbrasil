#Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


print("------------------------------------------------------------")
print("Um litro de tinta cobre até 3 metros quadrados")
parede = float(input("Qual o tamanho do local a ser pintado em metros quadarados? "))
print("------------------------------------------------------------")

litros = parede / 3

umlata = 0

while litros > 18:
    umlata = umlata + 1
    litros = litros - 18


if  litros < 18 and litros != 0:
    
    umlata = umlata + 1
    latapreco = 80
    precolata = latapreco * umlata
print("Você precisará de mais ", umlata, " e custará  ",precolata )

