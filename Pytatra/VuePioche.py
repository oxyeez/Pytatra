from tkinter import *

import Exemplaires
import Planchette
import Pioche
import Fenetre
import VuePlanchette
import tkinter.font as tkFont

def dessine(fenetre, pioche, gauche):
	largeur_fen = Fenetre.largeur(fenetre)
	hauteur_fen = Fenetre.hauteur(fenetre)
	epaisseur = Planchette.Epaisseur

	for i in range(len(pioche)-1, -1, -1) :
		planchette = Exemplaires.planchette(pioche[i])
		longueur_planch = VuePlanchette.pixels(Planchette.longueur(planchette))
		texte = Exemplaires.versChaine(pioche[i])
		hauteur_texte = VuePlanchette.pixels(2*(len(pioche)-i-1)*epaisseur)
		hauteur_planch = VuePlanchette.pixels((2*(len(pioche)-i-1)-0.5)*epaisseur)

		x0_gauche = (3, 45)
		x0_droit = (largeur_fen-3, largeur_fen-50-longueur_planch)
		y0 = (hauteur_fen-40-hauteur_planch, hauteur_fen-40-hauteur_planch)
		
		if gauche :
			Fenetre.toile(fenetre).create_text(x0_gauche[0], y0[1], text = texte, anchor = 'w')
			VuePlanchette.dessine(fenetre, planchette, x0_gauche[1], y0[0], VuePlanchette.CouleurJoueur1)
		else :
			Fenetre.toile(fenetre).create_text(x0_droit[0], y0[1], text = texte, anchor = 'e')
			VuePlanchette.dessine(fenetre, planchette, x0_droit[1], y0[0], VuePlanchette.CouleurJoueur2)
	
	y0_joueur = hauteur_fen-80-VuePlanchette.pixels(2*(len(pioche)-1)*epaisseur)
	
	if gauche :
		Fenetre.toile(fenetre).create_text(45, y0_joueur, text = 'Joueur 1', anchor = 'w', font = tkFont.Font(size = '20', weight = 'bold'))
	else :
		Fenetre.toile(fenetre).create_text(largeur_fen-45, y0_joueur, text = 'Joueur 2', anchor = 'e', font = tkFont.Font(size = '20', weight = 'bold'))
	'''
	on passe en revue tous les exemplaires de la pioche (en sens inverse pour commencer par la planchette la plus grande)
	pour chaque exemplaire, on va créer : 
			- un x0_gauche contenant : la position en abscisse du coté gauche des textes indiquant le numéro de planchette et la quantité disponible, ainsi que la position en abscisse du coté gauche des planchettes de la pioche de gauche (ici les valeurs sont définies arbitraiement, après quelques tests)
			- un x0_droit contenant : la position en abscisse du coté droit des textes indiquant le numéro de la planchette et la quantité disponible, ainsi que la position en abscisse du coté gauche des planchettes de la pioche de droite
			- un y0 (commun aux deux pioches) contenant : la position en ordonnée du centre du texte, ainsi que la position en ordonnée du haut de la planchette

	une fois les coordonnées calculées (le plus dur est fait), on utilise la fonction qui permet d'afficher du texte ainsi que la fonction qui affiche les planchettes, en leur donnant les coordonnées correspondantes
	avec bien sur des coordonnées et une couleur différentes si la pioche que l'on veut afficher est à gauche ou à droite

	petit ajout : on affiche au dessus de chaque pioche le numéro du joueur à laquelle elle correspond :
		on calcul un y0_joueur qui est 80 pixels au dessus de la planchette du haut de la pioche et à 45 pixels du bord
	'''
