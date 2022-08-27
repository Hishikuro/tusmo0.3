"""
file :Ce fichier contient un liste de fonction
qui traite les mots 
date :  5/07/2022
Auteur : Hi_shikuro 
"""
def motCommAvecT(lettreMaj , nbLettre , lstDeMot) :
	"""
	Cette fonction cherche les mots d'une liste 
	d'une taille de mot donner et avec la premiere letre donner 
	dans une liste de mot .
	input:
	-lettreMaj est un caractere
	-nbLettre est un entier
	-lstDeMot est une liste de chaine de caractere
	output:
	-retourne une liste de chaine de caractere

	"""
	lstMot =[]
	for mot in lstDeMot:
		if lettreMaj == mot[0] and len(mot) == nbLettre  and " " not in mot :
			lstMot.append(mot)
	return(lstMot)
def shearchLstCaratere(lstLettre,lstMot):
	"""
	Cette fonction cherche les mots contenant
	 au moins une lettre d'une liste de lettre dans une
	  liste de  mot 
	intput :
	- lstLettre : est une liste de caractere
	- lstMot : est une liste de chaine de caractere
	output:
	 retourne une liste  de chaine de caractere 
	"""
	lst =[]
	for c in lstLettre:
		for mot in lstMot:
			if c in mot:
				lst.append(mot)
	return(lst)

def shearchMotifDesMots(motif,lstMot):
	"""
	Cette fonction cherche les mots dans
	une liste qui contient le motif demander
	input :
	- motif est une chaine de caractere 
	- lstMot est une liste de chaine de caractere 
	output :
	-retourne une liste des elements de meme
	type lstMot 
	"""
	lst=[]
	for mot in lstMot :
		if motif in mot :
			lst.append(mot)
	return(lst)

def print_element(lstElt,endL):
	"""
	Cette fonction permette de affiche 
	des element d'une liste séparer par
	un caractere donner

	input:
	- lstElt est une liste d'élement de type mélanger
	- endl est un element de type chaine de caractere ,
	qui sert de separateur 

	output:
	affiche les elements par séparateur
	"""
	for elt in lstElt:
		if elt == lstElt[-1] :
			print(elt, end="\n")
		else:
			print(elt, end=endL)
