import Exemplaires
import Planchette

def cree():
	pioche = []
	for i in range(3) :
		for j in range(1, 4) :
			planchette = Planchette.cree(10+2*i, i+j)
			pioche.append(Exemplaires.cree(planchette, i+j))
	return pioche
	'''
	crée une pioche complète
	pour cela, j'ai trouvé un moyen de créer tous les types de planchette ainsi que leur nombre dans la pioche en faisant tourner deux boucles l'une dans l'autre
	la première boucle va tourner de 0 à 2 et la deuxième va aller de 1 à 3
	et grâce à d'astucieux calculs on obtient : 
			- toutes les longueurs de planchette possibles : (10+2*j) nous donne 10, 12 et 14
			- toutes les longueurs de marge possibles : (i+j) nous donne 1, 2, 3, 4 et 5 et correspond avec les bonnes longueurs de planchette
			- la quantité d'un type planchette dans la pioche qui est égale à chaque fois à la longueur des marges de la planchette donc encore (i+j)
		
		ex : la planchette n° 363 de longueur 12cm de marge longues de 3cm chacune et disponible en 3 exemplaires 
			 va etre obtenue quand i sera sur la valeur 1 et j sur la valeur 2 
			 ce qui donne : la longueur de la planchette 10+2*1 = 12
							la longueur des marges de la planchette 1+2 = 3
							la quantité disponible dans la pioche 1+2 = 3
	on crée donc une 'planchette' pour chaque type de planchette, et ensuite un 'exemplaire' pour chacun de ces types de planchette, puis on ajoute ces exemplaires à la pioche un par un
	finalement on retourne notre pioche complète
	'''

def nombrePlanchettes(pioche):
	nombre = 0		#on initialise le nombre de planchette sur 0
	for exemplaires in pioche :			
		nombre += Exemplaires.nombre(exemplaires)		#pour chaque exemplaire de planchette dans la pioche on ajoute la quantité de planchette de cet exemplaire au nombre total de planchette
	return nombre 	#retourne le nombre total de planchettes dans le pioche

def versChaine(pioche):
	string = ''		#on initialise une chaine de caractères vide
	for exemplaires in pioche :
		string += Exemplaires.versChaine(exemplaires)+' '		#pour chaque exemplaire de la pioche, on ajoute à la chaine de caractères un nouveau morceau de chaine contenant le nombre d'un type de planchette, 'x', son n° d'exemplaire
	return string	#retourne la chaine contenant tous les types de planchette ainsi que leur quantité dans la pioche

def recherche(pioche, numero):
	for element in pioche :		#passe en revu chaque exemplaire de la pioche
		if Planchette.numero(Exemplaires.planchette(element)) == numero :		#on test donc chaque exemplaire pour savoir si leur numéro correspond à celui recherché
			return pioche.index(element)		#si un numéro d'exemplaire correspond à celui recherché, on retourne la position de cet exemplaire dans la liste ce qui, au passage, mettra fin à la fonction 
	return -1		#si on arrive jusqu'ici c'est que aucun exemplaire n'a le numéro recherché, on retourne donc '-1'
	

def contient(pioche, numero):
	if recherche(pioche, numero) >= 0 : return True		#si la pioche contient au moins 1 exemplaire de la planchette possédant le numéro recherché, on retourne True
	else : return False					#sinon on retourne False

def retire(pioche, numero):
	if contient(pioche, numero) :		#on vérifie si la pioche contient que moins un exemplaire de la planchette que l'on veut retirer
		pioche[recherche(pioche, numero)][1] -= 1		#si il y a en effet au moins une planchette de ce numéro dans la pioche on retranche 1 au nombre de planchettes de cet exemplaire
		if pioche[recherche(pioche, numero)][1] == 0 :			#on vérifie qu'il reste toujours au moins une planchette de ce type
			del(pioche[recherche(pioche, numero)])				#si il n'y a plus du tout de planchette de ce type, on retire totalement la liste représentant l'exemplaire de planchette