# esse foi legal nao sabia fazer isso!


from collections import Counter

def contar_palavras(texto):
  texto_minusculo = texto.lower()

  palavras = texto_minusculo.split()

  contagem_palavras = Counter(palavras)

  return contagem_palavras

texto = "Este é um exemplo de texto com algumas palavras repetidas."

contagem_palavras = contar_palavras(texto)

for palavra, contagem in contagem_palavras.items():
  print(f"Palavra '{palavra}': {contagem}")
