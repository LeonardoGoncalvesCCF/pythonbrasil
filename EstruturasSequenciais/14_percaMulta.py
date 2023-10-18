#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.


print("------------------------------------------------------------")
print("O limite de peso de um peixe é de 50Kg, informe o peso do peixe")
print("------------------------------------------------------------")
pesopeixe = float(input("Peso do Peixe: "))

pesomaximo = 50 
excesso = pesopeixe

if pesomaximo < excesso :
    multa = (pesopeixe - pesomaximo) * 4
    print("------------------------------------------------------------")
    print("O limite de 50kg foi ultrapassado a taxa a pagar é de: ", multa)
else:
    print("------------------------------------------------------------")
    print("O peso deo peixe esta dentro do limite ", pesopeixe)