**Inicio Subtema Datas e Horas** 

Tabela de Horas

<img alt="Colaboratory logo" width="40%" src="https://user-images.githubusercontent.com/54008103/92027902-9233ab80-ed39-11ea-9808-54ee71cf56de.jpg">


A partir da pagina 70 do livro de Python temos o sub tema Data e Horas -  que refere-se ao modulo embutiod chamado datetime com os tipos datetime, date, time. O tipo 
datetime é o que combina informações em date e time e tb é o mais usado.



from datetime import datetime, date, time
#criar uma variave, com alguns dados e converter em data hora
df = datetime(2011,10,29,20,30,21)

# a partir da conversao da variavel para date time e possivel extrair dados de data hora,minutos segundos
print(df.date())
print(df.hour)
print(df.minute)
print(df.second)


#Na instacia datetime podemos extrair os objetos date e time equivalentes chamados os métodos no datetime com mesmo nome.
print(df.date())
print(df.time())

#ExExiste um método que possibilita formatar um datetime chamado strftime
print(df.strftime("%m/%d/%y %H:%M" ))
#ExExiste um método que possibilita formatar um datetime chamado strftime
print(df.strftime("%m/%d/%y %H:%M" ))

#Podemos fazer a diferença entre datas vamos la
#Criar uma nova data com datetime

df2 = datetime(2012,10,29,20,30,21)
print( df, "\n",df2)
delta = df2-df
print(delta)
print(type(delta))

#Podemos fazer a diferença entre datas vamos la
#Criar uma nova data com datetime
#Abaixo refizno comando porem nao usei print e alterei a ata e no retorna da resposta temos
#a saida timedelta que indica ofset de 17 dias e 7200 segundoas

df2 = datetime(2012,11,15,22,30,21)
print( df, "\n",df2)
delta = df2-df
delta
#print(type(delta))
#print(delta)



Tabela de Horas

<img alt="Colaboratory logo" width="50%" src="https://user-images.githubusercontent.com/54008103/92028220-0f5f2080-ed3a-11ea-9602-091cfe490cdf.jpg">


**Fim Subtema Datas e Horas** 

