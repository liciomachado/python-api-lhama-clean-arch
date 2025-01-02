from src.infra.config import DbConnectionHandler
from src.infra.entities.users import Users

class FakerRepository:
    """ A simple repository"""

    @classmethod
    def insert_user(cls) -> None:
        """insert data in user table"""
        with DbConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Mauricio", password="Rosa")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()