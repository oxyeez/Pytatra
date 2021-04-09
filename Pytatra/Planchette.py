# Etape 2

Epaisseur = 1

def cree(longueur, marge):
	return (longueur, marge)	#retourne un tuple de la forme : (longueur de la planchette, longueur des marges)

def longueur(planchette):
	return planchette[0]		#retourne la première valeur du tuple créé avec la fonction cree(.,.), ce qui correspond à la longueur de la planchette

def marge(planchette):
	return planchette[1]		#retourne la deuxième valeur du tuple créé avec la fonction cree(.,.), ce qui correspond à la longueur des marges de la planchette

def numero(planchette):
	return marge(planchette)*100+(longueur(planchette)-2*marge(planchette))*10+marge(planchette)
	'''
	retourne le numéro d'identification de la planchette en question
	pour formmer ce numéro on additionne :
		-un nombre de centaines égal à la longueur d'une marge
		-un nombre de dizaines égal à la longueur de la partie centrale (longueur de la planchette - 2 fois la longueur d'une marge)
		-un nombre d'unités égal à la longueur d'une marge
	'''
