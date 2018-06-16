from bs4 import BeautifulSoup
import requests

import mysql.connector


connexion = mysql.connector.connect(host="localhost", user="root", password="", database="pokemon")
cursor = connexion.cursor(buffered=True)

cursor.execute("""
CREATE TABLE IF NOT EXISTS pok
        (
            Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            id_pok INT (50),
            nom VARCHAR(50),
            type VARCHAR(50),
            total INT(50),
            hp INT (50),
            attack INT (50),
            defense INT (50),
            sp_attack INT (50),
            sp_defense INT (50),
            speed INT (50)
       );
  """)
connexion.commit()


url = "https://pokemondb.net/pokedex/all"

response = requests.get(url)
html = str(response.content)
soup = BeautifulSoup (html, "html.parser")
tab = soup.find (id="pokedex")

for link in tab.findAll("tr"):
    tt = []
    for l in link.find_all("td"):
        tt.append(l.text)

    if len(tt) > 1 :
        list = (tt[(0)],tt[(1)], tt[(2)], tt[(3)], tt[(4)], tt[(5)], tt[(6)], tt[(7)], tt[(8)], tt[(9)])
        cursor.execute(""" INSERT INTO pok(id_pok, nom, type, total, hp, attack, defense, sp_attack, sp_defense, speed) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", list)
        connexion.commit()

        print(tt)


#connexion.close()
