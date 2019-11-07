import numpy as np

class LinearAlgebra:
    def gauss_jacobi(self, A, b, chute, it=30, tol=0.00000000001):
        x = {0: chute}
        for ep in range(1, it + 1):
            x_ = list()
            for i in range(len(A)):
                soma = 0.0
                for j in range(len(A)):
                    if j != i:
                        soma = soma + A[i][j] * x[ep-1][j]
                x_.append((b[i] - soma) / A[i][i])
            x[ep] = x_[:]
            print((abs(x[ep-1]-x[ep]))/x[ep])#numpy
        return x

    def criterio_linhas(self, A):
        A = np.array(A)
        D = np.diag(A)
        alpha = list()
        linhas = 0

        for i in range(len(A)):
            soma = 0.0
            for j in range(len(A)):
                if j != i:
                    soma = soma + A[i][j]
            alpha.append(soma / D[i])
        for i in alpha:
            if i < 1:
                linhas += 1
            else:
                linhas-=1
        if linhas == len(A):
            return True
        else:
            return False

la = LinearAlgebra()

A = [[9.0, -3.0], [-2.0, 8.0]]
b = [6.0, -4.0]
guess = [0.0, 0.0, 0.0]

mtz = [[10,2,1], [1,5,1], [2,3,10]]
print(la.criterio_linhas(mtz))

t = la.gauss_jacobi(A, b, guess)

#print(t)