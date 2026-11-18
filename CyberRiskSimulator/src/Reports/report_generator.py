"""
report_generator.py

Creates cybersecurity assessment reports.
"""

from datetime import datetime
import os


class ReportGenerator:


    def generate_report(
            self,
            user,
            organisation,
            answers,
            risk
    ):


        report_date = datetime.now().strftime(
            "%d %B %Y %H:%M"
        )


        filename = (
            f"Cyber_Risk_Report_{user['username']}.txt"
        )


        reports_folder = "Reports/generated_reports"


        os.makedirs(
            reports_folder,
            exist_ok=True
        )


        filepath = os.path.join(
            reports_folder,
            filename
        )


        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:


            file.write(
                "=" * 70
                + "\n"
            )

            file.write(
                "              CYBER RISK SIMULATOR REPORT\n"
            )

            file.write(
                "=" * 70
                + "\n\n"
            )



            file.write(
                f"Assessment Date: {report_date}\n"
            )


            file.write(
                f"User: {user['username']}\n\n"
            )



            file.write(
                "-" * 70
                + "\n"
            )

            file.write(
                "ORGANISATION DETAILS\n"
            )

            file.write(
                "-" * 70
                + "\n"
            )



            file.write(
                f"Organisation: {organisation.name}\n"
            )


            file.write(
                f"Industry: {organisation.industry}\n"
            )


            file.write(
                f"Employees: {organisation.employees}\n\n"
            )



            file.write(
                "-" * 70
                + "\n"
            )

            file.write(
                "CYBERSECURITY ASSESSMENT RESULT\n"
            )

            file.write(
                "-" * 70
                + "\n"
            )



            file.write(
                f"Risk Score: {risk['score']}%\n"
            )


            file.write(
                f"Risk Level: {risk['level']}\n"
            )


            file.write(
                f"Security Maturity: {risk['maturity']}\n\n"
            )



            file.write(
                "-" * 70
                + "\n"
            )

            file.write(
                "QUESTIONNAIRE RESPONSES\n"
            )

            file.write(
                "-" * 70
                + "\n"
            )



            for question, answer in answers.items():


                file.write(
                    f"\nQuestion: {question}\n"
                )


                file.write(
                    f"Answer: {answer.upper()}\n"
                )



            file.write(
                "\n\n"
            )


            file.write(
                "-" * 70
                + "\n"
            )

            file.write(
                "RECOMMENDATIONS\n"
            )

            file.write(
                "-" * 70
                + "\n"
            )



            if risk["recommendations"]:


                for number, item in enumerate(
                    risk["recommendations"],
                    start=1
                ):

                    file.write(
                        f"{number}. {item}\n"
                    )


            else:


                file.write(
                    "No recommendations required.\n"
                )



            file.write(
                "\n"
                + "=" * 70
                + "\n"
            )


            file.write(
                "Assessment Completed Successfully\n"
            )


            file.write(
                "=" * 70
                + "\n"
            )



        print("\nReport generated successfully.")

        print(
            f"Saved location: {filepath}"
        )


        return filepath