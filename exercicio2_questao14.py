# ALGORITMO calculadora_basica

# DECLARE opção: NUMERICO (INTEIRA)
        # num1, num2, num3: NUMERICO (REAL)

#INICIO
# ESCREVA "Digite uma das opções (1 - somar, 2 - subtrair, 3 - multiplicar, 4 - dividir) "
# LEIA (opção)
# ESCREVA "Digite o primeiro valor: "
# LEIA (num1)
# ESCREVA "Digite o segundo valor: "
# LEIA (num2)

# resultado = 0
# SE (opção = 1) ENTAO
    # resultado = num1 + num2
# SE (opção = 2) ENTAO
    # resultado = num1 - num2
# SE (opção = 3) ENTAO
    # resultado = num1*num2
# SE (opção = 4) ENTAO 
    # SE (num2 = 0) ENTAO
        # ESCREVA "Não existe divisão por zero."
    # SENAO
        # resultado = num1/num2
# SENAO
    # ESCREVA "Opção inválida."
# ESCREVA "Valor da operação = " + resultado

#FIM
opção = int(input("Digite uma das opções " \
"(1 - somar, 2 - subtrair, 3 - multiplicar, 4 - dividir): "))
num1 = float(input("Digite o primeiro valor: "))
num2 = float (input("Digite o segundo valor: "))

resultado = 0
flag = False

if (opção == 1):
    resultado = num1 + num2
elif (opção == 2):
    resultado = num1 - num2
elif (opção == 3):
    resultado = num1*num2
elif (opção == 4):
    if (num2 == 0):
        print("Não existe divisão por zero.")
        flag = True
    else: 
        resultado = num1/num2
else:
    print("Opção inválida.")
    flag = True

if flag:
    print("Fim do programa")
else:
    print(f"O resultado é: {resultado}")
