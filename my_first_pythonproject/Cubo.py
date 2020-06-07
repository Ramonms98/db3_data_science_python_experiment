import csv

arquivo = open("Cubo.csv", "r") # Abre o arquivo
linhas = csv.reader(arquivo) # Lê os arquivos
linhas.__next__() # Reita os cabeçalhos

# Inicializa o array
vendedores = [] 

# Joga apenas os registros de vendedores num array
for n_venda,vendedor,marca,modelo,v_venda,v_comissao,regiao in linhas :
    vendedores.append(vendedor)

# Inicialização de variáveis
maior_vendedor = 'Nenhum'
contagem_anterior_vendedor = 0

# Compara a repetição de cada vendedor nos registros
for vendedor_compare in vendedores :
    if vendedores.count(vendedor_compare) > contagem_anterior_vendedor :
        contagem_anterior_vendedor = vendedores.count(vendedor_compare)
        maior_vendedor = vendedor_compare
# Imprime o resultado
print(maior_vendedor)