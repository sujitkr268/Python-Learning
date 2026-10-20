# 1. Import the required libraries
import os
import psycopg
from dotenv import load_dotenv

# 2. Load variables from the .env file
load_dotenv()

# 3. Get the database connection string
DATABASE_URL = os.getenv("DATABASE_URL")

# 4. Connect to PostgreSQL
with psycopg.connect(DATABASE_URL) as connection:

    # 5. Create a cursor to execute SQL queries
    with connection.cursor() as cursor:

        # 6. Create the students table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                skill VARCHAR(100) NOT NULL
            )
        """)

        # 7. Display a success message
        print("Students table created successfully!")
