while True: 
    titulo = input("Digite o título do filme: ")
    genero = int(input("Digite o gênero [1 - Ação, 2 - Drama, 3 - Comédia, 4 - Animação]: "))
    orçamento = float(input("Valor do orçamento (em milhões): "))
    apuraçao = float(input("Valor da apuração (em milhões): "))

# LOGICA DA APLICAÇÃO


opcao = input("Deseja continuar?: [S/N]")
if opcao.lower() == "nao" or opcao.lower() == "não" or opcao.lower() == "n":
    break 
else:
    continue