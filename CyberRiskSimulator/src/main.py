"""
main.py

Main entry point for Cyber Risk Simulator.
"""


from Database.database import create_database

from Authentication.register import register

from Authentication.login import login

from Dashboard.dashboard import show_dashboard


def display_title():

    print("\n" + "=" * 70)
    print("              CYBER RISK SIMULATOR")
    print("=" * 70)



def main():


    try:

        # Initialise database

        create_database()


    except Exception as error:


        print(
            "\nDatabase startup failed."
        )

        print(error)

        return



    display_title()



    while True:


        print("""

------------------------------------------------------------

1. Register Account

2. Login

3. Exit

------------------------------------------------------------

        """)



        choice = input(
            "Select option: "
        ).strip()



        # ==========================
        # REGISTER
        # ==========================


        if choice == "1":


            try:


                register()



            except Exception as error:


                print(
                    "\nRegistration error:"
                )

                print(error)



        # ==========================
        # LOGIN
        # ==========================


        elif choice == "2":


            try:


                user = login()



                if user:


                    show_dashboard(
                        user
                    )



            except Exception as error:


                print(
                    "\nLogin error:"
                )

                print(error)



        # ==========================
        # EXIT
        # ==========================


        elif choice == "3":


            print(
                "\nThank you for using Cyber Risk Simulator."
            )


            break



        else:


            print(
                "\nInvalid selection. Choose 1, 2 or 3."
            )





if __name__ == "__main__":

    main()