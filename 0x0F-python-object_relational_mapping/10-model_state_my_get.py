#!/usr/bin/python3
"""
 prints the State object with the name passed as argument
 from the database hbtn_0e_6_usa
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
    script = session.query(State).filter(State.name == sys.argv[4]).first()

    if script:
        print(script.id)
    else:
        print('Not found')
