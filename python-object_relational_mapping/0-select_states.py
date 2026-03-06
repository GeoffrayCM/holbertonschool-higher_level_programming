#!/usr/bin/python3
"""
0-select_states.py
Lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <username> <password> <database>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=database)
    cursor = db.cursor()

    # Exécution de la requête
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Affichage des résultats
    for row in cursor.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
