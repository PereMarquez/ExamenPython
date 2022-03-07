
    
def test_repartir_cartas():
    #comprobamos que con 1 repetición nos devuelve un diccionario con 1 lista de 5 cartas
    cartas_iniciales = ["reina","guardia","asesino","obispo","alguacil","bufon","contable","adulador","baronesa","cardenal"]
    resultado=repartir_cartas(cartas_iniciales,1)
    assert type(resultado) == dict
    assert type(resultado["repeticion1"]) == list
    assert len(resultado["repeticion1"]) == 5
    
    #comprobamos que con 2 repeticiones nos devuelve un diccionario con 2 listas de 5 cartas
    cartas_iniciales = ["reina","guardia","asesino","obispo","alguacil","bufon","contable","adulador","baronesa","cardenal"]
    resultado=repartir_cartas(cartas_iniciales,2)
    assert type(resultado) == dict
    assert type(resultado["repeticion1"]) == list
    assert type(resultado["repeticion2"]) == list
    assert len(resultado["repeticion1"]) == 5
    assert len(resultado["repeticion2"]) == 5

    #comprobamos que con 3 repeticiones nos devuelve un diccionario con 3 listas de 5 cartas
    cartas_iniciales = ["reina","guardia","asesino","obispo","alguacil","bufon","contable","adulador","baronesa","cardenal"]
    resultado=repartir_cartas(cartas_iniciales,3)
    assert type(resultado) == dict
    assert type(resultado["repeticion1"]) == list
    assert type(resultado["repeticion2"]) == list
    assert type(resultado["repeticion3"]) == list
    assert len(resultado["repeticion1"]) == 5
    assert len(resultado["repeticion2"]) == 5
    assert len(resultado["repeticion3"]) == 5
    