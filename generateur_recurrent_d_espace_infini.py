def generateur_recurrent_d_espace(unit_de_dimension, coordonnee, dimension):
    for unit in unit_de_dimension:
        if len(coordonnee)+1 < dimension:
            for y in generateur_recurrent_d_espace(unit_de_dimension, coordonnee + str(unit), dimension):
                yield y
        elif len(coordonnee)+1 == dimension:
            yield coordonnee + str(unit)

def generateur_recurrent_d_espace_infini():
	i = 0
	while True:
		i = i + 1
		for x in generateur_recurrent_d_espace([x for x in range(1, i)],  "", i):
			yield x
