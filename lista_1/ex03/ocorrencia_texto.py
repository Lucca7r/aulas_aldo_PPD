from collections import Counter

def contar_palavras(texto):
   # Converte o texto para minúsculas
  texto_minusculo = texto.lower()

  # Divide o texto em palavras
  palavras = texto_minusculo.split()

  # Conta o número de ocorrências de cada palavra
  contagem_palavras = Counter(palavras)

  # Retorna o dicionário com a contagem das palavras
  return contagem_palavras

# Exemplo de uso
texto = "Este é um exemplo de texto com algumas palavras repetidas."

contagem_palavras = contar_palavras(texto)

# Imprime a contagem das palavras
for palavra, contagem in contagem_palavras.items():
  print(f"Palavra '{palavra}': {contagem}")
