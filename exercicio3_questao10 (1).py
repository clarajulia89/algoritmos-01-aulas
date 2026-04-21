def calculo_salario_liquido (salario_bruto): 
    desconto_inss = salario_bruto*0.08
    print(f"Desconto de R$: {desconto_inss}")
    salario_liquido = salario_bruto - desconto_inss
    return salario_liquido

def main ():
    salario_bruto = float(input("Digite o salário bruto: "))
    salario_liquido = calculo_salario_liquido (salario_bruto)
    print(f"O salário líquido é: {salario_liquido: .2f}")

main()    