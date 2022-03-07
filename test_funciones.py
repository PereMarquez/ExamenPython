from funciones import *
import pytest

#Para ejecutar solo uno de los 3:
#python -m pytest -k "test_encontrar_menores"
def test_encontrar_menores():
    diccionario={
        4:['ERGO','FLOR','TIZA','OPEN','MEAR','BABI','MOTE'],
        5:['MONTA','ETILO','MANDO','PLAZO','RODAL','TORVO','BUZAR','LAUDA'],
        6:['ROGADO','AUNQUE','MELISA','ABINAR','TERMAS','MUEBLE','ORANTE','BELDAR']
    }

    #comprobamos que las palabras con letras anteriores a 'B' son las siguientes
    lista=encontrar_menores(diccionario,'B')
    assert lista == ['AUNQUE','ABINAR']

    #comprobamos que las palabras con letras anteriores a 'J' son las siguientes
    lista=encontrar_menores(diccionario,'J')
    assert lista == ['ERGO','FLOR','BABI','ETILO','BUZAR','AUNQUE','ABINAR','BELDAR']

def test_add_client():
    clients_list = {'45333152F':
                {'name':'Martina',
                 'address':'Calle Mislata, 32',
                 'phone':'+34636961236',
                 'email':'la_martina@gmail.com'}
    }

    #comprobamos que hay 3 clientes después de añadir 2 más, y que los contenidos son los esperados
    add_client(clients_list,'12343555F','Jacinto','Moraira','+34616124513','jacin@gmail.com')
    add_client(clients_list,'20555415M','Jaume','Gandia','+34652226215','soc_choume@gmail.com')
    assert len(clients_list) == 3
    #assert clients_list['12343555F'] == {'name': 'Jacinto', 'address': 'Moraira', 'phone': '+34616124513', 'email': 'jacin@gmail.com'}
    assert clients_list['20555415M'] == {'name': 'Jaume', 'address': 'Gandia', 'phone': '+34652226215', 'email': 'soc_choume@gmail.com'}
    
