"""
file :Ce fichier teste tout les fonctions
de module iss 
date :  5/07/2022
Auteur : Hi_shikuro 
"""

import unittest
from iss import * 
class teste(unittest.TestCase):
	def setUp(self):
		self.l1 = "a"
		self.l2 = "1"
		self.l3 = "mot"
		self.l4 = "m0t"
		self.l5 = 1

		self.l6 = [1,2,3]
		self.l7 = ["mot"]
		self.l8 = ["m","o","y"]
			
	def test_lettre(self):
		self.assertTrue(isLettre(self.l1))
		self.assertFalse(isLettre(self.l2))
		self.assertFalse(isLettre(self.l1) == isLettre(self.l2))
	def test_mot(self):
		self.assertTrue(isMot(self.l3))
		self.assertFalse(isMot(self.l4))
		self.assertFalse(isMot(self.l3) == isMot(self.l4))
	def test_entier(self):
		self.assertFalse(isEntier(self.l2))
		self.assertTrue(isEntier(self.l5))
		self.assertFalse(isEntier(self.l2) == isEntier(self.l5))
	def test_liste(self):
		self.assertTrue(isListe(self.l6))
		self.assertTrue(isListe(self.l7))
		self.assertTrue(isListe(self.l8))
		self.assertFalse(isListe(self.l2))
		self.assertFalse(isListe(self.l5))
	def test_nombreStr(self):
		self.assertTrue(isNomberStr(self.l2))
		self.assertFalse(isNomberStr(self.l3))
		self.assertFalse(isNomberStr(self.l4))
		self.assertFalse(isNomberStr(self.l5))

if __name__ == "__main__" : 
	unittest.main()