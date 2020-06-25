# Inicializa os arrays
carateristicasFilmes = [
  [1,0,1,1,1],
  [0,0,1,1,1],
  [1,1,0,1,1],
  [0,1,0,1,1],
  [1,1,1,0,1],
  [0,1,1,0,1],
  [0,0,1,1,0],
  [1,0,1,0,1],
  [1,0,0,1,1],
  [0,0,0,1,1],
  [1,1,0,0,1],
  [0,1,0,0,1]
]
resultados = [
  1,0,1,1,0,0,1,1,0,0,1,1
]

# Importa biblioteca sklearn.naive_bayes
from sklearn.naive_bayes import MultinomialNB

# Define limite
limite = 150

# Define modelo de treino
modelo_treino = MultinomialNB()
# Treina o modelo
modelo_treino.fit(carateristicasFilmes[:limite], resultados[:limite])

# Imprime os resultados
print("0, 0, 0, 0, 0:", modelo_treino.predict([[0, 0, 0, 0, 0]]))
print("1, 1, 1, 1, 1:", modelo_treino.predict([[1, 1, 1, 1, 1]]))