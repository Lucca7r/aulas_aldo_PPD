import numpy
def def_vetor(vetor):
    vetor_ordenado = vetor.copy()
    
    vetor_ordenado = numpy.sort(vetor_ordenado)
    
    return vetor_ordenado
      
tamanho_vetor = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(tamanho_vetor):
    valor = int(input("Digite o valor {} do vetor: ".format(i + 1)))
    vetor.append(valor)

ordenado = def_vetor(vetor)

print(ordenado)
