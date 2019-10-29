import numpy as np
from functools import reduce


def copiar_matriz(lista):
    novo = [[i for i in x] for x in lista]
    return novo


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
        A_new = copiar_matriz(A)
        b_new = b[:]
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
    A_new = copiar_matriz(A)
    x_new = x[:]
    for i in range(len(A)):
        if i == g[i]:
            pass
        else:
            for j in range(len(A)):
                A_new[j][i] = A[j][g[i]]
                x_new[i] = x[g[i]]
    return A_new, x_new


def pivoteamento_parcial(A, col, escala=False):
    g = list(range(len(A)))
    linha = None
    prim = True
    s = list()
    if escala:
        # achar o vetor de s
        for _ in range(len(A)):
            s.append(max(abs(x) for x in A[_]))
    for i in range(col, len(A)):
        if prim:
            if escala:
                maior = abs(A[i][col])/s[i]
            else:
                maior = abs(A[i][col])
            linha = i
            prim = False
        if escala:
            if abs(A[i][col])/s[i] > maior:
                maior = abs(A[i][col])/s[i]
                linha = i
        else:
            if abs(A[i][col]) > maior:
                maior = abs(A[i][col])
                linha = i
    g[col] = linha
    g[linha] = col
    return g


def pivoteamento_completo(A, col):
    g_l = list(range(len(A)))
    g_c = list(range(len(A)))
    linha = None
    coluna = None
    prim = True

    for i in range(col, len(A)):
        for j in range(col, len(A)):
            if prim:
                maior = abs(A[i][j])
                linha = i
                coluna = j
                prim = False
            if abs(A[i][j]) > maior:
                maior = abs(A[i][j])
                linha = i
                coluna = j
    g_l[col] = linha
    g_l[linha] = col
    g_c[col] = coluna
    g_c[coluna] = col
    return g_l, g_c


def sub_matriz(A, prof):
    A_new = list()
    for i in range(prof, len(A)):
        A_new.append([A[i][j] for j in range(prof, len(A))])
    return A_new


def eliminacao_gaussiana(A, b, withM=False, pivoteamento="None"):
    "Essa função realiza a Eliminação Gaussiana de uma Matriz realizando ou não técnica de Pivoteamento"
    m_dict = dict()
    A_dict = {0: A}
    b_dict = {0: b}
    x_dict = {0: list(range(len(A)))}
    for rodada in range(1, len(A)):
        A_new = list()
        b_new = list()
        m = list()
        if pivoteamento == "parcial":
            g = pivoteamento_parcial(A_dict[rodada-1], rodada-1)
            A_dict[rodada-1], b_dict[rodada-1] = permuta_linha(A_dict[rodada-1], b_dict[rodada-1], g)
        if pivoteamento == "parcial_escala":
            g = pivoteamento_parcial(A_dict[rodada - 1], rodada - 1, escala=True)
            A_dict[rodada - 1], b_dict[rodada - 1] = permuta_linha(A_dict[rodada - 1], b_dict[rodada - 1], g)
        if pivoteamento == "completo":
            g_l, g_c = pivoteamento_completo(A_dict[rodada-1], rodada-1)
            A_dict[rodada - 1], b_dict[rodada - 1] = permuta_linha(A_dict[rodada - 1], b_dict[rodada - 1], g_l)
            A_dict[rodada - 1], x_dict[rodada - 1] = permuta_coluna(A_dict[rodada - 1], x_dict[rodada - 1], g_c)
            x_dict[rodada] = x_dict[rodada - 1]
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
        return A_dict, b_dict, x_dict, m_dict
    else:
        return A_dict, b_dict, x_dict

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
    '''
    # Matriz A e b para pivoteamento parcial
    A = [[0, 8, 2],
         [3, 5, 2],
         [6, 2, 8]]
    b = [-7, 8, 26]
    '''
    # Matriz A e b para pivoteamento parcial com escala
    #A = [[2.11, -4.210, 0.921],
         #[4.01, 10.200, -1.120],
         #[1.09, 0.987, 0.832]]
    A = [[10.2, 4.01, -1.12], [0.0, 3.7651078431372547, 0.4587254901960784], [0.0, 0.7019735294117648, 0.9403764705882353]]
    b = [2.01, -3.09, 4.21]
    x = list(range(len(A)))

    dicA, dicB, dicx = eliminacao_gaussiana(A, b, pivoteamento="completo")
    #print(dicA[len(A)-1])
    #print(dicB[len(b)-1])
    #print(dicx)

    #g_l, g_c = pivoteamento_completo(A, 0)
    #A, b = permuta_linha(A, b, g_l)
    #A, x = permuta_coluna(A, x, g_c)

    #print(g_l)
    #print(g_c)

    #print(A)
    #print(x)
    #print(b)

    #fim = subs_regressiva(dicA[len(A)-1], dicB[len(b)-1])
    #print(fim)
    #print(fim)
    #print(x)





