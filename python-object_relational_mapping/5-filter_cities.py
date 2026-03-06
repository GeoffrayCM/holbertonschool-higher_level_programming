#!/usr/bin/python3
"""
List all cities of a given state (safe from SQL injection)
from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()

    # Requête JOIN sécurisée
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Récupère les résultats et affiche séparés par des virgules
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    # Fermeture
    cursor.close()
    db.close()
