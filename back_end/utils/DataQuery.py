import pymysql
from pymysql.err import IntegrityError

def connect_db():
    return pymysql.connect(host='localhost', user='user', password='123456', db='ridp', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

def get_times_by_bridge(bridge_name):
    sql = "SELECT Time FROM Metrics WHERE Bridge = %s;"
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            cursor.execute(sql, (bridge_name,))
            results = cursor.fetchall()
            return [result['Time'] for result in results]
    finally:
        connection.close()

def get_file_name_and_content_by_bridge_time_type(bridge, time, type):
    sql = "SELECT FileName, FileContent FROM Metrics WHERE Bridge = %s AND Time = %s AND Type = %s;"
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            cursor.execute(sql, (bridge, time, type))
            result = cursor.fetchone()
            return result if result else None
    finally:
        connection.close()