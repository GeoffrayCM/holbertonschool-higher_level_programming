#!/usr/bin/python3
"""List all State objects that contain the letter 'a'"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connexion à la base
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
                           pool_pre_ping=True)

    # Création de session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour récupérer tous les états contenant 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")
