import Dialogue
import Empilement
import Exemplaires
import Fenetre
import Joueur
import Pile
import Pioche
import Planchette
import VuePioche
import VuePile
import os
import pickle


# Etape 5.1

def cree():
	return [Fenetre.cree(1000, 600), Pile.cree(), [Joueur.cree(1), Joueur.cree(2)], {'indiceJoueur' : 0}]
	#retourne une liste composée d'une fenetre tkinter, d'une pile, d'une liste contenant deux joueurs, ainsi que de l'indice du joueur qui est en train de jouer

def gameSaved(jeu, pile, joueurs, indice):
	(jeu[1], jeu[2], jeu[3]) = (pile, joueurs, indice)
	return jeu
	#fonction que j'ai rajouté afin de modifier la liste contenant les informations du jeu en fonction des informations qui sont sauvegardées
	#pour modifier jeu, on rempalace dans la liste jeu : la pile, les deux joueurs et l'indice du joueur en train de jouer, par ce qui est contenu dans le fichier de sauvegarde

def fenetre(jeu):	#retourne la première valeur de la liste créé avec la fonction cree(.,.), correspondant à la fenetre tkinter
	return jeu[0]

def pile(jeu):		#retourne la deuxième valeur de la liste créé avec la fonction cree(.,.), correspondant à la pile
	return jeu[1]

def joueurs(jeu):	#retourne la troisième valeur de la liste créé avec la fonction cree(.,.), correspondant à une liste contenant les deux joueurs
	return jeu[2]

def indiceJoueur(jeu):		#retourne la quatrième valeur de la liste créé avec la fonction cree(.,.), correspondant à un dico contenant l'indice du joueur qui est en train de jouer
	return jeu[3]['indiceJoueur']

def joueurCourant(jeu):		#retourne les informations du joueur qui est en trin de jouer
	return joueurs(jeu)[indiceJoueur(jeu)]

def passeJoueurSuivant(jeu):	#change l'indice du joueur qui est en train de jouer
	if indiceJoueur(jeu) == 0 :	jeu[3]['indiceJoueur'] = 1		#si l'indice du joueur est 0 on le passe à 1
	else :	jeu[3]['indiceJoueur'] = 0			#sinon, c'est que l'indice est 1, on le remplace donc par 0
		

# Etape 5.2

def joue(jeu):
	#déclaration de variables globales et initialisations de celles-ci, GameOn est True tant que l'on ne veut pas arreter le jeu, et Desequilibre est False tant que la pile est en équilibre
	global GameOn
	global Desequilibre
	GameOn = True
	Desequilibre = False
	save_file_path = './GameSave.txt'
	
	majVues(jeu) #premier affichage graphique du jeu, cela n'affiche que les pioches (pleines) au départ, car la pile est vide
	
	if os.path.getsize(save_file_path) != 0 :
		load_save = Dialogue.choix('Il existe une partie sauvegardée.\nVoulez-vous la continuer ?')
		if load_save :
			with open(save_file_path, 'rb') as save_file:
				save = pickle.load(save_file)
				jeu = gameSaved(jeu, save[0], save[1], save[2])
				majVues(jeu)
	'''
	import de sauvegarde :
	- vérifie si le fichier de sauvegarde contient quelque chose (si il est vide sa taille est de 0 octet)
	- si une sauvegarde existe, on demande alors au joueur si il veut charger la sauvegarde
	- si le joueur veut charger la sauvegarde, on ouvre le fichier contenant le sauvegarde, on met dans la variable save la liste contenu dans le fichier
		cette liste est de la forme : [pile, [joueur1, joueur2], indice]
	- on peut alors appeler la fonction gameSaved en lui donnant les arguments nécessaires : save[0] correspond à la pile, save[1] correspond aux joueurs, et save[2] correspond au dico contenant l'indice du joueur en train de jouer
	- on fini en mettant l'affichage à jour
	'''
	while Pioche.nombrePlanchettes(Joueur.pioche(joueurCourant(jeu))) != 0 and not Desequilibre and GameOn :
		activite(jeu)
		majVues(jeu)
	'''
	boucle qui va tourner tant que les joueurs auront encore une pioche, que la pile n'est pas en déséquilibre et que les joueurs veulent toujours jouer
	la boucle va donc appeler à chaque fois la fonction activite() pour effectuer toutes les actions du tour, puis la fonction majVues() pour mettre à jour l'affichage à la fin de chaque tour
	'''
	if Desequilibre :
		passeJoueurSuivant(jeu)
		Dialogue.afficheMessage("La pile est tombée.\nC'est gagné pour le " + str(Joueur.nom(joueurCourant(jeu))) + ' !!')

	elif Pioche.nombrePlanchettes(Joueur.pioche(joueurCourant(jeu))) == 0 :
		Dialogue.afficheMessage('Les pioches sont vides.\nIl y a égalité.')

	elif not GameOn :
		if not Pile.estVide(pile(jeu)) :
			if Dialogue.choix('Vous avez mis fin au jeu avant sa fin.\nVoulez-vous sauvegarder la partie ?') :
				with open(save_file_path, 'wb') as save_file:
					pickle.dump([pile(jeu), joueurs(jeu), jeu[3]], save_file)
	'''
	lorsque le jeu ne peut plus continuer, en fonction de la raison qui met fin au jeu, on affiche un message différent et des actions peuvent être effectuées :
	- si la pile est en déséquilibre, une fenetre de dialogue affiche la raison de la fin de la partie ainsi que le joueur qui a gagné
	- si la pioche d'un des joueurs et vide, une fenetre de dialogue affiche la raison de la fin de la partie ainsi que l'égalité entre les joueurs
	- si un des joueurs a décidé volontairement de mettre fin à la partie, comme celle-ci n'est pas fini, on propose de sauvegarder la partie pour pouvoir la reprendre plus tard :
		- si le joueur décide donc de sauvegarder la partie, on ouvre le fichier de sauvegarde et on y inscrit une liste sous la forme : [pile, joueurs, indice]
	'''
	Fenetre.quitte(fenetre(jeu))
	return Dialogue.choix('Voulez-vous refaire une partie ?')	#return True si le joueur veut rejouer, ce True a un effet dans le fichie Pytatra.py

def majVues(jeu):		#permet la mise à jour de l'affichage, pour cela on efface tout ce qui est dans la fenetre, puis on affiche la pile et les deux pioches
	Fenetre.effaceGraphiques(fenetre(jeu))
	VuePile.dessine(fenetre(jeu), pile(jeu))
	VuePioche.dessine(fenetre(jeu), Joueur.pioche(joueurs(jeu)[0]), True)
	VuePioche.dessine(fenetre(jeu), Joueur.pioche(joueurs(jeu)[1]), False)
	
	

# Etape 5.3

def activite(jeu):		#effectue toutes les actions qui doivent etre effectuées durant un tour
	global GameOn
	global Desequilibre
	
	planchetteAPoser = selectionnePlanchette(jeu)
	if planchetteAPoser == None :
		GameOn = False
		return
	'''
	demande un numéro de panchette à empiler au joueur qui est en train de jouer
	si le joueur n'a pas entré de numéro (None), c'est qu'il veut mettre fin à la partie
	on affecte alors False à la variable GameOn
	le return permet de mettre fin à la fonction activite()
	'''
	passeJoueurSuivant(jeu)					#passe au joueur suivant pour qu'il choisisse un décalage
	decalage = choisisDecalage(jeu, planchetteAPoser)
	
	if decalage == None :
		GameOn = False
		passeJoueurSuivant(jeu)
		return
	Pile.empileEtCalcule(pile(jeu), planchetteAPoser, decalage)
	'''
	on demande au joueur de choisir un décalage
		si le joueur ne choisi pas, c'est qu'il veut mettre fin à la partie, on affecte alors False à la variable GameOn, et on bloque la fonction activite() grâce au return
			et on revient au joueur précédent afin que, dans le cas d'une sauvegarde, le même joueur ne joue pas deux tours de suite
		si le joueur choisi un décalage, on appelle la fonction empileEtCalcule() qui va ajouter à la pile la planchette choisi, avec le décalage choisi et va calculer et mettre à jour toutes les informations concernant le pile
	'''
	passeJoueurSuivant(jeu)
	Pioche.retire(Joueur.pioche(joueurCourant(jeu)), Planchette.numero(planchetteAPoser))
	passeJoueurSuivant(jeu)
	'''
	afin que, lorsque l'on met fin à la partie au moment de choisir un décalage et que l'on sauvegarde, il n'y ait pas une planchette qui soit retirée de la pioche mais pas présente dans la pile, 
	on ne retire la planchette de la pioche qu'une fois le tour terminé
	'''
	for empilement in pile(jeu) :
		if Empilement.desequilibre(empilement) :
			Desequilibre = True
			break
	'''
	on vérifie si tout les empilement de la pile sont en équilibre, 
	on passe en revue chaque empilement et si un ou plus est en déséquilibre, on affecte True à la variable Desequilibre
	'''

def selectionnePlanchette(jeu):
	numero = 0		#initialisation de la variable qui contiendra le numéro de la planchette choisi sur 0
	while not Pioche.contient(Joueur.pioche(joueurCourant(jeu)), numero) :
		numero = Dialogue.saisisEntier(Joueur.nom(joueurCourant(jeu)) + ', entrez un numéro de planchette.')
		if numero == None : return None
		elif not Pioche.contient(Joueur.pioche(joueurCourant(jeu)), numero) and numero != None :
				Dialogue.afficheMessage("Merci d'entrer un numéro de planchette valide et contenu dans votre pioche.")

	return Exemplaires.planchette(Joueur.pioche(joueurCourant(jeu))[Pioche.recherche(Joueur.pioche(joueurCourant(jeu)), numero)])
	'''
	tant que la valeur entrée n'est pas un numéro de planchette qui est contenu dans la pioche du joueur qui est en train de jouer, la boucle continue
	sauf si la valeur None ressort (c'est dans le cas où le joueur choisi cancel au lieu de choisir une valeur), dans quel cas on met fin à la fonction en retournant None
	si la valeur n'est pas None, mais n'est pas une planchette contenue dans la pioche, on affiche un message d'erreur
	une fois sorti de la boucle on retourne l'exemplaire contenant la planchette choisi
	'''

def choisisDecalage(jeu, planchetteAPoser):
	decalage = 0	#initialisation de la variable qui contiendra la valeur de décalage choisi sur 0
	if Pile.estVide(pile(jeu)) :
		pass
	else :
		marge_dessous = Planchette.marge(Empilement.planchette(Pile.sommet(pile(jeu))))
		longueur_dessous = Planchette.longueur(Empilement.planchette(Pile.sommet(pile(jeu))))
		centre_dessous = Empilement.centreGeometrique(Pile.sommet(pile(jeu)))
		longueur_dessus = Planchette.longueur(planchetteAPoser)
		
		while ((longueur_dessous/2 - marge_dessous) - longueur_dessus/2) < decalage < ((marge_dessous - longueur_dessous/2) + longueur_dessus/2) or abs(decalage) > ((longueur_dessous + longueur_dessus)/2)  :
			decalage = Dialogue.saisisFlottant(Joueur.nom(joueurCourant(jeu)) + ', choisissez un décallage')
			if decalage == None : break
			if ((longueur_dessous/2 - marge_dessous) - longueur_dessus/2) < decalage < ((marge_dessous - longueur_dessous/2) + longueur_dessus/2) :
				Dialogue.afficheMessage("Le décalage choisi est trop petit.\nLa planchette ne peut reposer que sur une marge.")
			elif abs(decalage) >= ((longueur_dessous + longueur_dessus)/2) :
				Dialogue.afficheMessage("Le décalage choisi est trop grand.\nLa planchette doit reposer sur la planchette précédente.")
	return decalage
	'''
	si la pile est vide, on ne fait rien, ce qui va laisser le décalage sur 0
	si la pile n'est pas vide, on va demander une valeur de décalage au joueur, jusqu'à ce que le décalage soit bon 
		(de façon à ce que le bord de la planchette à poser ne soit pas sur la marge de la planchette d'en dessous)
	pour vérifier cela, il faut que le décalage vérifie une certaine inéquation qui est détaillée dans le fichier 'inéquation_décalage.jpg' 
	mais il doit aussi etre inférieur à la moitié de la somme de la longueur de la  planchette du sommet de la pile avec la longueur de la planchette à empiler (sinon la planchette n'est pas posée sur la pile)
	
	à l'intérieur de la boucle: si on retourne un None, on met fin à la boucle avec break
		mais si le décalage est trop faible, on affiche un message, de même si le decallage est trop important

	lorsque le décalage vérifie les conditions ou que la boucle a été arrêté, on retourne cette valeur de décalage (qu'elle soit None ou un flottant)
	'''
