#DOCUMENTOS :   STRING      FLOAT       INPUT
#Nos EUA, gorjeta é comum, geralmente é 15% ou mais do valor da comida.

def main():
    dolares = dolares_para_float(input("Quanto foi a refeição "))
    porcentagem = porcentagem_para_float(input("Quanto tu quer dar de gorjeta? "))
    gorjeta = dolares * porcentagem
    print(f"Deixa ${gorjeta:.2f}")


def dolares_para_float(d):
    # fazer
    ...


def porcentagem_para_float(p):
    # fazer
    ...


main()

# TODO dolares_para_float, deve aceitar uma string como input, formatada como '$##.##', onde # é um número decimal (0-9)
# TODO removendo o '$', e retornado o total como 'float'
# EX: foi dado $50.00 como input, ele deve retornar(return) 50.0

# TODO porcentagem_para_float deve aceitar uma str como unput, formatada como '##%', onde # é um número decimal, removendo o '%'
# TODO e retornando a porcentagem como float
# EX: Dado 15% como input, deve retornar 0.15

#Assuma que o usuário vai colocar os input da forma desejada