from tkinter import *

import Planchette
import Empilement
import Fenetre
import VuePlanchette

def dessine(fenetre, pile):
	largeur_fen = Fenetre.largeur(fenetre)
	hauteur_fen = Fenetre.hauteur(fenetre)
	epaisseur = Planchette.Epaisseur
	couleur = VuePlanchette.CouleurJoueur1

	for i in range(len(pile)) :
		planchette = Empilement.planchette(pile[i])
		centre = Empilement.centreGeometrique(pile[i])
		longueur = Planchette.longueur(planchette)
		centreG = Empilement.centreGravite(pile[i])

		x0 = largeur_fen/2 + VuePlanchette.pixels(centre-longueur/2)
		y0 = hauteur_fen-40-VuePlanchette.pixels((i+1)*epaisseur)
		
		VuePlanchette.dessine(fenetre, planchette, x0 , y0, couleur)

		if couleur == VuePlanchette.CouleurJoueur1 : couleur = VuePlanchette.CouleurJoueur2
		else : couleur = VuePlanchette.CouleurJoueur1

		x_croix = largeur_fen/2 + VuePlanchette.pixels(centreG)
		y_croix = hauteur_fen-40-VuePlanchette.pixels((i+0.5)*epaisseur)
		
		if Empilement.desequilibre(pile[i]) == True :
			dessine_croix(fenetre, '#FF3200', x_croix, y_croix)

		else :
			dessine_croix(fenetre, '#4EAC5B', x_croix, y_croix)
	'''
	On passe en revue chaque empilement de la pile, et pour chacun on effectu ce qui suit
	
	Pour définir les coordonnées du coin supérieur gauche de la planchette qu'on veut afficher :
		x0 = largeur de la fenetre divisé par 2 (pour avoir le centre de la fenetre) 
				+ le centre de la planchette du bas de l'empilement (ajout du décallage par rapport au centre de la fenetre) 
					- la moitié de la longueur de la planchette (car la fonction qui affiche la planchette prend pour coordonnées le coin supérieur gauche)
		y0 = hauteur de la fenetre - 40 pixels - le nombre de planchettes déjà affichées multiplié par l'épaisseur
	
	On utilise donc la fonction qui affiche la planchette, en lui donnant les coordonnées calculées précédement ainsi que la couleur du joueur à qui appartenait la planchette en question

	Les planchettes de la pile proviennent une sur deux de la pioche du joueur 1 et une sur deux de celle du joueur 2, avec la première provenant de la pioche du joueur 1 
		ce pourquoi on définie la variable couleur sur la couleur du joueur 1 au début, puis à chaque planchette affichée, on la remplace par la couleur de l'autre joueur
	Pour définir les coordonnées du centre de la croix qui représente le centre de gravité :
		x_croix = largeur de la fenetre divisé par 2 (pour avoir le centre de la fenetre)
					+ le centre de gravité de la planchette
		y_croix = hauteur de la fenetre - 40 pixels - le nombre de planchette déjà affichées + la moitié d'une (pour que la croix soit au milieu) multiplié par l'épaisseur d'une planchette

	On utilise ensuite la fonction pour dessiner la croix (définie ensuite) en lui donnant les coordonnées qu'on vient de calculer, en lui affectant une couleur différente si la pile est en déséquilibre ou non
	'''



def dessine_croix(fenetre, color, x, y) :
	taille = VuePlanchette.pixels(0.3)*Planchette.Epaisseur

	Fenetre.toile(fenetre).create_line(x-taille, y-taille, x+taille, y+taille, fill = color, width = 2)
	Fenetre.toile(fenetre).create_line(x-taille, y+taille, x+taille, y-taille, fill = color, width = 2)

		#la fonction trace successivement deux lignes perpendiculaires pour faire une croix de centre (x,y)
