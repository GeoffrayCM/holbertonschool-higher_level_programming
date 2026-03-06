#!/usr/bin/python3
"""Deletes all State objects with a name containing 'a'"""
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

    # Récupération de tous les états contenant la lettre 'a'
    states_to_delete = session.query(State).filter(State.name.like("%a%")).all()

    # Suppression de ces états
    for state in states_to_delete:
        session.delete(state)

    session.commit()
