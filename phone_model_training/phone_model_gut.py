# O objetivo desse código é encontrar as respostas específicas para esse cenário, 
# Inicialização de variáveis com o array de smartphones escolhidos
zenfone = [7.2, 1700, 9, 6.2, 3300, 8.5]
galaxy_s9 = [8.9, 2089, 10, 6.0, 3000, 9.4]
motorola_moto_g = [7.2, 1136, 10, 7.2, 3000, 8.5]
galaxy_note9 = [9.0, 3199, 10, 6.4, 4000, 9.3]
galaxy_j7 = [6.3, 1000, 9, 5.5, 3600, 8.5]

# Joga todos os valores em um array
array = [zenfone, galaxy_s9, motorola_moto_g, galaxy_note9, galaxy_j7]
analyzed_array = [
  ["Zenfone"], ["Samsung Galaxy S9"], ["Motorola Moto G7 Plus"], ["Samsung Galaxy Note 9"], ["Samsung Galaxy J7 Pro"]   
]

# Performance 
performances = []
for device in array :
  performances.append(device[0])
max_performance = max(performances)
min_performance = min(performances)
performance_difference = max_performance - min_performance
step = performance_difference / 3
scale_ruler = [3, 5, 7, 9]
performance_ruler = []
for value in range(4) :
  performance_ruler.append(min_performance + value * step)
for row in range(5) :
  performance = array[row][0]
  scale = 0
  smaller_difference = performance_difference
  for quantity in range(4) :
    value = performance_ruler[quantity]
    values = [performance, value]
    difference = max(values) - min(values)
    if (difference <= smaller_difference) :
      scale = scale_ruler[quantity]
      smaller_difference = difference
  analyzed_array[row].append(scale)
print(analyzed_array)
print(scale_ruler)
print(performance_ruler)