Na pagina 70 do livro de Python temos o sub tema Data e Horas - que refere-se ao modulo embutiod chamado datetime com os tipos datetime, date, time. O tipo datetime é o que combina informações em date e time e tb é o mais usado.
from datetime import datetime, date, time
#criar uma variave, com alguns dados e converter em data hora
df = datetime(2011,10,29,20,30,21)

# a partir da conversao da variavel para date time e possivel extrair dados de data hora,minutos segundos
print(df.date())
print(df.hour)
print(df.minute)
print(df.second)
