import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database Configuration
DB_HOST = os.getenv("DB_HOST", "127.0.0.1").strip()  # Ensure correct format
DB_USER = os.getenv("DB_USER", "root").strip()
DB_PASSWORD = os.getenv("DB_PASSWORD", "01788541577").strip()
DB_NAME = os.getenv("DB_NAME", "youtube_trends").strip()

# Connect to Database
def connect_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=3306  # Explicitly specify the MySQL port
        )
        print("✅ Connected to MySQL")
        return conn
    except mysql.connector.Error as e:
        print("❌ Error connecting to MySQL:", e)
        return None

# Test connection
if __name__ == "__main__":
    connect_db()
