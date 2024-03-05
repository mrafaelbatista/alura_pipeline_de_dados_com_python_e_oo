import json
import csv

from processamento_dados import Dados



def size_data(dados):
    return len(dados)


def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    
    return combined_list
    

def transformando_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponível'))
        dados_combinados_tabela.append(linha)
        
    return dados_combinados_tabela


def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


# Extract

dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.nome_colunas)

dados_empresaB = Dados(path_csv, 'csv')
print(dados_empresaB.nome_colunas)

# Transform
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)


# # Iniciando a leitura
# dados_json = leitura_dados(path_json, 'json')
# nome_colunas_json = get_columns(dados_json)
# tamanho_dados_json = size_data(dados_json)

# print(f"Nome colunas JSON: {nome_colunas_json}")
# print(f"Tamanho dos dados json: {tamanho_dados_json}")

# dados_csv = leitura_dados(path_csv, 'csv')
# nome_colunas_csv = get_columns(dados_csv)
# tamanho_dados_csv = size_data(dados_csv)

# print(f"Nome colunas CSV: {nome_colunas_csv}")
# print(f"Tamanho dados CSV: {tamanho_dados_csv}")


# # Transformação dos dados


# dados_csv = rename_columns(dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)
# print(f"Nome colunas CSV: {nome_colunas_csv}")

# dados_fusao = join(dados_json, dados_csv)
# nome_colunas_fusao = get_columns(dados_fusao)
# tamanho_dados_fusao = size_data(dados_fusao)

# print(nome_colunas_fusao)
# print(tamanho_dados_fusao)

# # Salvando dados 

# dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

# path_dados_combinados = 'data_processed/dados_combinados.csv'

# salvando_dados(dados_fusao_tabela, path_dados_combinados)
# print(path_dados_combinados)