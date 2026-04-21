# entrada de dados
peso = float(input("Digite seu peso corporal em kg: "))
altura = float(input("Digite sua altura em metros: "))

# processamento 
IMC = (peso)/(altura*altura)

# saída de dados 
print(f"Seu IMC é: {IMC: .2f}")