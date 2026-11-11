"""
database.py

Handles database connection and table creation.
"""

import sqlite3


DATABASE_NAME = "cyber_risk.db"



def get_connection():

    return sqlite3.connect(
        DATABASE_NAME
    )



def create_database():

    connection = get_connection()

    cursor = connection.cursor()


    # ==========================
    # ORGANISATIONS TABLE
    # ==========================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS organisations
        (
            organisation_id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            industry TEXT NOT NULL,

            employees INTEGER NOT NULL
        )
        """
    )



    # ==========================
    # USERS TABLE
    # ==========================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users
        (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            organisation_id INTEGER,

            FOREIGN KEY
            (organisation_id)
            REFERENCES organisations
            (organisation_id)
        )
        """
    )



    # ==========================
    # ASSESSMENTS TABLE
    # ==========================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS assessments
        (
            assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,

            organisation_id INTEGER,

            date TEXT,

            score INTEGER,

            level TEXT,

            FOREIGN KEY
            (organisation_id)
            REFERENCES organisations
            (organisation_id)
        )
        """
    )



    # ==========================
    # QUESTION RESPONSES TABLE
    # ==========================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS responses
        (
            response_id INTEGER PRIMARY KEY AUTOINCREMENT,

            assessment_id INTEGER,

            question TEXT,

            answer TEXT,

            FOREIGN KEY
            (assessment_id)
            REFERENCES assessments
            (assessment_id)
        )
        """
    )



    connection.commit()

    connection.close()
