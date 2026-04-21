import math

message = """
Menu de opções:
1 - Somar dois números
2 - Dividir dois números
3 - Raiz quadrada de um número
"""

print(message)
opção = int(input("Digite sua opção: "))
resultado = 0

if opção == 1:
   n1 = float(input("Digite o número 1: "))
   n2 = float(input("Digite o número 2: "))
   resultado = n1 + n2
elif opção == 2:
    n1 = float(input("Digite o número 1: "))
    n2 = float(input("Digite o número 2: "))
    if n2 == 0:
        print("Não é possível fazer essa divisão.")
        exit()
    else:
        resultado = n1/n2    
elif opção == 3:
    n1 = float(input("Valor: "))
    resultado = math.sqrt(n1)
    if n1 < 0:
       print("Não é possível calcular raíz de negativo.")
       exit() 
else:
    print("Opção inválida.")
    exit()