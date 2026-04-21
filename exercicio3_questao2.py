def converterTempo(horas, tipo):
    if(tipo == "h"):
        return horas
    elif (tipo == "m"):
        return horas*60
    elif (tipo == "s"):
        return horas*60*60
    else: 
        print("Tipo inválido.")
        return 0
    
def main():
    horas = float(input("Digite a quantidade de horas: "))
    tipo = input("Digite o tipo de hora: h = horas, m = minutos e s = segundos: ")

    resultado = converterTempo(horas, tipo)

    print(f"Conversão de {horas} para {tipo} = {resultado}")

main ()    


