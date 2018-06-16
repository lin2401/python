import mysql.connector
import hug


@hug.put('/pok')
connexion = mysql.connector.connect(host = "localhost", user = "root", password = "", database ="pokemon")
cursor = connexion.cursor()

connexion = mysql.connector.connect(host = "localhost", user = "root", password = "", database = " pokemon")
    cursor = connexion.cursor()
    cursor.execute(" SELECT Id, nom FROM pok")
    for row in cursor.fetchall():
        Id = str(row[0])
        nom = str(row[1])
        print (Id, nom)

    connexion.commit()
    connexion.close()



#cursor.execute("""
 #              SELECT * FROM pok
                
  #              """)
#data = cursor.fetchall()
#for link in data :
 #   return
 #   json.dumps(r)
#connexion.close()


#post http;//localhost:8000


@hug.create('/Id', '/nom')
def add ():
connexion = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "pokemon")
cursor = connexion.cursor()
sursor.execute ("""
                INSERT INTO pok VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """)
add()
connexion.commit()
connexion.close()


@hug.update('/nom')

def maj ():

    connexion = mysql.connector.connect(host = "localhost", user = "root", passord = "", database = "pokemon")
    cursor = connexion.cursor()
    cursor.execute (""" 
                    UPDATE pok set Id = '%s', nom = %s' WHERE Id = %s
                    """)
    maj()
    connexion.commit()
    connexion.close()

    #connexion = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "pokemon")
    #cursor = connexion.cursor()
#    cursor.execute ("""
#                DELETE from pok "

  #  nom.set(result [1])
    #type.set(result[2])
    #connexion.close()


@hug.delete('/id')
def supp ():

    connexion = mysql.connector.connect(host = "localhost", user ="root", password = "", database ="pokemon")
    cursor = connexion.cursor()
    cursor.execute ("""
    DELETE FROM pok where Id = '%s'"
    """)

    supp()
    connexion.commit()
    connexion.close()



