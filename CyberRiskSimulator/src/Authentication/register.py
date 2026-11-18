"""
login.py

Handles user login for the Cyber Risk Simulator.
"""

import hashlib
from getpass import getpass

from Database.database import get_connection


MAX_LOGIN_ATTEMPTS = 3


def hash_password(password):
    """
    Hash password using SHA-256.
    """

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def login():

    print("\n" + "=" * 60)
    print("                    USER LOGIN")
    print("=" * 60)

    connection = get_connection()
    cursor = connection.cursor()

    attempts = 0

    while attempts < MAX_LOGIN_ATTEMPTS:

        email = input("\nEmail: ").strip().lower()

        password = getpass("Password: ")

        cursor.execute(
            """
            SELECT
                user_id,
                username,
                email,
                organisation_id

            FROM users

            WHERE email = ?
            AND password = ?
            """,
            (
                email,
                hash_password(password)
            )
        )

        user = cursor.fetchone()

        if user:

            connection.close()

            print("\nLogin successful.")
            print(f"Welcome back, {user[1]}!")

            return {
                "user_id": user[0],
                "username": user[1],
                "email": user[2],
                "organisation_id": user[3]
            }

        attempts += 1

        remaining = MAX_LOGIN_ATTEMPTS - attempts

        if remaining > 0:

            print("\nInvalid email or password.")
            print(f"Attempts remaining: {remaining}")

        else:

            print("\nMaximum login attempts reached.")

    connection.close()

    return None