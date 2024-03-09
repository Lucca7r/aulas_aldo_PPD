def contar_numeros(vetor):

  positivos = 0
  negativos = 0
  zeros = 0

  for numero in vetor:
    if numero > 0:
      positivos += 1
    elif numero < 0:
      negativos += 1
    else:
      zeros += 1

  return positivos, negativos, zeros

vetor = []
tamanho_vetor = int(input("Digite o tamanho do vetor: "))
for i in range(tamanho_vetor):
    vetor.append(int(input(f"Digite o valor {i + 1} do vetor: ")))

positivos, negativos, zeros = contar_numeros(vetor)

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")
