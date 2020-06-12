##### MATRIZ UM #####
array = [
  [1,2,3,4,5],
  [6,7,8,9,0],
  [4,2,1,7,8],
  [9,2,2,4,6],
  [9,9,1,1,1] 
]
### qual a soma do valor de cada linha
for linha in range(5):
  somaLinha = 0
  for coluna in range(5):
    valor = array[linha][coluna]
    somaLinha = somaLinha + valor
    print(linha,coluna, valor)
  print("soma da linha " + str(linha) + " :",  somaLinha)
    
### qual a soma do valor de cada coluna
print("L","C","V")
for coluna in range(5):
  somaColuna = 0
  for linha in range(5):
    valor = array[linha][coluna]
    somaColuna = somaColuna + valor
    print(linha,coluna, valor)
  print("soma da coluna " + str(coluna) + ":",  somaColuna)
### qual a soma total array
print("L","C","V")
somaTotal = 0
for coluna in range(5):
  for linha in range(5):
    valor = array[linha][coluna]
    somaTotal = somaTotal + valor
    print(linha, coluna, valor)
print("soma total:",  somaTotal)

### qual a média total array
print("L","C","V")
contElementos = 0
for coluna in range(5):
  for linha in range(5):
    valor = array[linha][coluna]
    contElementos = contElementos + 1
    print(linha, coluna, valor)
print("num elementos:",  contElementos)
media = somaTotal/contElementos
print("media:", media)

### Tarefa 1
# 1. qual a soma da diagonal [0,0] => [4,4] (soma é 14)
x_axis = 0
sum_equal_diagonals = 0
for column in range(5) :
  for row in range(5) :
    if column == row :
      sum_equal_diagonals = sum_equal_diagonals + array[column][row]
print("1-3. Soma das diagonais [0,0] => [4,4]:", sum_equal_diagonals)

# 2. qual a soma da diagonal [0,4] => [4,0] (soma é 26)

sum_different_diagonals = 0
row_2 = 4
column_2 = 0
while column_2 <= 4 and row_2 >= 0  :
  if row_2 + column_2 == 4 :
    sum_different_diagonals = sum_different_diagonals + array[row_2][column_2]
    print(sum_different_diagonals)
  row_2 = row_2 - 1
  column_2 = column_2 + 1
print("1-2. soma da diagonal [0,4] => [4,0]:", sum_different_diagonals)

# 3. qual a coluna com o valor médio mais alto
greater_medium_column = 0
greater_medium_value = 0.0
for column_3 in range(5) :
  column_3_sum = 0
  for row_3 in range(5) :
    column_3_sum = column_3_sum + array[row_3][column_3]
  column_medium = float(column_3_sum / 5)
  if greater_medium_value < column_medium :
    greater_medium_column = column_3
    greater_medium_value = column_medium
print("1-3. Coluna com maior valor médio:", greater_medium_column, "Valor:", greater_medium_value)
   
# 4. qual a linha com o valor médio mais baixo
smaller_medium_row = 0
smaller_medium_value = 2 ** 128
for row_4 in range(5) :
  row_4_sum = 0
  for column_4 in range(5) :
    row_4_sum = row_4_sum + array[row_4][column_4]
  row_medium = float(row_4_sum / 5)
  if smaller_medium_value > row_medium :
    smaller_medium_row = row_4
    smaller_medium_value = row_medium
print("1-4. Linha com menor valor médio:", smaller_medium_row, "Valor:", smaller_medium_value)

##### MATRIZ DOIS #####

array_2 = [
  [0,1,1,0,1,0,1,1,1,0],
  [1,0,0,1,0,1,1,0,0,1],
  [1,0,1,0,1,1,1,0,0,1],
  [1,0,1,0,1,1,0,0,1,1],
  [1,1,0,0,1,0,1,0,1,0],
  [1,0,1,0,1,1,0,0,1,0],
  [0,1,1,0,0,0,1,0,1,0],
  [1,0,0,1,0,1,0,1,0,1],
  [1,0,0,1,0,0,1,0,0,1],
  [1,0,0,1,1,1,1,0,0,1]
]

### Tarefa 2
### Para a matriz2 escreva algoritmos e identifique+

# 1. a soma do valor de cada linha
for row_5 in range(10):
  row_5_sum = 0
  for column_5 in range(10):
    value_5 = array_2[row_5][column_5]
    row_5_sum = row_5_sum + value_5
  print("2-1. Soma da linha " + str(row_5) + " :",  row_5_sum)
# 2. a soma do valor de cada coluna
for column_6 in range(10):
  sum_column_6 = 0
  for row_6 in range(10):
    value_6 = array_2[row_6][column_6]
    sum_column_6 = sum_column_6 + value_6
  print("2-2. Soma da Coluna " + str(column_6) + ":",  sum_column_6)
# 3. a soma total da array
total_sum_7 = 0
for column_7 in range(10):
  for row_7 in range(10):
    value_7 = array_2[row_7][column_7]
    total_sum_7 = total_sum_7 + value_7
print("2-3. Soma total:",  total_sum_7)
# 4. a coluna cuja a soma seja a mais alta
greater_sum_column_2 = 0
greater_sum_value_2 = 0.0
for column_8 in range(10) :
  column_8_sum = 0
  for row_8 in range(10) :
    column_8_sum = column_8_sum + array_2[row_8][column_8]
  if greater_sum_value_2 < column_8_sum :
    greater_sum_column_2 = column_8
    greater_sum_value_2 = column_8_sum
print("2-4. Coluna com maior soma:", greater_sum_column_2, "Valor:", greater_sum_value_2)
# 5. a linha cuja a soma seja a mais baixa
smaller_sum_row_2 = 0
smaller_row_value_2 = 2 ** 128
for row_9 in range(10) :
  row_9_sum = 0
  for column_9 in range(10) :
    row_9_sum = row_9_sum + array_2[row_9][column_9]
  if smaller_row_value_2 > row_9_sum :
    smaller_sum_row_2 = row_9
    smaller_row_value_2 = row_9_sum
print("2-5. Linha com menor soma:", smaller_sum_row_2, "Valor:", smaller_row_value_2)