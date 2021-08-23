import Planchette

def cree(planchette, nombre):
	return [planchette, nombre]	#retourne une liste contenant un type de planchette, suivi du nombre d'exemplaires de ce type

def planchette(exemplaires):
	return exemplaires[0] 		#retourne la première valeur de la liste créee avec la fonction cree(), ce qui correspond au type de planchette

def nombre(exemplaires, valeur=None):
	if valeur != None :	exemplaires[1] = valeur		#si une valeur a été rentrée, celle-ci remplace la précedente valeur
	return exemplaires[1]		#retourne la deuxième valeur de la liste créée avec la fonction cree(), ce qui correspond au nombre de d'exemplaires du type de planchette en question

def retireUn(exemplaires):
	exemplaires[1] -= 1			#remplace le nombre d'exemplaire du type de planchette voulu par une valeur minorée de 1 par rapport à la précédente
	return exemplaires[1]		#retourne le nombre d'exemplaire du type de planchette voulu

def versChaine(exemplaires):
	nbr = str(nombre(exemplaires))
	numero = str(Planchette.numero(planchette(exemplaires)))
	return nbr+'x'+numero
		#retourne une chaine de caractères contenant, le nombre d'exemplaire d'une planchette, le signe 'x', le numéro d'identification du type de planchette
