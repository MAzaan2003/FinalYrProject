"""
Questions.py

Handles the cybersecurity questionnaire.
"""


def ask_questions():

    print("\n")
    print("=" * 60)
    print("          CYBER SECURITY QUESTIONNAIRE")
    print("=" * 60)


    questions = {

        1: "Do you use Multi-Factor Authentication (MFA)?",

        2: "Do you regularly update operating systems?",

        3: "Are backups performed regularly?",

        4: "Are backups tested regularly?",

        5: "Do employees receive cybersecurity awareness training?",

        6: "Is antivirus software installed on all devices?",

        7: "Do you have a firewall enabled?",

        8: "Are passwords changed regularly?",

        9: "Do you encrypt sensitive company data?",

        10: "Do you use secure SQL queries (Prepared Statements)?"

    }


    answers = {}


    for question_id, question in questions.items():


        while True:


            answer = input(
                f"\n{question}\n(yes/no): "
            ).lower()



            if answer in ["yes", "no"]:

                answers[question] = answer

                break


            else:

                print(
                    "Please enter yes or no."
                )


    return answers