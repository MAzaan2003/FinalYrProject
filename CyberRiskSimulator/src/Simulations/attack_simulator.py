"""
attack_simulator.py

Educational cybersecurity attack simulator.

Simulates common cyber threats and provides
security awareness information.
"""


import random
import time



def display_line():

    print("-" * 60)



def run_simulator(user):


    while True:


        print("\n" + "=" * 60)

        print("              CYBER ATTACK SIMULATOR")

        print("=" * 60)


        print(
            f"\nUser: {user['username']}"
        )


        print("""
------------------------------------------------------------

1. Phishing Attack Simulation

2. Ransomware Scenario

3. Password Attack Scenario

4. SQL Injection Scenario

5. Return to Dashboard

------------------------------------------------------------
        """)



        choice = input(
            "Select simulation: "
        )



        if choice == "1":

            phishing_simulation()



        elif choice == "2":

            ransomware_simulation()



        elif choice == "3":

            password_simulation()



        elif choice == "4":

            sql_simulation()



        elif choice == "5":

            break



        else:

            print(
                "Invalid option."
            )





def loading():

    print(
        "\nRunning simulation",
        end=""
    )


    for i in range(3):

        time.sleep(0.5)

        print(
            ".",
            end=""
        )


    print()





def phishing_simulation():


    print("\nPHISHING ATTACK SIMULATION")

    display_line()


    loading()


    print(
        """
Scenario:

An employee receives an email claiming to be
from the IT department.

The email asks the employee to verify their
account details.

The employee clicks the link and provides
credentials.

Result:

An attacker gains access to the account.

Impact:

- Data exposure
- Account compromise
- Possible financial loss

Prevention:

✓ Employee awareness training
✓ MFA enabled
✓ Verify suspicious emails
"""
    )





def ransomware_simulation():


    print("\nRANSOMWARE SIMULATION")

    display_line()


    loading()


    print(
        """
Scenario:

A malicious file is opened from an unknown
email attachment.

The attacker encrypts important files.

Result:

The organisation cannot access its data.

Impact:

- Business disruption
- Data loss
- Recovery costs

Prevention:

✓ Regular backups
✓ Endpoint protection
✓ Patch management
"""
    )





def password_simulation():


    print("\nPASSWORD ATTACK SIMULATION")

    display_line()


    loading()


    attempts = random.randint(
        1000,
        100000
    )


    print(
        f"""
Scenario:

An attacker attempts to guess a weak password.

Simulation:

Possible attempts:
{attempts:,}

Result:

Weak passwords may be compromised.

Prevention:

✓ Strong passwords
✓ Password managers
✓ Multi-Factor Authentication
"""
    )





def sql_simulation():


    print("\nSQL INJECTION SIMULATION")

    display_line()


    loading()


    print(
        """
Scenario:

A vulnerable application does not properly
validate user input.

An attacker attempts to manipulate database
queries.

Impact:

- Unauthorised data access
- Data modification
- Information disclosure

Prevention:

✓ Prepared statements
✓ Input validation
✓ Secure coding practices
"""
    )