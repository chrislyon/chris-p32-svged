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

class Doc(object):
    """
    Les documents, apres c'est une Gestion Electonique des Documents
    - peut etre : un fichier / un conteneur / des données
    fichier : type connu (txt odf ... html) on peut facilement extraire du texte
    et l'utiliser pour generer un index
    conteneur : pour l'instant un repertoire 
    données : fichier pas prévu pour être indexe sauf meta données

    MetaType : Fichier/conteneur/donnees
    Nom : Nom du document
    Id : Identifiant unique
    Propriétaire/Groupe
    Date de Creation
    Date de modification
    Date de suppression
    Date de lecture

    """
    LAST_ID = None

    FIC = 1
    DIR = 2
    DAT = 3

    def __init__(self, nom, meta_type):
        ## Pedigree
        self.Nom = nom
        self.MetaType = meta_type
        self.Id = self.new_id()
        ## Proprio / groupe
        self.Uid = None
        self.Gid = None
        ## Date 
        self.DateCre = None
        self.DateMod = None
        self.DateLec = None

    def new_id(self):
        if Doc.LAST_ID is None:
            Doc.LAST_ID = 1000
        Doc.LAST_ID += 1
        return Doc.LAST_ID

def log(msg="<vide>"):
    """
    Petite routine de log
    """
    d = datetime.datetime.now()
    ts = d.strftime("%j %X %f")
    print("%s : %s" % (ts, msg) )

def t_doc():
    log("Test Class Doc")
    D = Doc("fichier", Doc.FIC )

def test():
    log("Debut du traitement")
    t_doc()
    log("Fin   du traitement")

if __name__ == "__main__":
    test()
