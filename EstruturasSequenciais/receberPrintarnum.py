#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

try:
    entradaNumero = int(input("Digite um numero: "))
    print("O numero informado foi " , entradaNumero)
    
except ValueError:
    print("Entrada deve ser apenas de NUMEROS")


