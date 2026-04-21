num = int(input("Digite um número: "))
if num < 0:
    print("Não é possível fazer essa operação.")
else:
    fat = 1
    contador = 1
    while(contador <= 1):
        fat = fat*contador
        contador += 1
    print(f"Seu fatorial é: {fat}")    
