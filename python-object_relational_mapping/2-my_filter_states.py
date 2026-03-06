#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupère les arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()

    # Création de la requête SQL avec format pour l'argument
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Affichage des résultats
    for row in cursor.fetchall():
        print(row)

    # Fermeture
    cursor.close()
    db.close()
