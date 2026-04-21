qtd_termos = int(input("Digite a quantidade de termos da Fibonacci: "))
if qtd_termos < 0:
    print("Não existe série de Fibonacci com números negativos.")
else: 
    a = 0
    b = 1
    if qtd_termos == 1:
        print(f"{a}")
    elif qtd_termos == 2:
        print(f"{a}")
        print(f"{b}")
    else:
        print(f"{a}")
        print(f"{b}")
        aux = 0        
        for termos in range(qtd_termos - 2):
            aux = a + b
            print(f"{aux}")
            a = b
            b = aux 
