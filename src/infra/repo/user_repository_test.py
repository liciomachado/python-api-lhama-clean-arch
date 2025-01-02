from faker import Faker
from sqlalchemy import text
from src.infra.config import DbConnectionHandler
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DbConnectionHandler()

def test_insert_user():
    """Should insert user"""

    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_user = user_repository.insert_user(name, password)
    with engine.connect() as connection:
        query = connection.execute(text("DELETE FROM users WHERE id='{}';".format(new_user.id)))

    #assert new_user.id == query_user.id
    assert new_user.name == name
    assert new_user.password == password
    