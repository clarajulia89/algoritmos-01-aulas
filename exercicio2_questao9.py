# ALGORITMO atualização_preço

# DECLARE preço_antigo, preço_atualizado: NUMERICO

# INICIO
    # ESCREVA "Digite o valor do preço antigo: "
    # LEIA (preço_antigo)

    # SE (preço_antigo <= 50) ENTAO
       # preço_atualizado = preço_antigo*1.05
    # SENAO SE (preço_antigo > 50 e preço_antigo <= 100) ENTAO
       # preço_atualizado = preço*1.1
    # SENAO
       # preço_atualizado = preço_antigo*1.15
    # ESCREVA "Valor atualizado: " + preço_atualizado 
# FIM

preço_antigo = float(input("Digite o valor do preço antigo: "))
preço_atualizado = 0
if (preço_antigo <= 50):
    preço_atualizado = preço_antigo*1.05
elif (preço_antigo > 50) and (preço_antigo <= 100):
    preço_atualizado = preço_antigo*1.1
else:
    preço_atualizado = preço_antigo*1.15

print(f"Valor atualizado: {preço_atualizado: .2f}")