from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

# Etape 2

Titre = 'Pytatra'

def cree(largeur, hauteur):
	tk = Tk()			#création d'une variable tk contenant une fenetre Tkinter
	tk.title(Titre)		#attribution du titre à l'objet Tkinter
	toile = Canvas(tk, width=largeur, height=hauteur, background="white")		#création d'une variable toile contenant un canvas, attribué à la fenetre précédement créée, de hauteur :'hauteur', de largeur:'largeur', et de fond blanc
	toile.pack()		#mise en place de la toile dans la fenetre Tkinter
	return (toile, largeur, hauteur, tk)  #retourne un tuple contenant : la toile, sa largeur, sa hauteur, et la fenetre

def cree_replay(largeur, hauteur):
	tk_replay = Tk()			#création d'une variable tk contenant une fenetre Tkinter
	tk_replay.title('Replay')	#attribution du titre à l'objet Tkinter
	toile_replay = Canvas(tk_replay, width=largeur, height=hauteur, background="white")		#création d'une variable toile contenant un canvas, attribué à la fenetre précédement créée, de hauteur :'hauteur', de largeur:'largeur', et de fond blanc
	toile_replay.pack()		#mise en place de la toile dans la fenetre Tkinter
	return (toile_replay, largeur, hauteur, tk_replay)  #retourne un tuple contenant : la toile, sa largeur, sa hauteur, et la fenetre

def toile(fenetre):
	return fenetre[0]	#retourne le premier élément du tuple créé avec la fonction cree(.,.), correspondant à la toile

def largeur(fenetre):
	return fenetre[1]	#retourne le deuxième élément du tuple créé avec la fonction cree(.,.), correspondant à la largeur de la toile

def hauteur(fenetre):
	return fenetre[2]	#retourne le troisième élément du tuple créé avec la fonction cree(.,.), correspondant à la hauteur de la toile

def tk(fenetre):
	return fenetre[3]	#retourne le quatrième élément du tuple créé avec la fonction cree(.,.), correspondant à la fenetre Tkinter

def affiche(fenetre):
	tk(fenetre).mainloop()		#lance la boucle principale de la fenetre


# Etape 5

TagGraphiques = 'graphique'

def effaceGraphiques(fenetre):
	toile(fenetre).addtag_all(TagGraphiques)
	toile(fenetre).delete(TagGraphiques)

def quandOuverte(fenetre, fonction, argument):
	def fonctionInterne(e):
		# pour éviter les invocations ultérieures
		tk(fenetre).unbind('<Map>') 
		# invocation de la fonction principale
		fonction(argument)
	# liaison de l'évènement d'ouverture
	tk(fenetre).bind('<Map>', fonctionInterne)

def quitte(fenetre):
	tk(fenetre).quit()

