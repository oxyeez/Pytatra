import Pioche

def cree(numero):
	return (numero, Pioche.cree())	#crée un tuple contenant en première position le numéro du joueur, et en deuxième position la pioche étant en sa possession

def numero(joueur):
	return joueur[0]		#retourne la première valeur du tuple, correspondant au numéro du joueur

def nom(joueur):
	return 'Joueur '+str(numero(joueur))	#retourne une chaine de caractère contenant : 'joueur ' suivi du numéro du joueur

def pioche(joueur):
	return joueur[1]		#retourne la deuxième valeur du tuple, correspondant à la pioche en possission du joueur
