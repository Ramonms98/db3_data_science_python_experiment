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

# Inicilização de array Performance 
performances = []
# Inicilização de array de Preço
prices = []
# Inicialização do array de versões do Android
android_versions = []
# Inicialização do array de cameras
cameras = []
# Incialização do array de baterias
batteries = []
# Inicialização do array de telas
screens = []
# Percorre o array e alimenta arrays individuais para cada atributo
for device in array :
  performances.append(device[0])
  prices.append(device[1])
  android_versions.append(device[2])
  cameras.append(device[3])
  batteries.append(device[4])
  screens.append(device[5])
# Lista máximo, mínimo e diferença na Performance
max_performance = max(performances)
min_performance = min(performances)
performance_difference = max_performance - min_performance
# Lista máximo, mínimo e diferença no Preço
max_price = max(prices)
min_price = min(prices)
price_difference = max_price - min_price
# Lista máximo, mínimo e diferença na Versão do Android
max_android_version = max(android_versions)
min_android_version = min(android_versions)
android_version_difference = max_android_version - min_android_version
# Lista máximo, mínimo e diferença na Câmera
max_camera = max(cameras)
min_camera = min(cameras)
camera_difference = max_camera - min_camera
# Lista máximo, mínimo e diferença na Bateria
max_battery = max(batteries)
min_battery= min(batteries)
battery_difference = max_battery - min_battery
# Lista máximo, mínimo e diferença na tela
max_screen = max(screens)
min_screen= min(screens)
screen_difference = max_screen - min_screen
# Inicialização das variáveis de régua de escala e régua dos atribuitos
scale_ruler = [3, 5, 7, 9]
# Régua de Performance
performance_ruler = []
# Régua de Preço
price_ruler = []
# Régua de versão do Android
android_version_ruler = []
# Régua das câmeras
camera_ruler = []
# Régua das baterias
battery_ruler = []
# Réguas das telas
screen_ruler = []
# Incrementa arrays de régua
for value in range(4) :
  performance_ruler.append(min_performance + value * (performance_difference / 3))
  price_ruler.append(max_price - value * (price_difference / 3))
  android_version_ruler.append(min_android_version + value * (android_version_difference / 3))
  camera_ruler.append(min_camera + value * (camera_difference / 3))
  battery_ruler.append(min_battery + value * (battery_difference / 3))
  screen_ruler.append(min_screen + value * (screen_difference / 3))

### Visualiza Performance
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

### Visualiza Preço
for row in range(5) :
  price = array[row][1]
  scale = 0
  smaller_difference = price_difference
  for quantity in range(4) :
    value = price_ruler[quantity]
    values = [price, value]
    difference = max(values) - min(values)
    if (difference <= smaller_difference) :
      scale = scale_ruler[quantity]
      smaller_difference = difference
  analyzed_array[row].append(scale)

### Visualiza Versão do Android
for row in range(5) :
  android_version = array[row][2]
  scale = 0
  smaller_difference = android_version_difference
  for quantity in range(4) :
    value = android_version_ruler[quantity]
    values = [android_version, value]
    difference = max(values) - min(values)
    if (difference <= smaller_difference) :
      scale = scale_ruler[quantity]
      smaller_difference = difference
  analyzed_array[row].append(scale)

### Visualiza Camera
for row in range(5) :
  camera = array[row][3]
  scale = 0
  smaller_difference = camera_difference
  for quantity in range(4) :
    value = camera_ruler[quantity]
    values = [camera, value]
    difference = max(values) - min(values)
    if (difference <= smaller_difference) :
      scale = scale_ruler[quantity]
      smaller_difference = difference
  analyzed_array[row].append(scale)

### Visualiza Bateria
for row in range(5) :
  print(array[row][4])
  battery = array[row][4]
  scale = 0
  smaller_difference = battery_difference
  for quantity in range(4) :
    value = battery_ruler[quantity]
    values = [battery, value]
    difference = max(values) - min(values)
    if (difference <= smaller_difference) :
      scale = scale_ruler[quantity]
      smaller_difference = difference
  analyzed_array[row].append(scale)

### Visualiza Tela
for row in range(5) :
  screen = array[row][5]
  scale = 0
  smaller_difference = screen_difference
  for quantity in range(4) :
    value = screen_ruler[quantity]
    values = [screen, value]
    difference = max(values) - min(values)
    if (difference <= smaller_difference) :
      scale = scale_ruler[quantity]
      smaller_difference = difference
  analyzed_array[row].append(scale)

# Imprime array analisado
print(analyzed_array)

# Imprime resultados com comparações
result_names = []
result_values = []
for element in analyzed_array :
  print(element)
  result_names.append(element[0])
  total = 1
  for value in element[1:] :
    total = total * value
  result_values.append(total)
best_phone_value = max(result_values)
best_phone_index = result_values.index(best_phone_value)
print(result_names[best_phone_index], best_phone_value)