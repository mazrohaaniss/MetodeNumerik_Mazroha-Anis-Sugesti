import numpy as np

# Langkah 1: Mendefinisikan matriks koefisien A dan vektor konstanta B
A = np.array([[2, 3, -1],
              [1, -2, 2],
              [3, 2, -4]])

B = np.array([7, 3, 1])

# Menampilkan matriks koefisien A dan vektor konstanta B
print("Langkah 1: Matriks koefisien A dan vektor konstanta B")
print("Matriks koefisien A:")
print(A)
print("\nVektor konstanta B:")
print(B)

# Langkah 2: Mencari invers dari matriks A
A_inv = np.linalg.inv(A)

# Menampilkan invers dari matriks A
print("\nLangkah 2: Mencari invers dari matriks A")
print("Invers dari matriks A:")
print(A_inv)

# Langkah 3: Mengalikan invers dari matriks A dengan vektor B untuk mendapatkan vektor solusi X
X = np.dot(A_inv, B)

# Menampilkan vektor solusi X
print("\nLangkah 3: Mengalikan invers dari matriks A dengan vektor B untuk mendapatkan vektor solusi X")
print("Vektor solusi X:")
print(X)

# Menampilkan solusi dari sistem persamaan linear
print("\nLangkah 4: Solusi dari sistem persamaan linear")
print("x =", X[0])
print("y =", X[1])
print("z =", X[2])
