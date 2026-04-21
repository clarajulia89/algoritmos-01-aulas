import math
a = float(input("Digite um número para a: "))  
b = float(input("Digite um número para b: ")) 
c = float(input("Digite um número para c: "))

if a == 0:
   print("Não é uma equação de 2° grau.")
   exit()
else:
   delta = b**2 - (4 * a * c)
   print(f"Valor do delta : {delta}")
   if (delta < 0): 
      print("Não há raíz real.")
      exit()
   elif (delta == 0):
      x1 = (-b + math.sqrt(delta))/(2 * a)
      print(f"Raíz da equação: {x1}")
   else: 
      x1 = (-b + math.sqrt(delta))/(2 * a)
      x2 = (-b + math.sqrt(delta))/(2 * a)
      
      