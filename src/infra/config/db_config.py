from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConnectionHandler:
    """ SqlAlchemy database connection """

    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """ Return connection
        :param - None
        :return - engine connection to database
        """
        engine = create_engine(self.__connection_string)
        return engine
    
    def __enter__(self):
        """ Method to create a session
        :param - None
        :return - session
        """
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Method to close the session
        :param - None
        :return - None
        """
        self.session.close()