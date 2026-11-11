"""
report_generator.py

Creates cybersecurity assessment reports.
"""


from datetime import datetime



class ReportGenerator:



    def generate_report(
            self,
            user,
            organisation,
            answers,
            risk):


        print("\n")

        print("=" * 60)
        print("              CYBER RISK SIMULATOR")
        print("=" * 60)



        print(
            "\nAssessment Date:",
            datetime.now().strftime("%d %B %Y")
        )


        print(
            f"User: {user['username']}"
        )



        print("\n")
        print("-" * 50)
        print("ORGANISATION DETAILS")
        print("-" * 50)



        print(
            f"Organisation Name: {organisation.name}"
        )


        print(
            f"Industry: {organisation.industry}"
        )


        print(
            f"Employees: {organisation.employees}"
        )



        print("\n")
        print("-" * 50)
        print("QUESTIONNAIRE RESULTS")
        print("-" * 50)



        for question, answer in answers.items():


            symbol = "✓" if answer == "yes" else "✗"


            print(
                f"{symbol} {question}"
            )

            print(
                f"Answer: {answer.upper()}"
            )



        print("\n")
        print("-" * 50)
        print("CYBER RISK ASSESSMENT")
        print("-" * 50)



        print(
            f"Risk Score: {risk['score']}%"
        )


        print(
            f"Risk Level: {risk['level']}"
        )



        print("\n")
        print("-" * 50)
        print("RECOMMENDATIONS")
        print("-" * 50)



        recommendations = [

            "Enable Multi-Factor Authentication.",

            "Regularly update systems.",

            "Test backups regularly.",

            "Provide cybersecurity awareness training.",

            "Use secure SQL queries.",

            "Enable firewall protection."

        ]



        for number, recommendation in enumerate(
                recommendations,
                start=1
        ):

            print(
                f"{number}. {recommendation}"
            )



        print("\n")
        print("=" * 60)
        print("Assessment Status: COMPLETE")
        print("=" * 60)