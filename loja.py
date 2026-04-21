# entrada de dados 
qtdHamburguer = int(input("Digite a quantidade de hambúrgueres: "))
qtdBatata = int(input("Digite a quantidade de batatas: "))
qtdRefrigerante = int(input("Digite a quantidade de refrigerantes: "))

#processamento (cálculo da conta)
resultadoConta = (qtdHamburguer * 10) + (qtdBatata * 5) + (qtdRefrigerante * 3)

#saída de dados
print("O valor total da conta é: R$ " + str(resultadoConta))
