# entrada de dados
real = float(input("Digite um número real: "))
inteiro1 = int(input("Digite um número inteiro: "))
inteiro2 = int(input("Digite outro número inteiro: "))
# processamento

calculo1 = (real * 2) * (inteiro1 / 2)
calculo2 = (real * 3) + inteiro2   
calculo3 = (real ** 3)

# saída de dados
print(f"a) O produto do número real por 2, multiplicado pelo quociente do número inteiro por 2 é: {calculo1: .2f}")
print(f"b) A soma do número real multiplicado por 3, com o número inteiro é: {calculo2: .2f}")
print(f"c) O número real elevado ao cubo é: {calculo3: .2f}")

