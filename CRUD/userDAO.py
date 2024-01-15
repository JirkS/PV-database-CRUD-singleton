from CRUD.database import Database
from CRUD.user import User


class UserDAO:
    def __int__(self):
        self._connection = Database().get_connection()

    def create_user(self, user: User):
        if not isinstance(user, User):
            raise TypeError("User is no instance of class User!")
        command = "insert into uzivatel(username, favorite_number, favorite_color) values(%s, %s, %s)"
        with self._connection.cursor() as cursor:
            cursor.execute(command, user)
        self._connection.commit()

    def read_user_by_username(self, username: str):
        if not isinstance(username, str):
            raise TypeError("User is no instance of class String!")
        command = "select * from uzivatel where username = %s"
        with self._connection.cursor() as cursor:
            cursor.execute(command, username)
            result = cursor.fetchone()

        users = []
        for row in result:
            user = User(row[0], row[1], row[2], row[3])
            users.append(user)
        return users

    def read_all_users(self, username: str):
        if not isinstance(username, str):
            raise TypeError("User is no instance of class String!")
        command = "select * from uzivatel"
        with self._connection.cursor() as cursor:
            cursor.execute(command, username)
            result = cursor.fetchone()

        users = []
        for row in result:
            user = User(row[0], row[1], row[2], row[3])
            users.append(user)
        return users

    def update_user_favourite_color(self, color: str):
        if not isinstance(color, str):
            raise TypeError("User is no instance of class String!")
        command = f"update user set favorite_color = %s where favorite_color = %color"
        with self._connection.cursor() as cursor:
            cursor.execute(command, color)
        self._connection.commit()

    def update_user_favourite_number(self, number: str):
        if not isinstance(user, User):
            raise TypeError("User is no instance of class User!")
        command = "insert into uzivatel(username, favorite_number, favorite_color) values(%s, %s, %s)"
        with self._connection.cursor() as cursor:
            cursor.execute(command, user)
        self._connection.commit()

    def delete_user(self, user):
        if not isinstance(user, User):
            raise TypeError("User is no instance of class User!")
        command = "insert into uzivatel(username, favorite_number, favorite_color) values(%s, %s, %s)"
        with self._connection.cursor() as cursor:
            cursor.execute(command, user)
        self._connection.commit()

