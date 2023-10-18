"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

(A) salário bruto.
(B) quanto pagou ao INSS.
(C) quanto pagou ao sindicato.
(D) o salário líquido.
(E) calcule os descontos e o salário líquido, conforme a tabela abaixo:
-------------------------------------------------------------------
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
--------------------------------------------------------------------
"""

print("Para calcular o salario é preciso saber quantas horas voçê trabalhou e qual o valor da hora")
print("------------------------------------------------------------")
horas = float(input("Quantas horas você trabalhar por mes? "))
print("------------------------------------------------------------")
reais = float(input("Qauntos reais voçê ganha por hora? "))
print("------------------------------------------------------------")

#A) Salário Bruto
salario = horas * reais
print("Seu salario é de: ", salario)
print("------------------------------------------------------------")

#B)quanto pagou ao INSS.
inss = 0.08
porcentagemInss = salario * inss

print("Os 8 porcento do Inss são ", porcentagemInss)
print("------------------------------------------------------------")

#C) quanto pagou ao sindicato.
sindicato = 0.05
porcentagemSindicato = salario * sindicato

print("Os 5 porcento do Sindicato são ", porcentagemSindicato)
print("------------------------------------------------------------")

#D) o salário líquido.

impostodeRenda = 0.11
porcentagemImpostoRenda = ( salario * impostodeRenda )
salarioLiquido = salario - (porcentagemInss + porcentagemSindicato + porcentagemImpostoRenda)
print("O salrio liquido é igual a: ", salarioLiquido)
print("------------------------------------------------------------")