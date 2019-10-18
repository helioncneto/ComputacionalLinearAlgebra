import numpy as np
from functools import reduce

def copiar_lista(lista):
    novo = [[i for i in x] for x in lista]
    return novo

def elimgauss(A, b, withM=False):
    "Essa função realiza a Eliminação Gaussiana de uma Matriz"
    m_dict = dict()
    A_dict = {0: A}
    b_dict = {0: b}
    for rodada in range(1, len(A)):
        A_new = list()
        b_new = list()
        m = list()
        for j in range(len(A)):
            A_list = list()
            if rodada >= j + 1:
                A_new.append(A_dict[rodada - 1][j])
                b_new.append(b_dict[rodada - 1][j])
            else:
                m.append(A_dict[rodada-1][j][rodada-1]/A_dict[rodada-1][rodada-1][rodada-1])
                for i in range(len(A[0])):
                    A_list.append(A_dict[rodada-1][j][i]-m[-1]*A_dict[rodada-1][rodada-1][i])
                A_new.append(A_list)
                b_new.append(b_dict[rodada-1][j] - m[-1] * b_dict[rodada - 1][rodada - 1])
        A_dict[rodada] = A_new
        b_dict[rodada] = b_new
        m_dict[rodada] = m
    if withM:
        return A_dict, b_dict, m_dict
    else:
        return A_dict, b_dict

def subs_regressiva(A, b):
    x = list(range(len(b)))
    for i in range(len(b)-1,-1, -1):
        if i == len(b)-1:
            x[i] = b[i]/A[i][i]
        elif i == len(b)-2:
            x[i] = (b[i]-(A[i][i+1]*x[i+1]))/A[i][i]
        else:
            x[i] = (b[i]-(reduce(lambda p,s: A[i][i+p]*x[i+p]+A[i][i+s]*x[i+s], range(1,len(x)-i))))/A[i][i]
    return x

def permuta_linha(A, b, g):
    if len(A) == len(g):
        A_new = copiar_lista(A)
        b_new = copiar_lista(b)
        for i in range(len(A)):
            if i == g[i]:
                pass
            else:
                A_new[i] = A[g[i]]
                b_new[i] = b[g[i]]
        return A_new, b_new
    else:
        print("O vetor de ordem possui tamanho diferente da Matriz A")

def permuta_coluna(A, x, g):
    A_new = copiar_lista(A)
    for i in range(len(A)):
        if i == g[i]:
            pass
        else:
            for j in range(len(A)):
                A_new[j][i] = A[j][g[i]]
                #print(A[j][g[i]])
                #print(A_new[j][i])

    return A_new

if __name__ == "__main__":
    #'''
    #A = [[1, -1, 2], [2, 1, -1],[-2, -5, 3]]
    #b = [2, 1, 3]
    #x = [1, -1, 0]
    #'''
    '''
    A = [[3, 2, 5], [2, 1, 1], [2, 5, 1]]
    x = [3, 2, 4]
    b = [33, 12, 20]
    '''
    '''
    A = [[2,1,1,0],[4,3,3,1],[8,7,9,5],[6,7,9,8]]
    x = [1, 1]
    b = [1,2,4,5]
    '''

    #dicA, dicB = elimgauss(A, b)
    #print(dicA[len(A)-1])
    #print(dicB[len(b)-1])
    #print(subs_regressiva(dicA[len(A)-1], dicB[len(b)-1]))
    #print(x)
    A = [[1,2,3],[4,5,6],[7,8,9]]
    b = [1,2,3]
    g = [1,0,2]
    print(permuta_coluna(A,b,g))


