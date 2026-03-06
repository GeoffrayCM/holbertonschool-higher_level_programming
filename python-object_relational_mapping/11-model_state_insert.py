#!/usr/bin/python3
"""Add the State object 'Louisiana' to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Création de l'engine SQLAlchemy
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
                           pool_pre_ping=True)

    # Création d'une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Création du nouvel état
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()  # Nécessaire pour persister l'objet

    # Affichage de l'id généré
    print(new_state.id)
