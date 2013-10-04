from pymongo import MongoClient, collection

SERVER='localhost'
PORT=27017

class DB(object):
	def __init__(self, name):
		self.name = name
		self.db_cli = MongoClient(SERVER, PORT)
		## Creation Base de donnée
		self.db = self.db_cli[name]
		try:
			self.doc = self.db['DOC']
		except:
			self.doc = self.create_modele()

	def __str__(self):
		return "DB:%s %s" % (self.name, self.db.collection_names())

	def create_modele(self):
		d = { 'nom':'root', 'meta':{
									'type':'DIR'	
									}
			}
		self.db.DOC.insert(d)
		return self.db.DOC

	def purge(self):
		self.db.DOC.remove()

	def close(self):
		self.db_cli.close()


if __name__ == '__main__':
	D = DB('TEST')
	d1 = { 'nom':'fichier1', 'meta_type':'FIC', 'FIC_TYPE':'TXT' }
	d2 = { 'nom':'fichier2', 'meta_type':'FIC', 'FIC_TYPE':'TXT' }
	D.db.DOC.insert(d1)
	D.db.DOC.insert(d2)
	print ("Database : %s " % D)
	for doc in D.db.DOC.find():
		print( "doc : ", doc )
	D.purge()
	D.close()

