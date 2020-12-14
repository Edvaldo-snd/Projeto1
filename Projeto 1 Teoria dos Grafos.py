    #Importa o Igraph, biblioteca utilizada para trabalhar com grafos
from igraph import *


def criaMultiset(grafo: Graph):
        #Para cada vertice
    for i in range(grafo.vcount()):
            #listaAux recebe todos os vizinhos do vertice i
        listaAux = grafo.neighbors(i)
            #insere os valores dos labels dos vizinhos para a lista do vertice
        grafo.vs[i]["listaLabel"] = []
        for j in listaAux:
            grafo.vs[i]["listaLabel"].append(grafo.vs[j]["label"])

    #Procura o maior valor para montar a lista com a quantidade de cada label
def encontraMaior(grafo: Graph):
    maior=0
    totalV = grafo.vcount()
    for i in range(totalV):
        if maior < grafo.vs[i]["label"]:
            maior = grafo.vs[i]["label"]
    return maior

    #Conta a quantidade de cada label no grafo
def contaLabels(grafo: Graph, maior:int):
    lista = [0] * (maior+1)
    for i in range(grafo.vcount()):
        lista[grafo.vs[i]["label"]] = lista[grafo.vs[i]["label"]] + 1
    return lista

    #compara cada lista de labels de cada grafo
def comparaGrafos(grafo1: Graph, grafo2:Graph):
    maior1=encontraMaior(grafo1)
    maior2=encontraMaior(grafo2)
        #se os dois possuem o mesmo valor maior, é possivel que sejam iguais
    if maior1==maior2:
        lista1 = contaLabels(grafo1, maior1)
        lista2 = contaLabels(grafo2, maior2)

        if(lista1==lista2):
            print("-----------Não podemos afirmar que não são isomorfos-----------")
        else:
            print("-----------Os grafos não são isomorfos-----------")
            exit()
    else:
        print("-----------Os grafos não são isomorfos-----------")
        exit()

    comprime(grafo1)
    comprime(grafo2)

    #Unifica todos os labels em apenas 1 valor, utilizando hash
def comprime(grafo: Graph):
    for i in range(grafo.vcount()):
        grafo.vs[i]["listaLabel"].sort()
        grafo.vs[i]["label"] = abs(hash(str(grafo.vs[i]["listaLabel"]))%100)

    #Função inicial que atribui o label para cada vertice, sendo esse label
    #o grau do vertice
def PrimeiroLabel(grafo:Graph):
    for i in range(grafo.vcount()):
        grafo.vs[i]["label"] = int(grafo.degree(i))

grafo1 = Graph(directed=False)
grafo2 = Graph(directed=False)


    #Entradas para o primeiro grafo
numeroVertices1, numeroArestas1 = input().split(" ")

numeroVertices1 = int(numeroVertices1)
numeroArestas1 = int(numeroArestas1)

grafo1.add_vertices(numeroVertices1)

for i in range(numeroArestas1):
    auxA1, auxA2 = input().split(" ")
    auxA1 = int(auxA1)
    auxA2 = int(auxA2)
    grafo1.add_edges([(auxA1, auxA2)])

    #Entradas para o segundo grafo
numeroVertices2, numeroArestas2 = input().split(" ")

numeroVertices2 = int(numeroVertices2)
numeroArestas2 = int(numeroArestas2)

grafo2.add_vertices(numeroVertices2)

    #Lembrando que o grafo não é direcionado

for i in range (numeroArestas2):
    auxA1,auxA2 = input().split(" ")
    auxA1 = int(auxA1)
    auxA2 = int(auxA2)
    grafo2.add_edges([(auxA1, auxA2)])


if numeroArestas2 != numeroArestas1 or numeroVertices2 != numeroVertices1:
    print("Os grafos não são isomorfos, número de arestas ou vértices diferente")


PrimeiroLabel(grafo1)
PrimeiroLabel(grafo2)

for i in range(numeroVertices1):
    criaMultiset(grafo1)
    criaMultiset(grafo2)
    comparaGrafos(grafo1, grafo2)