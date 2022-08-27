"""
file :Ce fichier teste tout les fonctions
de module utilpy  
date :  5/07/2022
Auteur : Hi_shikuro 
"""
import unittest
from utilpy import * 
class teste(unittest.TestCase):
	def setUp(self):
		self.lstMot = ["val","zoo","arbre","ballon","colle","dur"]
		self.lstLetre = ["a","e"]
		self.motif = "ll"
		self.lettre = "c"
		self.taille = 5
			
	def test_motCommAvecT(self):
		self.assertTrue(motCommAvecT(self.lettre  , self.taille , self.lstMot )==["colle"])
		self.assertFalse(motCommAvecT(self.lettre  , self.taille+1 , self.lstMot )==["colle"])
	
	def test_shearchLstCaratere(self):
		# stLettre,lstMot
		self.assertTrue(shearchLstCaratere(self.lstLetre  , self.lstMot )==['val', 'arbre', 'ballon', 'arbre', 'colle'])
		self.assertFalse(shearchLstCaratere(self.lstLetre  , self.lstMot )==['val', 'arbre', 'ballon',  'colle'])
	def test_shearchMotifDesMots(self):
		#shearchMotifDesMots(motif,lstMot)
		self.assertTrue(shearchMotifDesMots(self.motif,self.lstMot) ==["ballon",'colle'] )
		self.assertFalse(shearchMotifDesMots(self.motif,self.lstMot) == ["ballon"] )
	
if __name__ == "__main__" : 
	unittest.main()