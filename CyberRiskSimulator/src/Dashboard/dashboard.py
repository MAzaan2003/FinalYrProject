"""
dashboard.py

Main user dashboard after login.
"""

from Questionaire.Questions import ask_questions
from Risk_engine.risk_calculator import RiskCalculator
from Reports.report_generator import ReportGenerator
from Database.database import get_connection



def show_dashboard(user):

    while True:

        print("\n")
        print("=" * 60)
        print("              CYBER RISK DASHBOARD")
        print("=" * 60)

        print(
            f"\nWelcome, {user['username']}"
        )


        print("""
------------------------------------------------

1. Start Cyber Risk Assessment

2. View Assessment History

3. View Organisation Details

4. Logout

------------------------------------------------
        """)


        choice = input("Select option: ")



        if choice == "1":

            start_assessment(user)



        elif choice == "2":

            view_history(user)



        elif choice == "3":

            view_organisation(user)



        elif choice == "4":

            print("\nLogging out...")
            break



        else:

            print("\nInvalid option.")





def start_assessment(user):

    print("\nStarting Cyber Security Assessment...\n")


    # Existing questionnaire

    answers = ask_questions()



    # Existing risk calculator

    calculator = RiskCalculator(
        answers
    )


    calculator.calculate_score()


    result = calculator.get_results()



    print("\nAssessment Complete")

    print(
        f"Score: {result['score']}%"
    )

    print(
        f"Risk Level: {result['level']}"
    )


    save_assessment(
        user,
        result,
        answers
    )



    print("\nAssessment saved successfully.")





def save_assessment(user, result, answers):

    connection = get_connection()

    cursor = connection.cursor()



    from datetime import datetime


    cursor.execute(
    """
    INSERT INTO assessments
    (
        organisation_id,
        date,
        score,
        level
    )

    VALUES (?, ?, ?, ?)

    """,
    (
        user["organisation_id"],
        datetime.now().strftime("%d/%m/%Y"),
        result["score"],
        result["level"]
    ))



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
        ))



    connection.commit()

    connection.close()





def view_history(user):

    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
    """
    SELECT date, score, level

    FROM assessments

    WHERE organisation_id = ?

    """,
    (
        user["organisation_id"],
    ))



    history = cursor.fetchall()


    connection.close()



    print("\n========== ASSESSMENT HISTORY ==========\n")


    if not history:

        print("No previous assessments found.")


    else:

        for item in history:

            print(
                f"Date: {item[0]}"
            )

            print(
                f"Score: {item[1]}%"
            )

            print(
                f"Risk Level: {item[2]}"
            )

            print("-" * 30)





def view_organisation(user):

    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
    """
    SELECT name, industry, employees

    FROM organisations

    WHERE organisation_id = ?

    """,
    (
        user["organisation_id"],
    ))



    organisation = cursor.fetchone()


    connection.close()



    print("\n========== ORGANISATION ==========\n")


    if organisation:

        print(
            f"Name: {organisation[0]}"
        )

        print(
            f"Industry: {organisation[1]}"
        )

        print(
            f"Employees: {organisation[2]}"
        )

    else:

        print("Organisation not found.")