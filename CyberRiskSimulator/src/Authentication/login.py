"""
login.py

Handles user login for the Cyber Risk Simulator.
"""

import hashlib
from Database.database import get_connection



def hash_password(password):
    """
    Hash password so it matches the stored database password.
    """

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def login():

    print("\n================================")
    print("          USER LOGIN")
    print("================================\n")


    email = input("Email: ")
    password = input("Password: ")


    connection = get_connection()
    cursor = connection.cursor()


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


    connection.close()



    if user:

        print("\nLogin successful!")
        print(
            f"Welcome {user[1]}"
        )


        return {
            "user_id": user[0],
            "username": user[1],
            "email": user[2],
            "organisation_id": user[3]
        }


    else:

        print("\nInvalid email or password.")

        return None