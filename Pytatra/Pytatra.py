import Jeu
import Dialogue
import Fenetre

while True :
	jeu = Jeu.cree()
	play_again = Jeu.joue(jeu)
	if not play_again :
		break
	Fenetre.tk(Jeu.fenetre(jeu)).destroy()
'''
on crée un jeu et on lance une partie, une fois celle-ci terminée, on demande au joueur s'il veut en refaire une, 
si oui, la boucle va continuer de tourner et une partie va recommencer, 
sinon, la boucle va arreter de tourner et le jeu va se fermer
si on choisi de refaire une partie, on doit détruire la fenetre précédement créée avant de recréer un jeu, sinon le jeu va continuer avec deux fenetres ouvertes
'''
