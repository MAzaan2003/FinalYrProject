"""
main.py

Main entry point for Cyber Risk Simulator.
"""


from Database.database import create_database

from Authentication.register import register

from Authentication.login import login

from Dashboard.dashboard import show_dashboard

from utils.ui import banner, title, success, error



def main():


    # Start database

    create_database()


    # Display banner

    banner()

    title("CYBER RISK SIMULATOR")



    while True:


        print()


        print("""
        1. Register

        2. Login

        3. Exit
        """)



        choice = input(
            "Select option: "
        )



        # ==========================
        # REGISTER
        # ==========================

        if choice == "1":


            try:

                register()

                success(
                    "Registration completed."
                )


            except Exception as e:

                error(
                    f"Registration failed: {e}"
                )



        # ==========================
        # LOGIN
        # ==========================

        elif choice == "2":


            try:


                user = login()



                if user:


                    success(
                        "Login successful."
                    )


                    show_dashboard(
                        user
                    )


                else:


                    error(
                        "Login failed."
                    )



            except Exception as e:


                error(
                    f"Login error: {e}"
                )



        # ==========================
        # EXIT
        # ==========================

        elif choice == "3":


            print()

            success(
                "Thank you for using Cyber Risk Simulator."
            )

            break



        else:


            error(
                "Invalid option. Please choose 1, 2 or 3."
            )





if __name__ == "__main__":

    main()