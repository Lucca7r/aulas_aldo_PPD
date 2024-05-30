import numpy as np
def calcular_transposta(matriz):


  matriz_transposta = matriz.T

  return matriz_transposta

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_transposta = calcular_transposta(matriz)
print(matriz_transposta)
