# Importação do CSV
import csv
# Leitura do arquivo
file = open("./college_students.csv", "r")
# Leitura das linhas
lines = csv.reader(file)
# Pula cabeçalho
lines.__next__()
# Inicialização de arrays principais
characteristics = []
results = []
# Loop em todas as linhas traduzindo para as matrizes.
for student_code, discipline_a, discipline_b, discipline_c, idade, state, post_graduation_registered in lines :
    # Seleciona características e converte para inteiro inteligível para o treino
    int_discipline_a = 0
    if discipline_a == "APROVADO" :
        int_discipline_a = 1
    int_discipline_b = 0
    if discipline_b == "APROVADO" :
        int_discipline_b = 1
    int_discipline_c = 0
    if discipline_c == "APROVADO" :
        int_discipline_c = 1
    int_idade = 0
    if int(idade) >= 24 :
        int_idade = 1
    array_state = [0, 0, 1]
    if state == "SC" :
        array_state = [0, 1, 0]
    if state == "RS" :
        array_state = [1, 0, 0]
    # Colocar informações no array de características
    characteristics.append([int_discipline_a, int_discipline_b, int_discipline_c, int_idade] + array_state)
    # Seleciona resultados e converte para inteiro inteligíveis para o treino
    int_post_graduation_registered = 0
    if post_graduation_registered == "SIM" :
        int_post_graduation_registered = 1
    # Colocar resultados no array de resultados
    results.append(int_post_graduation_registered)
    # Usado para razões de debug, printa todos os valores
    print(int_discipline_a, int_discipline_b, int_discipline_c, int_idade, array_state, "-", int_post_graduation_registered)
# Instanciar a biblioteca para chamar o treino
from sklearn.naive_bayes import MultinomialNB
# Define o limite
limit = 150
# Inicializa uma varável com o MultinomialNB
training_model = MultinomialNB()
# Treina o modelo em si
training_model.fit(characteristics[:limit], results[:limit])
# Iniciliza variável de quantidades e número de acertos
quantity = 0
hits = 0
expected_answers = results[:limit]
answers_recieved = training_model.predict(characteristics[:limit])
# print(expected_answers)
# print(answers_recieved)
# print(characteristics)
for answer_recieved in answers_recieved :
    if answer_recieved == expected_answers[quantity] :
        hits = hits + 1
    quantity = quantity + 1
print ("Limite de:",limit, "Porcentagem de sucesso:", float(hits/len(expected_answers))*100, "%")

# 4 - Qual disciplina aprovada tem maior relação com a taxa de sucesso?

# Inicializa as variáveis de contagem
discipline_a_count = 0
discipline_b_count = 0
discipline_c_count = 0
# Inicializa contador de posição
results_read_position = 0
# Percorre o array de características
for characteristic in characteristics :
    if results[results_read_position] == 1 :
        if characteristic[0] == 1 :
            discipline_a_count = discipline_a_count + 1
        if characteristic[1] == 1 :
            discipline_b_count = discipline_b_count + 1
        if characteristic[2] == 1 :
            discipline_c_count = discipline_c_count + 1
    results_read_position = results_read_position + 1
print(discipline_a_count, discipline_b_count, discipline_c_count)
# Comparador de contagem
if discipline_a_count > discipline_b_count :
    # (b <= a) == true
    if discipline_a_count > discipline_c_count :
        print("A disciplina A tem a maior relação.", discipline_a_count)
    else :
        print("A disciplina C tem a maior relação.", discipline_c_count)
else :
    # (a <= b) == true
    if discipline_b_count > discipline_c_count :
        print("A disciplina B tem a maior relação.", discipline_b_count)
    else :
        print("A disciplina C tem a maior relação.", discipline_c_count)
