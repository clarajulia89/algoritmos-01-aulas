# entrada de dados 
lado_a = int(input("Digite o valor de A: "))
lado_b = int(input("Digite o valor de B: "))
lado_c = int(input("Digite o valor de C: "))

# processamento
if (lado_a > lado_b + lado_c) and (lado_b > lado_a + lado_c) and (lado_c > lado_a + lado_b):
    print("é um triângulo")
else: 
    print("Não é um triângulo")    