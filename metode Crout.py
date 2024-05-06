import numpy as np

# Membuat matriks augmented [A|B]
A = np.array([[2, 3, 1],
              [4, 7, 2],
              [-2, 5, 2]])

B = np.array([10, 23, 4])

# Melakukan dekomposisi Crout
def crout_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        # Menghitung nilai pada matriks L
        for i in range(j, n):
            if i == j:
                L[i][j] = 1
            else:
                L[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(j))

        # Menghitung nilai pada matriks U
        for i in range(j, n):
            if i == j:
                U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(j))
            else:
                U[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(j))) / L[j][j]

    return L, U

L, U = crout_decomposition(A)

# Menyelesaikan Ly = B untuk mencari y
def forward_substitution(L, B):
    n = len(B)
    y = np.zeros(n)

    for i in range(n):
        y[i] = (B[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    return y

y = forward_substitution(L, B)

# Menyelesaikan Ux = y untuk mencari x
def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x

x = backward_substitution(U, y)

# Output langkah-langkah penyelesaian
print("Langkah 1: Matriks augmented [A|B]:")
print(np.column_stack((A, B)))

print("\nLangkah 2: Dekomposisi Crout:")
print("Matriks L:")
print(L)
print("Matriks U:")
print(U)

print("\nLangkah 3: Menyelesaikan Ly = B untuk mencari y:")
print("Nilai y:")
print(y)

print("\nLangkah 4: Menyelesaikan Ux = y untuk mencari x:")
print("Nilai x:")
print(x)
