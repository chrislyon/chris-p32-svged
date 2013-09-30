from pymongo import MongoClient
import random
import datetime

## On se connecte
db_cli = MongoClient('localhost', 27017)

## Creation d'une base de données de TEST
db = db_cli.TEST

## Creation d'une collection 
data = db.data

## Creation d'un certain nombre d'entree
nb = random.randrange(20, 100)

USER = 'chris'

for x in range(1, nb):
	d = { 	'nom': "F%06d" % x,
			'meta': { 'type':'FIC', 'ext':'TXT' },
			'ts':{ 'date_cre': datetime.datetime.now(), 'user_cre':USER },
			'data':'< ici les données >'
		}
	data.insert(d)


## Creation d'un dict a stocker dans data

#d1 = { 'nom':'fichier1', 'meta_type':'FIC', 'FIC_TYPE':'TXT' }

## Creation d'une autre
#d2 = { 'nom':'data1', 'meta_type':'DAT', 'DAT_TYPE':'VIDEO' }

#d1_id = data.insert(d1)
#d2_id = data.insert(d2)

#print( "Id : ", d1_id, d2_id)

print( "Collections names :", db.collection_names() )

for d in data.find():
    print( "data : ", d )

## On vire la collection
#db.data.remove()

db_cli.close()
