from datetime import datetime



class ReportGenerator:


    def generate_report(
            self,
            organisation,
            answers,
            risk):


        print("\n")

        print("=" * 60)

        print("              CYBER RISK SIMULATOR")

        print("=" * 60)



        print(
            f"\nAssessment Date: "
            f"{datetime.now().strftime('%d %B %Y')}"
        )



        print("\n------------------------------------------------")

        print("ORGANISATION DETAILS")

        print("------------------------------------------------")



        print(
            f"Organisation Name : {organisation.name}"
        )

        print(
            f"Industry          : {organisation.industry}"
        )

        print(
            f"Employees         : {organisation.employees}"
        )



        print("\n------------------------------------------------")

        print("CYBER SECURITY QUESTIONNAIRE")

        print("------------------------------------------------")



        for question, answer in answers.items():


            symbol = "✓" if answer == "yes" else "✗"


            print(
                f"{symbol} {question} : {answer.upper()}"
            )



        print("\n------------------------------------------------")

        print("CYBER RISK ASSESSMENT")

        print("------------------------------------------------")



        print(
            f"Risk Score : {risk['score']}%"
        )


        print(
            f"Risk Level : {risk['level']}"
        )



        print("\n------------------------------------------------")

        print("RECOMMENDATIONS")

        print("------------------------------------------------")



        recommendations = [

            "Enable Multi-Factor Authentication.",

            "Regularly update systems.",

            "Test backups.",

            "Train employees.",

            "Use prepared SQL statements.",

            "Enable firewall protection."

        ]



        for i, item in enumerate(
            recommendations,
            start=1
        ):

            print(
                f"{i}. {item}"
            )



        print("\n================================================")

        print("Assessment Status : COMPLETE")

        print("================================================")




        