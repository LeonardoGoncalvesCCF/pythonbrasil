#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    #Para homens: (72.7*h) - 58
    #Para mulheres: (62.1*h) - 44.7
    
print("------------------------------------------------------------")
escolha = input("Digite H se for homem e M para mulher: ")
print("------------------------------------------------------------")

if escolha.upper() == "M":
    pesoM = float(input("Digite ssua altura para calcular seu peso ideial: "))
    pesoIdealM = (62.1*pesoM) - 44.7
    print("------------------------------------------------------------")
    print("Seu peso ideal é: ", pesoIdealM)
    print("------------------------------------------------------------")
    
else:
    pesoH = float(input("Digite ssua altura para calcular seu peso ideial: "))
    pesoIdealH = (72.7*pesoH) - 58
    print("------------------------------------------------------------")
    print("Seu peso ideal é: ", pesoIdealH)
    print("------------------------------------------------------------")