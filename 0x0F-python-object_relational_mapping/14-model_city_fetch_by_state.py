#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa:
"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    script = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)

    for i, j in script.all():
        print('{}: ({}) {}'.format(i.name, j.id, j.name))

    session.close()
