# DataStorage.py

import os
import re
import json
import pandas as pd
import pymysql
from pymysql.err import IntegrityError

def connect_db():
    return pymysql.connect(host='localhost', user='user', password='123456', db='ridp', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

def store_data(bridge_name, time, filename, measurement_type, file_content):
    # SQL to insert into metrics without FileContent initially
    metrics_sql = '''
    INSERT INTO metrics (Bridge, Time, Type, FileName)
    VALUES (%s, %s, %s, %s)
    '''
    # SQL to insert into FileContents
    file_content_sql = '''
    INSERT INTO FileContents (FileID, Content)
    VALUES (%s, %s)
    '''
    # SQL to update metrics with the ContentID
    update_metrics_sql = '''
    UPDATE metrics SET ContentID = %s WHERE ID = %s
    '''

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            # Execute insertion into metrics
            cursor.execute(metrics_sql, (bridge_name, time, measurement_type, filename))
            last_metrics_id = cursor.lastrowid  # Get the last inserted id in metrics

            # Execute insertion into FileContents
            cursor.execute(file_content_sql, (last_metrics_id, json.dumps(file_content)))
            last_content_id = connection.insert_id()  # Get the last inserted id in FileContents

            # Update the metrics entry with the ContentID
            cursor.execute(update_metrics_sql, (last_content_id, last_metrics_id))

        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()
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
                store_data(bridge_name, time, filename, measurement_type, file_content)

if __name__ == "__main__":
    base_path = r'C:\\Users\\Administrator\\OneDrive - csu.edu.cn\work\\开源实验室\\横向项目\\土木\\RIDP\\data'
    process_files(base_path)
