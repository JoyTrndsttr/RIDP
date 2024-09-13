# DataStorage.py

import os
import re
import json
import pandas as pd
import pymysql
from pymysql.err import IntegrityError

def connect_db():
    return pymysql.connect(host='localhost', user='user', password='123456', db='ridp', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

def store_data(path, bridge_name, time, filename, measurement_type, file_content):
    sql = '''
    INSERT INTO metrics (Bridge, Time, Type, FileName, FileContent)
    VALUES (%s, %s, %s, %s, %s)
    '''
    try:
        connection = connect_db()
        with connection.cursor() as cursor:
            cursor.execute(sql, (bridge_name, time, measurement_type, filename, json.dumps(file_content)))
        connection.commit()
    finally:
        connection.close()

def process_files(base_path):
    """ Process each file in the given directory """
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.csv'):
                full_path = os.path.join(root, file)
                parts = full_path.split('\\')
                # Extract needed parts from the path
                bridge_name = parts[-4]
                date = parts[-3]
                time_id = parts[-2]
                filename = parts[-1]
                time = f"{date} {time_id.replace('_', ':')}"

                # Extract measurement type from the filename
                type_match = re.search(r'\[(.*?)\]', filename)
                if type_match:
                    measurement_type = type_match.group(1)
                
                # Read CSV and convert to JSON
                data = pd.read_csv(full_path)
                data.columns = ['time', 'value']  # Rename columns
                file_content = data.to_dict(orient='records')
                
                # Store data into database
                store_data(full_path, bridge_name, time, filename, measurement_type, file_content)

if __name__ == "__main__":
    base_path = r'C:\\Users\\Administrator\\OneDrive - csu.edu.cn\work\\开源实验室\\横向项目\\土木\\RIDP\\data'
    process_files(base_path)
