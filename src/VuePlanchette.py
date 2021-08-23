from tkinter import *

import Fenetre
import Planchette

#Définition des couleurs des joueurs
CouleurJoueur1 = '#FFDCB3'

CouleurJoueur2 = '#B3D6FF'

Facteur = 10 # 1 cm = 10 pixels

def pixels(cm):
	return round(Facteur*cm)	#retourne une valeur, en nombre de pixel, après convertion à partir d'une valeur en cm 

def dessine(fenetre, planchette, x0, y0, couleur):
	longueur = pixels(Planchette.longueur(planchette))
	marge = pixels(Planchette.marge(planchette))
	epaisseur = pixels(Planchette.Epaisseur)

	Fenetre.toile(fenetre).create_rectangle(x0, y0, x0+longueur, y0+epaisseur, fill = 'white')
	Fenetre.toile(fenetre).create_rectangle(x0+marge, y0, x0+longueur-marge, y0+epaisseur, fill = couleur)
	
	'''
	crée 2 rectangles l'un sur l'autre :
		- le premier représente la planchette en entière : on crée donc un rectangle avec le coin suppérieur gauche aux coordonnées (x0, y0), et le coin inférieur droit aux coordonnées (x0 + longueur de la planchette, y0 + hauteur de la planchette)
		- le deuxième représente la partie centrale de la planchette : on crée donc un rectangle avec le coin suppérieur gauche aux coordonnées (x0 + longueur de la marge, y0), et le coin inférieur droit aux coordonnées (x0 + longueur de la planchette - longueur de la marge, y0 + hauteur de la planchette)
			ce deuxième rectangle est de la couleur donnée en argument de la fonction
	'''

	Fenetre.toile(fenetre).create_polygon(x0, y0, x0+5, y0-5, x0+5+longueur, y0-5, x0+longueur, y0, fill = '#EAEAEA', outline = 'black')
	Fenetre.toile(fenetre).create_polygon(x0+longueur, y0, x0+5+longueur, y0-5, x0+5+longueur, y0-5+epaisseur, x0+longueur, y0+epaisseur, fill = '#A7A7A7', outline = 'black')
	Fenetre.toile(fenetre).create_polygon(x0+marge, y0, x0+marge+5, y0-5, x0+longueur-marge+5, y0-5, x0+longueur-marge, y0, fill = couleur, outline = 'black')

	'''
	gère la perspective des planchettes
	pour chaque planchette on crée 3 polygones supplémentaires:
		- un premier au dessus du rectange représentant la face avant de la planchette, qui représente la face supérieur
		- un deuxième à droite du rectangle représentant la face avant de la planchette, qui représent la face de droite
		- un troisième au dessus du rectanle représentant la face avant de la planchette, plus petit que le premier et d'une autre couleur, qui représnete la partie centrale de la planchette
	'''
