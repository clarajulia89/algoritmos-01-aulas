# ALGORITMO 

# DECLARE avaliação, laboratório, exame: NUMÉRICO (REAL)
        # peso_avaliação, peso_laboratório, peso_exame: NUMÉRICO (INTEIRO)
# INICIO
# peso_avaliacao = 3
#    peso_exame = 5
#    peso_laboratorio = 2

#    ESCREVA "Digite a nota do Laboratório: "
#   LEIA(laboratorio)
#   ESCREVA "Digite a nota do Avaliacao: "
#    LEIA(avalicao)
#   ESCREVA "Digite a nota do Exame: "
#   LEIA(exame)
# media = (avalicao*peso_avaliacao + laboratorio*peso_laboratorio + exame*peso_exame)/(peso_avaliacao + peso_exame + peso_laboratorio)
    
#    ESCREVA "Media = ", media

#    SE (media < 3) ENTAO
#        ESCREVA "Reprovado"
#    SENAO SE (media >= 3) e (media < 5):
#        ESCREVA "Recuperacao"
#    SENAO
#        ESCREVA "Aprovado"
# FIM  

nota1 = float(input("Digite a nota de Trabalho de Laboratório: "))
nota2 = float(input("Digite a nota de Avaliação Semestral: "))
nota3 = float(input("Digite a nota de Exame Final: "))

laboratorio = 2
avaliação = 3
exame = 5

media = (nota1*2) + (nota2*3) + (nota3*exame)/(laboratorio + avaliação + exame)
if (media == 0) and (media <= 2.9): 
    print("Você está reprovado.")
elif (media == 3) and (media <= 4.9):
    print("Você está de recuperação.")
else: 
    print("Você está aprovado.")