from PrintaGrafo import PrintaGrafo
import csv
import time

#comeca a execucao
ini = time.time()

#armazena o conteudo do arquivo em entrada_csv Ids_Pessoas
entrada_csv = open('dados/ids_pessoas.csv', 'r')
#armazena o conteudo do arquivo em entrada_txt Encontros
entrada_txt = open('dados/encontros.txt', 'r')

#desconsidera as primeiras linhas
next(entrada_txt)
next(entrada_txt)
next(entrada_csv)

dados_tabela = csv.reader(entrada_csv)

# Cria as listas para os vértices e arestas
nodes = []
all_edges = []

for dados in dados_tabela:
    nodes.append(dados[0])

#atribui as arestas a all_edges
for linha in entrada_txt:
    stripped_line = linha.strip()
    line_list = stripped_line.split()
    all_edges.append(line_list)

#converte para lista de tuplas
all_edges = [tuple(l) for l in all_edges]

#chama o construtor do grafo na variavel grafo
grafo = PrintaGrafo(len(nodes) + 1)

#cria as arestas
for u,v in all_edges:
    grafo.add_edge(int(u),int(v))

entrada_csv.close()
entrada_txt.close()

#recebe os componentes conexos
cc = grafo.connectedComponents()

#deleta o primeiro componente(invalido)
del cc[0]

#vetor que armazenará o tamanho dos vértices de cada componente
quantidadeCC = []

for componente in cc:
    quantidadeCC.append(len(componente))

#escreve no arquivo de saída
with open('dados/tabela_saida.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter =',')
    a.writerows(map(lambda x: [x], quantidadeCC))

#calcula o tempo de execução
fim = time.time()

print("Tempo de execuçao (S): ", fim-ini)
