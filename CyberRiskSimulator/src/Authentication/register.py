"""
register.py

Handles new user registration for the Cyber Risk Simulator.
"""

import hashlib
from Database.database import get_connection


def hash_password(password):
    """
    Encrypts the password before storing it.
    """

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def register():

    print("\n================================")
    print("       CREATE NEW ACCOUNT")
    print("================================\n")


    # User details

    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")


    # Organisation details

    print("\n--- Organisation Details ---")

    organisation_name = input("Organisation Name: ")
    industry = input("Industry: ")

    employees = int(
        input("Number of Employees: ")
    )


    connection = get_connection()
    cursor = connection.cursor()


    try:

        # Create organisation first

        cursor.execute(
        """
        INSERT INTO organisations
        (
            name,
            industry,
            employees
        )

        VALUES (?, ?, ?)

        """,
        (
            organisation_name,
            industry,
            employees
        ))


        organisation_id = cursor.lastrowid



        # Create user linked to organisation

        cursor.execute(
        """
        INSERT INTO users
        (
            username,
            email,
            password,
            organisation_id
        )

        VALUES (?, ?, ?, ?)

        """,
        (
            username,
            email,
            hash_password(password),
            organisation_id
        ))



        connection.commit()


        print("\nAccount created successfully!")
        print(
            f"Organisation: {organisation_name}"
        )


    except Exception as error:

        connection.rollback()

        print(
            "\nRegistration failed:"
        )

        print(error)



    finally:

        connection.close()
        