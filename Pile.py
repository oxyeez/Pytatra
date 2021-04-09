import Planchette
import Empilement

def cree():
	return [] #retourne une liste vide, représentant une pile vide

def estVide(pile):
	return len(pile) == 0		#retourne True si la condition est vérifiée, c'est à dire si la pile ne compte aucun empilement

def sommet(pile):
	if estVide(pile) :	return None		#retourne None si la pile est vide
	else :	return pile[len(pile)-1]	#si la pile n'est pas vide, retourne l'empilement qui est au sommet de la pile (en position len(pile)-1)

def empile(pile, planchette, decalage):
	if estVide(pile) :	pile.append(Empilement.cree(planchette, decalage))		#si la pile est vide, ajoute un empilement, avec un décalage par rapport au centre de l'écran
	else : pile.append(Empilement.cree(planchette, decalage+Empilement.centreGeometrique(sommet(pile))))	#sinon, ajoute un empilement, avec un décallage par rapport à celui juste en dessous

def versChaine(pile):
	string = '----------------------\n'
	for i in range(len(pile)-1, -1, -1) :
		string += str(Empilement.versChaine(pile[i]))+'\n'
	string += '^^^^^^^^^^^^^^^^^^^^'
	return string
	'''
	création et renvoi d'une chaine de caractères :
		- une ligne de '--' symbolisant le sommet
		- une ligne pour chaque empilement (en utilisant la fonction deu fichie empilement qui permet de créer une chaine de caractères), en commençant par l'empilement du haut, d'où le 'range(len(pile)-1, -1, -1)' qui permet de remonter la liste en partant de la fin
		- une ligne de '^^' symbolisant le bas de la pile
	'''

def empileEtCalcule(pile, planchette, decalage):
	empile(pile, planchette, decalage)
	calculeCentresGravite(pile)
	calculeEquilibre(pile)
		#fonction permettant d'ajouter un nouvel empilement et en même temps, de calculer les nouvelles valeurs de centre de gravité et de masse des autres empilements

def calculeCentresGravite(pile):
	for i in range(len(pile)-2, -1, -1) :
		masse_dessus = Empilement.masse(pile[i+1])
		longueur = Planchette.longueur(Empilement.planchette(pile[i]))
		centre = Empilement.centreGeometrique(pile[i])
		centreG_dessus = Empilement.centreGravite(pile[i+1])

		masse = longueur + masse_dessus
		centreG = (longueur*centre+masse_dessus*centreG_dessus)/masse

		pile[i][2]['masse'] = masse
		pile[i][2]['centreGravite'] = centreG
	'''
	calcul et actualisation des masses et centres de gravités de tous les empilement sauf celui du sommet
	on prend donc chaque empilement un par un en partant de celui du sommet (d'où le 'range(len(pile)-2,-1, -1'), et on effectue les oppérations suivantes :
		- on cherche la masse de l'ensemble des empilement qui sont au dessus de celui avec lequel on travail
		- on cherche la longueur de la planchette qui est à la base de l'empilement avec lequel on travail
		- on cherche le centre de la planchette à la base de l'empilement avec lequel on travail
		- on cherche le centre de gravité de l'empilement au dessus de celui avec lequel on travail
		à partir de ces valeurs qu'on a été cherché :
		- on calcule la nouvelle masse de l'empilement avec lequel on travail
		- on calcule le nouveau centre de gravité de l'empilement avec lequel on travail
		- on remplace ces deux valeurs dans notre empilement
		et on recommence ensuite avec l'empilement juste en dessous
	'''


def calculeEquilibre(pile):
	for i in range(len(pile)-2, -1, -1) :
		centreG_dessus = Empilement.centreGravite(pile[i+1])
		centre = Empilement.centreGeometrique(pile[i])
		longueur = Planchette.longueur(Empilement.planchette(pile[i]))
		if abs(centreG_dessus-centre) > longueur/2 :
			pile[i+1][2]['desequilibre'] = True
	'''
	pour chaque empilement, on vérifie s'il est toujours en équilibre ou non
	comme précédement, on part de l'empilement du sommet, vers l'empilement le plus en bas, sans s'occuper de celui du sommet
	et pour chaque empilement, on vérifie si le centre de gravité de l'empilement avec lequel on travail dépasse un des bords de l'empilement d'au dessus
	si c'est le cas, on affecte à 'déséquilibre' (dans le dico de l'empilement avec lequel on travail) la valeur 'True'
	'''