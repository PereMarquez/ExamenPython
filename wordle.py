import random

def choose_secret(filename):
  """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
  Args:
    filename: El nombre del fichero. Ej. "palabras_reduced.txt"
  Returns:
    secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
  """
  f = open(filename, mode="rt", encoding="utf-8")

  lista_lineas = f.readlines()

  longitud_fichero = len(lista_lineas)

  if longitud_fichero == 0:
    raise ValueError("Archivo vacio")
  
  indice = random.randint(0,longitud_fichero)

  secret = lista_lineas[indice].upper()

  return secret


def compare_words(word, secret):
  """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
  Args:
    word: Una palabra. Ej. "CAMPO"
    secret: Una palabra. Ej. "CREMA"
  Returns:
    same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
    same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
  """
  word = word.upper()
  secret = secret.upper()

  if len(word) != len(secret):
    raise ValueError("Las palabras no tienen la misma longitud")

  same_position = 0
  same_letter = 0
  for letra_word in word:
    for letra_secret in secret:
      if letra_word == letra_secret:
        pos_letra_word = word.index(letra_word)
        pos_letra_secret = secret.index(letra_secret)
        same_letter += 1
        if pos_letra_word == pos_letra_secret:
          same_position +=1

  return same_letter, same_position


def print_word(word, same_letter_position, same_letter):
  """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
  Args:
    word: Una palabra. Ej. "CAMPO"
    same_letter_position: Lista de posiciones. Ej. [0]
    same_letter: Lista de posiciones. Ej. [1,2]
  Returns:
    transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
  """
  transformed=""
  for letra_word in word:
    

print(word)
    
def choose_secret_advanced():
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
 
def check_valid_word():
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """

"""
if __name__ == "__main__":
    secret=choose_secret()
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words()
        resultado=print_word()
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
"""