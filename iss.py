"""
file :Ce fichier contient un liste de fonction
qui verifier le type de donner 
date :  5/07/2022
Auteur : Hi_shikuro 
"""

def isLettre(l):
	"""
	Cette fonction dit si un element donner
	 est une lettre de l'alphabet francais

	 input:
	 - l est un caratere 
	 output:
	 -retourne vrai ou faux
	"""
	if (l >="a" and l <= "z") or (l >="A" and l <= "Z"):
		return(True)
	return(False)

def isMot(mot):
	"""
	Cette fonction dit si un element donner
	est un mot c'est a dire une sucection de lettre
	input:
	-mot est une chaine de caractere
	output:
	retourne vrai ou faux

	"""
	for l in mot:
		if not(isLettre(l)):
			return(False)
	return(True)


def isEntier(nombre):
	"""
	Cette fonction dit si un element
	 donner est un nombre sans virgule

	input : 
	-nombre est un enteir
	output:
	- Retourne vrais ou faux
	"""
	if type(nombre) == int :
		return(True)
	return(False)

def isNomberStr(nbStr):
	"""
	Cette fonction dit si une chaine 
	est un nombre sous forme de chaine
	 de caractere
	 input : 
	 -nbStr est une chaine de caractere
	 output:
	 -retourne vrai ou faux

	"""
	for elt in nbStr:
		if not(elt >= "0" and elt <= "9"):
			return(False)
	return(True)

def isListe(lst):
	"""
		Cette fonction dit si un element
	 donner est une liste

	input : 
	-lst est une liste d'élément 
	output:
	- Retourne vrais ou faux
	"""
	if type(lst) == list :
		return(True)
	return(False)


