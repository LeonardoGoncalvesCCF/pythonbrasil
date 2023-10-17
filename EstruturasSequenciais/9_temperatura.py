#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
print("------------------------------------------------------------")
temph = float(input("Qual a temperatura atual em Fahrenheit ? "))
print("------------------------------------------------------------")
tempc = 5 * ((temph - 32) / 9)
print("A temperatura em graus Celsius é de: ", tempc)