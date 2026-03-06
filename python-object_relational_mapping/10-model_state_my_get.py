#!/usr/bin/python3
"""Print the id of the State object with the name passed as argument"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Création de l'engine SQLAlchemy
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
                           pool_pre_ping=True)

    # Création d'une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche du State par nom (sécurisée)
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")
