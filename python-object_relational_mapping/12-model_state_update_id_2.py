#!/usr/bin/python3
"""Change the name of the State with id = 2 to 'New Mexico'"""
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

    # Récupération de l'état avec id=2
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
