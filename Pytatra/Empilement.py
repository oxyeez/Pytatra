import Planchette

def cree(planchette, centre):
	return (planchette, centre, {'masse' : Planchette.longueur(planchette), 'centreGravite' : centre, 'desequilibre' : False})
	'''
		retourne un tuple contenant : une planchette (tuple avec longueur et marges), le centre de l'empilement (donc de la planchette du bas), et un dico contenant :
				-la masse de l'empilement (= à la longueur de la planchette 1 car il n'y en a qu'une seule)
				-le centre de gravité de l'empilement (= au centre de la planchette 1 car il n'y en a qu'une seule)
				-le déséquilibre de l'empilement (True si déséquilibre, False si équilibre)
	'''
def planchette(empilement):
	return empilement[0]		#retourne la première valeur du tuple créé avec la fonction cree(.,.), correspondant à la planchette du bas de l'empilement (le tuple avec longueur et marge)

def centreGeometrique(empilement):
	return empilement[1]		#retourne la deuxième valeur du tuple créé avec la fonction cree(.,.), correspondant au centre de l'empilement

def masse(empilement, valeur=None):
	if valeur != None :			#vérifie si une valeur a été rentrée pour 'valeur'
		empilement[2]['masse'] = valeur		#si une valeur a été rentrée, celle-ci remplace la masse (dans le dico étant en troisième position du tuple empilement)
	return empilement[2]['masse']	#retourne la masse, qu'elle soit nouvelle ou non modifiée

def centreGravite(empilement, valeur=None):
	if valeur != None :			#vérifie si une valeur a été rentrée pour 'valeur'
		empilement[2]['centreGravite'] = valeur		#si une valeur a été rentrée, celle-ci remplace le centre de gravité (dans le dico étant en troisième position du tuple empilement)
	return empilement[2]['centreGravite']		#retourne le centre de gravité, qu'il soit nouveau ou non modifié

def desequilibre(empilement, valeur=None):
	if valeur != None :			#vérifie si une valeur a été rentrée pour 'valeur'
		empilement[2]['desequilibre'] = valeur		#si une valeur a été rentrée, celle-ci remplace la situation de déséquilibre de l'empilement (dans le dico étant en troisième position du tuple empilement)
	return empilement[2]['desequilibre']		#retourne la situation de déséquilibre de l'empilement

def versChaine(empilement):
	numero = str(Planchette.numero(planchette(empilement)))
	mass = str(masse(empilement))
	centre = str(centreGeometrique(empilement))
	centreG = str(centreGravite(empilement))
	if desequilibre(empilement) :
		return 'n°'+numero +' m='+mass+' c='+centre+' g='+centreG+' !'
	else :
		return 'n°'+numero+' m='+mass+' c='+centre+' g='+centreG

	'''
	retourne une chaine de caractère composé de :
		- 'n°' + le numéro de la planchette du bas de l'empilement
		- 'm=' + la masse de l'empilement
		- 'c=' + le centre de la planchette du bas de l'empilement
		- 'g=' + le centre géométrique de l'empilement
		- si l'empilement est en déséquililbre (la valeur True est affcté à 'déséquilibre dans le dico'), on rajoute alors un '!' à la fin de la chaine de caractères

	'''
