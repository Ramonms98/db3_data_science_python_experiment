import csv 
arquivo = open("./teste.csv","r") # read 
linhas = csv.reader(arquivo)
linhas.__next__() 

caracteristicas = []
resultados = []
# venda boa comissao menor que 5%
for n_venda,vendedor,marca,modelo,v_venda,v_comissao,regiao in linhas:
  # vN, vB, vC
  v = []
  if vendedor == "Ninja":
    v = [1,0,0]
  if vendedor == "Bob":
    v = [0,1,0]
  if vendedor == "Chico":
    v = [0,0,1]
  # mC, mF, mV, mF
  m = []
  if marca == "Chevrolet":
    m = [1,0,0,0]
  if marca == "Ford":
    m = [0,1,0,0]
  if marca == "Volkswagen":
    m = [0,0,1,0]
  if marca == "Fiat":
    m = [0,0,1,0]

  # rS, rN, rL, rO, rC
  r = []
  if regiao == "Sul":
    r = [1,0,0,0,0] 
  if regiao == "Norte":
    r = [0,1,0,0,0]  
  if regiao == "Leste":
    r = [0,0,1,0,0]  
  if regiao == "Oeste":
    r = [0,0,0,1,0]  
  if regiao == "Centro":
    r = [0,0,0,0,1]  

  resultado = 0
  if float(v_comissao)/float(v_venda)*100 > 9:
    resultado = 1

  caracteristicas.append(v + m + r)
  resultados.append(resultado)


from sklearn.naive_bayes import MultinomialNB
# intanciar a biblioteca
modelo = MultinomialNB()
# chamar o treino
modelo.fit(caracteristicas[:80], resultados[:80])

cont = 0
numAcertos = 0

respostasEsperadas = resultados[80:]
respostasRecebidas = modelo.predict(caracteristicas[80:])
for respostaRecebida in respostasRecebidas:
  if respostaRecebida == respostasEsperadas[cont]:
    numAcertos = numAcertos + 1
  cont = cont + 1 
print(numAcertos/len(respostasEsperadas)*100)


# criar 
# novaVenda = [0,1,0,1,0,0,1,0,0,0,0,1]
#novaVenda2 = [1,0,0,1,0,0,1,0,0,0,0,1]
# Vendas criadas pelo aluno
venda_criada1 = [0,0,1,0,1,0,0,0,0,0,0,1]
venda_criada2 = [1,0,0,1,0,0,0,0,1,0,0,0]
venda_criada3 = [0,1,0,0,1,0,0,0,0,1,0,0]
venda_criada4 = [1,0,0,0,0,1,0,0,0,0,0,1]
venda_criada5 = [0,1,0,0,0,1,0,0,0,0,1,0]

print(modelo.predict([venda_criada1,venda_criada2,venda_criada3,venda_criada4,venda_criada5]))
