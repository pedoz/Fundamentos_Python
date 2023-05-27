#imagine que mudaste de país onde o café da manhã é das 7:00 às 8:00, o almoço das 12:00 às 13:00
#e o jantar das 18:00 às 19:00
#Agora, implemente um programa que pede um horário ao usuário, que dará como output:
# - "Hora do cafézin"
# - "Hora do almoço"
# - "Hora da Jantinha"
#Se não for horário de nada, Não de output algum

#Assuma que o usuário irá cooperar e que o horário será de uma das seguintes formas '##:##' ou "#:##"

#assuma que o horário das refeições incluem todos os horários possíveis, por exemplo
#não importa se for '7:00', '7:01', '7:59' ou '8:00', ou qualquer hora entre eles, é hora do cafézin

#Faça seu código com a base abaixo (SEM MODIFICAR NADA FORA DAS FUNÇÕES)
#aonde convert é uma função(que pode ser chamada por 'main'), que converte 'horario', uma string no formato 24h
# para um número correspondente em float
#exemplo:
# se o horário for '7:30', convert deve retornar '7.5' (7.5 horas)

#Docomentação necessária: docs.python.org/3/library/stdtypes.html#string-methods
#lembrando que split separa a string, que podem ser associadas a uma váriavel
#por exemplo, se 'horario' for uma string de valor '7:30', então:
#   horas, minutos = time.split(":")
# onde:
# - '7' = horas
# - '30' = minutos
#LEMBRANDO: 1 hora é igual a 60 minutos
#           ^                 ^         => te liga no hora de converter


def main():
    ...


def convert(horario):
    ...


if __name__ == "__main__":
    main()