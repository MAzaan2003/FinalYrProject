"""
register.py

Handles new user registration for the Cyber Risk Simulator.
"""

import hashlib
import re

from getpass import getpass

from Database.database import get_connection



def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



def validate_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(
        pattern,
        email
    )



def validate_password(password):

    if len(password) < 8:
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[!@#$%^&*]", password):
        return False

    return True



def enter_password():

    show = input(
        "Show password? (y/n): "
    ).lower()



    if show == "y":

        return input(
            "Password: "
        )


    else:

        return getpass(
            "Password: "
        )



def register():

    print("\n" + "=" * 60)
    print("              CREATE NEW ACCOUNT")
    print("=" * 60)



    connection = get_connection()

    cursor = connection.cursor()



    username = input(
        "\nUsername: "
    ).strip()



    email = input(
        "Email: "
    ).strip().lower()



    if not validate_email(email):

        print(
            "Invalid email format."
        )

        connection.close()

        return



    while True:


        password = enter_password()


        confirm = enter_password()



        if password != confirm:


            print(
                "\nPasswords do not match."
            )

            continue



        if not validate_password(password):


            print(
                """
Password requirements:

✓ Minimum 8 characters
✓ One uppercase letter
✓ One lowercase letter
✓ One number
✓ One special character

"""
            )

            continue



        break




    print(
        "\n--- Organisation Details ---"
    )



    organisation_name = input(
        "Organisation Name: "
    )


    industry = input(
        "Industry: "
    )



    while True:

        try:

            employees = int(
                input(
                    "Number of Employees: "
                )
            )

            break


        except ValueError:

            print(
                "Please enter numbers only."
            )



    try:


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

            )
        )



        organisation_id = cursor.lastrowid



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

            )
        )



        connection.commit()



        print(
            "\nAccount created successfully!"
        )

        print(
            f"Welcome {username}"
        )



    except Exception as error:


        connection.rollback()


        print(
            "\nRegistration failed:"
        )

        print(error)



    finally:


        connection.close()