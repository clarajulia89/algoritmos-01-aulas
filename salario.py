# entrada de dados
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))

# processamento
salário_bruto = horas_trabalhadas * valor_hora
ir = salário_bruto * 0.11
inss = salário_bruto * 0.08
sindicato = salário_bruto * 0.05
salário_liquido = salário_bruto - ir - inss - sindicato

# saída de dados
print(f"+ Salário Bruto: R$ {salário_bruto: .2f}")
print(f"- IR (11%): R$ {ir: .2f}")
print(f"- INSS (8%): R$ {inss: .2f}")
print(f"- Sindicato (5%): R$ {sindicato: .2f}")
print(f"= Salário Líquido: R$ {salário_liquido: .2f}")