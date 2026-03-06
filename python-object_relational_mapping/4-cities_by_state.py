#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa
with their corresponding state names.
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

    # Requête JOIN pour récupérer cities et états
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Affichage des résultats
    for row in cursor.fetchall():
        print(row)

    # Fermeture
    cursor.close()
    db.close()
