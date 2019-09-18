import numpy as np

def elimgauss(A, b):
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
    '''
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


    AA, bb = elimgauss(A, b)
    print(subs_regressiva(AA, bb))
    print(x)

#print(np.dot(A,x)) Multiplicação de matrizes em python