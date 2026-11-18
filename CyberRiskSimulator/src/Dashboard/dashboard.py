"""
dashboard.py

Main user dashboard after login.
"""


from Questionaire.Questions import ask_questions

from Risk_engine.risk_calculator import RiskCalculator

from Reports.report_generator import ReportGenerator

from Database.database import get_connection

from datetime import datetime



def show_dashboard(user):


    while True:


        print("\n" + "=" * 70)
        print("                 CYBER RISK DASHBOARD")
        print("=" * 70)


        print(
            f"\nWelcome, {user['username']}"
        )


        print("""
------------------------------------------------------------

1. Start Cyber Risk Assessment

2. View Assessment History

3. Generate Latest Report

4. View Organisation Details

5. Logout

------------------------------------------------------------
        """)


        choice = input(
            "Select option: "
        )



        if choice == "1":

            start_assessment(user)



        elif choice == "2":

            view_history(user)



        elif choice == "3":

            generate_report(user)



        elif choice == "4":

            view_organisation(user)



        elif choice == "5":

            print("\nLogging out...")
            break



        else:

            print("\nInvalid option.")





def start_assessment(user):


    print("\nStarting Cyber Risk Assessment...\n")


    answers = ask_questions()



    calculator = RiskCalculator(
        answers
    )


    calculator.calculate_score()


    result = calculator.get_results()



    print("\n" + "=" * 70)
    print("                 ASSESSMENT RESULT")
    print("=" * 70)


    print(
        f"\nRisk Score: {result['score']}%"
    )


    print(
        f"Risk Level: {result['level']}"
    )


    print(
        f"Security Maturity: {result['maturity']}"
    )


    print("\nRecommendations")

    print("-" * 50)



    if result["recommendations"]:


        for item in result["recommendations"]:

            print(
                "- " + item
            )


    else:

        print(
            "No recommendations required."
        )



    save_assessment(
        user,
        result,
        answers
    )


    print(
        "\nAssessment saved successfully."
    )





def save_assessment(user, result, answers):


    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
        """
        INSERT INTO assessments
        (
            organisation_id,
            completed_by,
            date,
            score,
            level,
            maturity
        )

        VALUES (?, ?, ?, ?, ?, ?)

        """,

        (

            user["organisation_id"],

            user["user_id"],

            datetime.now().strftime(
                "%d/%m/%Y %H:%M"
            ),

            result["score"],

            result["level"],

            result["maturity"]

        )
    )



    assessment_id = cursor.lastrowid



    for question, answer in answers.items():


        cursor.execute(
            """
            INSERT INTO responses
            (
                assessment_id,
                question,
                answer
            )

            VALUES (?, ?, ?)

            """,

            (

                assessment_id,

                question,

                answer

            )
        )



    connection.commit()

    connection.close()





def generate_report(user):


    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
        """
        SELECT
            score,
            level,
            maturity

        FROM assessments

        WHERE organisation_id = ?

        ORDER BY assessment_id DESC

        LIMIT 1

        """,

        (

            user["organisation_id"],

        )
    )



    result = cursor.fetchone()



    if not result:


        print(
            "\nNo assessment found. Complete an assessment first."
        )

        connection.close()

        return



    cursor.execute(
        """
        SELECT
            question,
            answer

        FROM responses

        WHERE assessment_id =
        (
            SELECT MAX(assessment_id)

            FROM assessments

            WHERE organisation_id = ?
        )

        """,

        (

            user["organisation_id"],

        )
    )



    responses = cursor.fetchall()



    cursor.execute(
        """
        SELECT
            name,
            industry,
            employees

        FROM organisations

        WHERE organisation_id = ?

        """,

        (

            user["organisation_id"],

        )
    )



    organisation_data = cursor.fetchone()


    connection.close()



    class Organisation:

        def __init__(self, data):

            self.name = data[0]

            self.industry = data[1]

            self.employees = data[2]



    organisation = Organisation(
        organisation_data
    )



    answers = dict(responses)



    risk = {


        "score": result[0],

        "level": result[1],

        "maturity": result[2],


        "recommendations":

        [

            "Review unanswered security controls.",

            "Improve employee cybersecurity awareness.",

            "Maintain regular security reviews."

        ]

    }



    report = ReportGenerator()



    report.generate_report(

        user,

        organisation,

        answers,

        risk

    )





def view_history(user):


    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
        """
        SELECT
            date,
            score,
            level

        FROM assessments

        WHERE organisation_id = ?

        ORDER BY assessment_id DESC

        """,

        (

            user["organisation_id"],

        )
    )



    history = cursor.fetchall()


    connection.close()



    print("\n" + "=" * 60)
    print("              ASSESSMENT HISTORY")
    print("=" * 60)



    if not history:


        print(
            "\nNo previous assessments."
        )


    else:


        for item in history:


            print(
                f"\nDate: {item[0]}"
            )

            print(
                f"Score: {item[1]}%"
            )

            print(
                f"Risk Level: {item[2]}"
            )

            print("-" * 40)





def view_organisation(user):


    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
        """
        SELECT
            name,
            industry,
            employees

        FROM organisations

        WHERE organisation_id = ?

        """,

        (

            user["organisation_id"],

        )
    )


    organisation = cursor.fetchone()


    connection.close()



    print("\n" + "=" * 60)
    print("              ORGANISATION DETAILS")
    print("=" * 60)



    if organisation:


        print(
            "\nName:",
            organisation[0]
        )


        print(
            "Industry:",
            organisation[1]
        )


        print(
            "Employees:",
            organisation[2]
        )


    else:


        print(
            "Organisation not found."
        )