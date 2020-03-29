#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    script = session.query(State).filter(State.name.like('%a%'))

    for i in script:
        session.delete(i)

    session.commit()
    session.close()
