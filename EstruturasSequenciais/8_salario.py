#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print("Para calcular o salario é preciso saber quantas horas voçê trabalhou e qual o valor da hora")
print("------------------------------------------------------------")
horas = float(input("Quantas horas você trabalhar por mes? "))
print("------------------------------------------------------------")
reais = float(input("Qauntos reais voçê ganha por hora? "))
print("------------------------------------------------------------")
salario = horas * reais
print("Seu salario é de: ", salario)
print("------------------------------------------------------------")