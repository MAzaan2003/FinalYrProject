"""
database.py

Creates and manages the Cyber Risk Simulator database.
"""

import sqlite3

DATABASE_NAME = "src/database/cyberrisk.db"


class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """Create all required database tables."""

        # Users
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            organisation_id INTEGER,
            FOREIGN KEY (organisation_id)
                REFERENCES organisations(organisation_id)
        )
        """)

        # Organisations
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS organisations (
            organisation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            organisation_name TEXT NOT NULL,
            industry TEXT,
            employee_count INTEGER
        )
        """)

        # Questions
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            question_id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            category TEXT,
            risk_weight INTEGER
        )
        """)

        # Assessments
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            organisation_id INTEGER,
            assessment_date TEXT,
            total_score INTEGER,
            risk_level TEXT,
            FOREIGN KEY (organisation_id)
                REFERENCES organisations(organisation_id)
        )
        """)

        # Responses
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            response_id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER,
            question_id INTEGER,
            answer TEXT,
            FOREIGN KEY (assessment_id)
                REFERENCES assessments(assessment_id),
            FOREIGN KEY (question_id)
                REFERENCES questions(question_id)
        )
        """)

        self.connection.commit()

    def execute(self, query, values=()):
        """Execute INSERT, UPDATE or DELETE statements."""
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor

    def fetch_one(self, query, values=()):
        """Return one record."""
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def fetch_all(self, query, values=()):
        """Return all matching records."""
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    db = DatabaseManager()
    db.create_tables()
    print("Database created successfully.")
    db.close()