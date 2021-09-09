
import uuid
import jaydebeapi


def main():
    with jaydebeapi.connect(
            "com.mysql.cj.jdbc.Driver",
            "jdbc:mysql://localhost:3306/stackoverflow",
            {"user": "stackoverflow", "password": "stackoverflow"},
            "./mysql/mysql-connector-java-8.0.26.jar") as conn:
        user_id = uuid.uuid4()
        print(user_id)
        print(user_id.hex)
        print(user_id.bytes)
        with conn.cursor() as curs:
            curs.execute('INSERT INTO `user` (userId,username) VALUES (?, ?)',
                         (uuid.uuid4().bytes, 'some_user'))


if __name__ == '__main__':
    main()

