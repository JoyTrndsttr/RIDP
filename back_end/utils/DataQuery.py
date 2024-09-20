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
    sql = '''
    SELECT m.FileName, fc.Content AS FileContent
    FROM Metrics m
    JOIN FileContents fc ON m.ContentID = fc.ContentID
    WHERE m.Bridge = %s AND m.Time = %s AND m.Type = %s;
    '''
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            cursor.execute(sql, (bridge, time, type))
            result = cursor.fetchone()
            return result if result else None
    finally:
        connection.close()

def get_parameters_by_bridge_and_model(bridge_type, model_type):
    sql = "SELECT Parameters FROM model WHERE BridgeType = %s AND ModelType = %s;"
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            cursor.execute(sql, (bridge_type, model_type))
            result = cursor.fetchone()
            return result['Parameters'] if result else None
    finally:
        connection.close()

def update_parameters_by_bridge_and_model(bridge_type, model_type, new_parameters):
    sql = "UPDATE model SET Parameters = %s WHERE BridgeType = %s AND ModelType = %s;"
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            cursor.execute(sql, (new_parameters, bridge_type, model_type))
            connection.commit()  # Ensure changes are committed to the database
    finally:
        connection.close()
