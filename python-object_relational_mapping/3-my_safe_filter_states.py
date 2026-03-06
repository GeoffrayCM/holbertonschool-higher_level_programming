#!/usr/bin/python3
"""
Take in an argument and displays all values in the states table
where name matches the argument (safe from SQL injection)
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

    # Requête paramétrée sécurisée
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Affichage des résultats
    for row in cursor.fetchall():
        print(row)

    # Fermeture
    cursor.close()
    db.close()
