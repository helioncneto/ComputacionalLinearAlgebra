import numpy as np

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


def elimgauss_0(A, b):
    "Essa função realiza a Eliminação Gaussiana de uma Matriz"
    A1, A2 = list(), list()
    b1, b2 = list(), list()
    A1 = list()
    # Copiando primeira linha
    A1.append([A[0][0],A[0][1],A[0][2]])
    b1.append(b[0])
    # Zerando o primeiro elemento da primeira coluna
    m10 = A[1][0] / A[0][0]
    A1.append([A[1][0]-m10*A[0][0], A[1][1]-m10*A[0][1], A[1][2]-m10*A[0][2]])
    b1.append(b[1]-m10*b[0])
    # Zerando o segundo elemento da primeira coluna
    m20 = A[2][0] / A[0][0]
    A1.append([A[2][0]-m20*A[0][0], A[2][1]-m20*A[0][1], A[2][2]-m20*A[0][2]])
    b1.append(b[2]-m20*b[0])
    # Copiando primeira linha da rodada passada
    A2.append([A1[0][0],A1[0][1],A1[0][2]])
    b2.append(b1[0])
    # Copiando segunda linha da rodada passada
    A2.append([A1[1][0], A1[1][1], A1[1][2]])
    b2.append(b1[1])
    # Zerando o primeiro elemento da segunda coluna
    m21 = A1[2][1] / A1[1][1]
    A2.append([A1[2][0]-m21*A1[1][0],A1[2][1]-m21*A1[1][1], A1[2][2]-m21*A2[1][2]])
    b2.append(b1[2]-m21*b1[1])
    return A2, b2

def subs_regressiva(A, b):
    x = list()
    x2 = b[2]/A[2][2]
    x1 = (b[1]-(A[1][2]*x2))/A[1][1]
    x0 = (b[0]-(A[0][1]*x1 + A[0][2]*x2))/A[0][0]
    x.append([x0, x1, x2])
    return x






if __name__ == "__main__":

    A = np.array([[3, 2, 5],
                  [2, 1, 1],
                  [2, 5, 1]])
    x = np.array([3, 2, 4])
    b = np.array([33, 12, 20])
    '''
    A = np.array([[1, -1, 2],
                  [2, 1, -1],
                  [-2, -5, 3]])
    b = np.array([2, 1, 3])
    x = np.array([1, -1, 0])
    '''


    AA, bb = elimgauss(A, b)
    print(AA)
    print(bb)
    print(subs_regressiva(AA, bb))
    print(x)

#print(np.dot(A,x)) Multiplicação de matrizes em python