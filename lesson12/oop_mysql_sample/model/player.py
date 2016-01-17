from db import connection, ModelIntegrityError


class Player(object):
    def __init__(self, _id=None, name=None, email=None, password=None,
                 created=None, updated=None):
        self._id = _id
        self.name = name
        self.email = email
        self.password = password
        self.created = created
        self.updated = updated

    def load_from_db(self, email):
        """
        Method for loading player instance from DB row

        :param email: Player email for loading all info from db
        :return: None
        """
        cursor = connection.cursor()
        sql_cmd = """SELECT id, name, email, password, created, updated FROM
                     player WHERE email=%(email)s"""
        sql_args = {
            "email": email
        }
        cursor.execute(sql_cmd, sql_args)
        db_row = cursor.fetchone()
        self._id = db_row[0]
        self.name = db_row[1]
        self.email = db_row[2]
        self.password = db_row[3]
        self.created = db_row[4]
        self.updated = db_row[5]

    def save_to_db(self):
        """
        Save all player data to MySQL database.
        If a record with player is not exists, it is inserted.
        If method knows _id of player, it will try to update existing
        db record.

        :return: None
        """
        insert_query = """INSERT INTO player (name, email, password, created, updated) VALUES
                (%(name)s, %(email)s, %(password)s, now(), now())"""
        update_query = """UPDATE player SET name=%(name)s, email=%(email)s, password=%(password)s,
                updated=now() WHERE id=%(_id)s"""

        sql_data = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }

        cursor = connection.cursor()
        if self._id is None:
            try:
                cursor.execute(insert_query, sql_data)
                self._id = cursor.lastrowid
            except ModelIntegrityError:
                print("DEBUG: an integrity error occured when player inserting, it's OK")
                pass
        else:
            sql_data["_id"] = self._id
            cursor.execute(update_query, sql_data)


    def delete_from_db(self):
        """
        Method for deleting player from DB. Needs correct _id field.
        Perhaps player should be loaded before using this method.

        :return: None
        """
        cursor = connection.cursor()
        delete_query = "DELETE FROM player WHERE id=%(_id)s"
        sql_data = {
            "_id": self._id
        }
        cursor.execute(delete_query, sql_data)


    def __str__(self):
        return "Player(_id={}, name={}, email={})".format(self._id, self.name, self.email)


