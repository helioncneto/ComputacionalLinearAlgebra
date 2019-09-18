import numpy as np

def elimgauss(A, b):
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

    return A_dict, b_dict






def subs_regressiva(A, b):
    x = list()

if __name__ == "__main__":
    A = np.array([[1, -1, 2],
                  [2, 1, -1],
                  [-2, -5, 3]])
    b = np.array([2, 1, 3])
    x = np.array([1, -1, 0])

    print(elimgauss(A,b))
