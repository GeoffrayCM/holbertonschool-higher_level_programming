#!/usr/bin/python3
"""
List all states starting with 'N' from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupère les arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()

    # Exécution de la requête SQL
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Affichage des résultats
    for row in cursor.fetchall():
        print(row)

    # Fermeture
    cursor.close()
    db.close()
