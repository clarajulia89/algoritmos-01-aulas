# entrada de dados 
nota1 = float(input("Digite sua 1° nota: "))
nota2 = float(input("Digite sua 2° nota: "))
nota3 = float(input("Digite sua 3° nota: "))
trabalho_de_lab = 2
avaliação_semestral = 3
exame_final = 5

# processamento 
media = ((nota1 * trabalho_de_lab) + (nota2 * avaliação_semestral) + (nota3 * exame_final))/(trabalho_de_lab + avaliação_semestral + exame_final)

print(f"Sua média é: {media: .2f}")

# saída de dados 
if (media >= 8): 
   print("Conceito A")
elif (media < 8) and (media >= 7):
   print("Conceito B")
elif (media < 7) and (media >= 6):
   print("Conceito C")
elif (media < 6) and (media >= 5):
   print("Conceito D")
else:
   print("Conceito E")       
   


