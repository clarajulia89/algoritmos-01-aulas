media = 0
contador = 0

while True: 
    idade = int(input("Digite sua idade: "))
    if (idade < 0):
        print("Idade inválida.")
    elif idade == 0:
        break
    else: 
        contador += 1
        media += idade
if contador == 0:
    print("Não houve cálculo.")        
media = media/contador
print(f"Quantidade de idades foi: {contador}")
print(f"Média das idades: {media}")        


