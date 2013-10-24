## ----------------------------------------
## Test de stockage de fichier dans mongodb
## ----------------------------------------

from pymongo import MongoClient, collection
import gridfs

import datetime

SERVER='localhost'
PORT=27017

def log(msg="<vide>"):
	"""
	Petite routine de log
	"""
	d = datetime.datetime.now()
	ts = d.strftime("%j %X %f")
	print("%s : %s" % (ts, msg) )

class DOC(object):
	"""
	La classe de base : Document
	"""
	def __init__(self, DB, name):
		self.db = DB
		self.name = name
		self.title = ""
		self.description = ""
		self.version = ""
		self.mime = 'application/data'

	def __str__(self):
		return "DOC:%s/%s/%s" % (self.name, self.title, self.version)

	def store(self, filename=None, data=""):
		if filename:
			## verifier existence toussa ...
			oid = None
			with open(filename) as d:
				oid = self.db.fs.put(d, content_type = self.mime, filename=filename)
			return oid

		else:
			d = self.db.fs.put(data)
			oid = self.db.fs.put(self.db.fs.get(d), content_type = self.mime, filename=filename)
			return oid


class DB(object):
	"""
	La classe DB Database 
	"""
	def __init__(self, name):
		self.name = name
		self.db_cli = MongoClient(SERVER, PORT)
		## Creation Base de donnée
		self.db = self.db_cli[name]
		self.fs = gridfs.GridFS(self.db)

	def __str__(self):
		return "DB:%s %s" % (self.name, self.db.collection_names())

	def create_Doc(self, name="Nouveau Document"):
		"""
		creation d'un document
		doit retourner un document
		"""
		return DOC(self, name)

	def purge(self):
		self.db.DOC.remove()

	def close(self):
		self.db_cli.close()


if __name__ == '__main__':
	log("Creation de la base de donnees")
	D = DB('TEST')
	print ("Database : %s " % D)
	log("Creation d'un doc")
	d = D.create_Doc()
	d.title = "Le titre du document 1"
	d.description = "La description du document Numero un"
	d.version = "0.0"
	print ("Document : %s " % d)
	log("Stockage du document")
	oid = d.store(data="HELLO WORLD WITH PYMONGO")
	print(" Le document : \n", D.fs.get(oid).read() )
