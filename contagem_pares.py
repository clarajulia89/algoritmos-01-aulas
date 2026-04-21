# entrada de dados 
cont_par = 0
contador = 0
while(contador < 5):
    num = int(input("Digite um número: "))
    if (num % 2 == 0):
        cont_par += 1
    contador += 1
print(f"Quantidades de pares: {cont_par}")

