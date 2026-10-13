import os
import mysql.connector
from mysql.connector import Error
import functions_framework
from flask import jsonify

# Database configuration
DB_CONFIG = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME')
}

@functions_framework.http
def write_to_mysql(request):
    """
    Cloud Function to write data to MySQL database.
    Expects a POST request with JSON data containing 'name' and 'email' fields.
    """
    # 處理 CORS 預檢請求
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',  # 在生產環境中替換為特定域名
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # 為所有回應添加 CORS 頭信息
    headers = {
        'Access-Control-Allow-Origin': '*',  # 在生產環境中替換為特定域名
        'Content-Type': 'application/json'
    }

    try:
        # 獲取請求數據
        request_json = request.get_json(silent=True)
        
        if not request_json:
            return (jsonify({'error': 'No data provided'}), 400, headers)
            
        name = request_json.get('name')
        email = request_json.get('email')
        
        if not all([name, email]):
            return (jsonify({'error': 'Missing required fields'}), 400, headers)

        # 連接到 MySQL
        connection = mysql.connector.connect(**DB_CONFIG)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # 插入數據
            query = """
                INSERT INTO users (name, email) 
                VALUES (%s, %s)
            """
            values = (name, email)
            
            cursor.execute(query, values)
            connection.commit()
            
            return (jsonify({
                'message': 'Data successfully written',
                'user_id': cursor.lastrowid
            }), 200, headers)

    except Error as e:
        return (jsonify({'error': f'Database error: {str(e)}'}), 500, headers)
        
    except Exception as e:
        return (jsonify({'error': f'Unexpected error: {str(e)}'}), 500, headers)
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
