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
            diff_x = 0.0
            old_x = 0.0
            for i in range(len(x[ep])):
                diff_x = diff_x + abs(x[ep][j] - x[ep-1][j])
                old_x = old_x + abs(x[ep-1][j])
            if old_x == 0.0:
                old_x = 1.0
            norm = diff_x / old_x
            if norm < tol:
                return x
        return x

    def gauss_seidel(self, A, b, chute, it=30, tol=0.00000000001):
        x = {0: chute}
        for ep in range(1, it + 1):
            x_ = list()
            for i in range(len(A)):
                soma = 0.0
                for j in range(len(A)):
                    if j != i:
                        if i < 1:
                            soma = soma + A[i][j] * x[ep - 1][j]
                        else:
                            if j < i:
                                #Faz a equacao com o x atualizado
                                soma = soma + A[i][j] * x_[j]
                            else:
                                # Faz a equacao com o x do chute
                                soma = soma + A[i][j] * x[ep - 1][j]
                x_.append((b[i] - soma) / A[i][i])
            x[ep] = x_[:]
            diff_x = 0.0
            old_x = 0.0
            for i in range(len(x[ep])):
                diff_x = diff_x + abs(x[ep][j] - x[ep - 1][j])
                old_x = old_x + abs(x[ep - 1][j])
            if old_x == 0.0:
                old_x = 1.0
            norm = diff_x / old_x
            if norm < tol:
                return x
        return x

    def criterio_linhas(self, A):
        alpha = list()
        linhas = 0

        for i in range(len(A)):
            soma = 0.0
            for j in range(len(A)):
                if j != i:
                    soma = soma + A[i][j]
            alpha.append(soma / A[i][i])
        for i in alpha:
            if i < 1:
                linhas += 1
            else:
                linhas-=1
        if linhas == len(A):
            return True
        else:
            return False

    def criterio_sassenfeld(self, A):
        beta = list()
        linhas = 0

        for i in range(len(A)):
            soma = 0.0
            for j in range(len(A)):
                if j != i:
                    if i < 1:
                        #primeiro beta
                        soma = soma + A[i][j]
                    else:
                        if j < i:
                            #faz a equacao multiplicando pelo beta
                            soma = soma + A[i][j]* beta[j]
                        else:
                            #faz a soma sem o beta
                            soma = soma + A[i][j]
            beta.append(soma / A[i][i])
        for i in beta:
            if i < 1:
                linhas += 1
            else:
                linhas -= 1
        if linhas == len(A):
            return True
        else:
            return False

la = LinearAlgebra()

A = [[9.0, -3.0], [-2.0, 8.0]]
b = [6.0, -4.0, 2]
guess = [0.0, 0.0]

A2 = [[9.0, -3.0, 1], [-2.0, 8.0, 1],[1,1,1]]
b2 = [6.0, -4.0, 2]
guess2 = [0.0, 0.0, 0.0]

mtz = [[10,2,1], [1,5,1], [2,3,10]]
print(la.criterio_linhas(A))
print(la.criterio_sassenfeld(A))

t = la.gauss_seidel(A, b, guess, it=50)

print(t)