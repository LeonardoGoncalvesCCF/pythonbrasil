#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
# (72.7*altura) - 58

print("------------------------------------------------------------")
print("Diga qual a sua altura para calcular o seu peso ideial: ")
print("------------------------------------------------------------")
altura = float(input("Digite sua altura: "))
print("------------------------------------------------------------")
pesoideial = (72.7 * altura) - 58
print("O seu peso ideal é de: ",pesoideial)
print("------------------------------------------------------------")