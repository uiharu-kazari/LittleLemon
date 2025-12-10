"""
Database setup script for MySQL
Run this before running migrations: python create_db.py
"""
import mysql.connector
from mysql.connector import Error

def create_database():

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS littlelemon_db")
            print("✅ Database 'littlelemon_db' created or already exists")
            
            cursor.close()
    
    except Error as e:
        print(f"❌ Error while connecting to MySQL or creating database: {e}")
        print("\n⚠️  Make sure MySQL is running and credentials are correct:")
        print("   - Host: localhost")
        print("   - User: root")
        print("   - Password: root")
    
    finally:
        if connection.is_connected():
            connection.close()
            print("✅ MySQL connection is closed")


if __name__ == "__main__":
    create_database()
