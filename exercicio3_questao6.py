def valor_conta (consumo_mensal):
    if (consumo_mensal <= 100):
        return consumo_mensal*0.5
    else:
        kwh_diferença = consumo_mensal - 100
        return (100 * 0.5) + (kwh_diferença * 0.75)
    
def main():
    kwh_mensal = float(input("Digite a quantidade de kWh consumida no mês: "))

    resultado = valor_conta (kwh_mensal)

    print(f"O valor da sua conta é: {resultado}")

main()