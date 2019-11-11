import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect

class Db():
    def __init__(self, db_name):
        self.db_name = db_name
        db_conn_string = f"sqlite:///{db_name}.sqlite"
        self.engine = create_engine(db_conn_string)

    def get_session(self):
        return Session(bind=self.engine)
