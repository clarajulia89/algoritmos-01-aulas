salário = float(input("Digite seu salário: "))
aumento = int(input("Digite o aumento em porcentagem: "))

aumento = aumento/100
aumento_concedido = aumento*salário
novo_salário = salário + salário*aumento

print(f"Aumento baseado na porcentagem passada:{aumento_concedido: .2f}")
print(f"Salário total: {novo_salário: .2f}")
