"""
file :Ce fichier  est le fichier principal du programme
qui permette de donner une liste de mot possible du mot a trouver
dans tusmo

date :  5/07/2022
Auteur : Hi_shikuro 
"""
from iss import *

lettreMaj = input("Entrer la premiere lettre du mot :")
while(len(lettreMaj) >1 or not(isLettre(lettreMaj))):
	lettreMaj = input("Entrer la premiere lettre du mot :")

nbLettreTemp  = input("Entrer la taille du mot :")
while not(isNomberStr(nbLettreTemp)):
	nbLettreTemp  = input("Entrer la taille du mot :")
nbLettre = int(nbLettreTemp)


motif = input("Entrer un motif principal si vous le savais , sinon la premiere lettre du mot :")
while not(isMot(motif)):
	motif = input("Entrer un motif principal si vous le savais , sinon la premiere lettre du mot :")


lstCarac = []
lstCarac.append(lettreMaj)

caractere = "stop"
print("Entrer les lettres composant le mot un par  un :")
nbNombre =1
while caractere != "" :
	caractere = input(f"Le {nbNombre} lettres ou rien pour stopper >")
	while(len(caractere) >1 or not(isLettre(caractere)) and caractere != ""):
		caractere = input(f"Le {nbNombre} lettres ou rien pour stopper >")
	nbNombre+=1
	if caractere != "" and caractere != "stop":
		lstCarac.append(caractere)

# lecture du dico 
url = "DEM.jsonl.txt"
mode = "r"

from utilpy import *
import json


with open(url, mode) as json_file:
    json_list = list(json_file)
result = []
for json_str in json_list:
    result .append(json.loads(json_str)) 
resultat = {i:result[i] for i in range(len(result)-1)}

# accès au mot 
lstDeMot = []
for i in range(len(resultat)-1):
	lstDeMot.append(resultat[i]["M"])


	
# filtre des mots par la premiere letre combinée au  nombre de lettre
motFiltrer = motCommAvecT(lettreMaj , nbLettre ,lstDeMot )

#filtre pas rapport au caractere connus dans le mot
motFiltrerAff1 = shearchLstCaratere(lstCarac,motFiltrer)

#filtre par un motif 
motFiltrerAff2 = shearchMotifDesMots(motif,motFiltrerAff1)

#affinage
affinage = {}
for lst in motFiltrerAff2 :
	affinage[lst] = lst
affinag2 =[]
for nb,mot in enumerate(affinage) :
	affinag2.append(mot)
#affichage des mot possible
print("\nListe des mots possible :") 
print_element(affinag2 ,",")