import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado.append(palabra)
    return resultado
#PROBLEMA: El problema de esta función estaba en que se generaba la lista resultado cada vez que se entraba al for, por tanto nunca almacenaba las palabras anteriores
#SOLUCION: Se ha definido la lista resultado antes del bucle para que vaya almacenando las palabras


def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    dic = {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }

    clients_list[nif] = dic
    print(clients_list)

#PROBLEMA: Al imprimir el valor de una clase del diccionario nos aparecia un diccionario dentro de otro
#SOLUCION: Se ha creado un diccionario con los valores del cliente y se ha añadido a una lista en la posicion del nif
    

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
            cartas_aleatorias.remove(carta)

    return combinaciones

    
