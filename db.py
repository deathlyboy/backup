import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
except Exception as ex:
    print("connection refused...")
    print(ex)


def set_drive_id(file_path, id):
    with connection.cursor() as cursor:
        query = "INSERT INTO `drive_id` (`file_path`, `drive_id`) VALUES (%s,%s)"
        cursor.execute(query, (file_path, id))
        connection.commit()


def get_drive_id(file_path):
    with connection.cursor() as cursor:
        query = "SELECT drive_id FROM `drive_id` WHERE file_path=%s"
        cursor.execute(query, (file_path,))
        return cursor.fetchall()[0]['drive_id']

