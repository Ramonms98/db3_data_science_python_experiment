
# 1 - preparo os dados ---------------------
f1 = [0,1,0,1] 
f2 = [0,1,1,0]
f3 = [1,1,0,1]
f4 = [1,0,1,0]
f5 = [1,0,1,0]
f6 = [0,0,1,0]
f7 = [0,1,1,1]
f8 = [1,0,1,1]
f9 = [1,1,1,0]
f10 = [1,0,1,1]
#  2 - treino o modelo ---------------------
caracteristicas = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]
classificacao = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]
# importar a biblioteca
from sklearn.naive_bayes import MultinomialNB
# intanciar a biblioteca
modelo = MultinomialNB()
# chamar o treino
modelo.fit(caracteristicas, classificacao)
# 3 - valido o treino
t1 = [1, 1, 1, 0] #1 
t2 = [0, 0, 1, 1] #0
t3 = [1, 1, 0, 0] #1
testes = [t1, t2, t3]

print(modelo.predict(testes))

# 4 - usar o modelo 
# What we do in the shadows - O que fazemos nas sombras
novoFilme = [0, 0, 1, 1]

print(modelo.predict([novoFilme]))