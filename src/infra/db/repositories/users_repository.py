from src.infra.db.settings.connection import DbConnectionHander
from src.infra.db.entities.users import Users as UsersEventity

class UsersRepository():

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DbConnectionHander() as database:
            try:
                new_resistry = UsersEventity(
                    first_name=first_name,
                    last_name=last_name,
                    age=age
                )
                database.session.add(new_resistry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
