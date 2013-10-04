#!  /usr/bin/python3.2
# -*- coding: UTF8 -*-
##----------------------------------------------------
## Projet        :  SVGED
## Version       :  Alpha 0.0
## Auteur        :  chris
## Date Creation :  30/09/2013 
## Objet         :
## MAJ           :
## Bug Report    :
## Todo List     :
##----------------------------------------------------
## $Id :$
##----------------------------------------------------
## (c)  chris 2010
##----------------------------------------------------

import datetime

class VsGed(object):
	"""
		La classe principale
	"""

	def __init__(self, nom):
		self.nom = nom
		## Connexion a la base de données

	def connect(self, user, password=None):
		pass

	def create(self):
		pass

	def update(self):
		pass

	def read(self):
		pass

	def delete(self):
		pass

	def search(self):
		pass

def log(msg="<vide>"):
    """
    Petite routine de log
    """
    d = datetime.datetime.now()
    ts = d.strftime("%j %X %f")
    print("%s : %s" % (ts, msg) )

def t_ged():
    log("Test Class VsGed")
    D = VsGed("TEST")

def test():
    log("Debut du traitement")
    t_ged()
    log("Fin   du traitement")

if __name__ == "__main__":
    test()
