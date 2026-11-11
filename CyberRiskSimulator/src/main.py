"""
main.py

Main entry point for the Cyber Risk Simulator.
"""

from Database.database import create_database
from Authentication.register import register
from Authentication.login import login
from Dashboard.dashboard import show_dashboard



def main():

    # Create database tables when program starts
    create_database()


    while True:

        print("\n")
        print("=" * 60)
        print("              CYBER RISK SIMULATOR")
        print("=" * 60)


        print("""
1. Register

2. Login

3. Exit

""")


        choice = input("Select option: ")



        # -------------------------
        # REGISTER
        # -------------------------

        if choice == "1":

            register()



        # -------------------------
        # LOGIN
        # -------------------------

        elif choice == "2":

            user = login()


            if user:

                show_dashboard(user)



        # -------------------------
        # EXIT
        # -------------------------

        elif choice == "3":

            print(
                "\nThank you for using Cyber Risk Simulator."
            )

            break



        else:

            print(
                "\nInvalid choice. Please select 1, 2 or 3."
            )





if __name__ == "__main__":

    main()