from Questionaire.Organisation import Organisation
from Questionaire.Questions import ask_questions
from Questionaire.Responses import Responses

from Database.database import Database
from Database.models import Risk


def main():
    print("=" * 50)
    print("        Cyber Risk Simulator")
    print("=" * 50)

    # Create database
    db = Database()

    # Create Organisation object
    organisation = Organisation()

    # Collect organisation information
    organisation.collect_details()

    # Save organisation to database
    db.add_organisation(organisation)

    # Ask cybersecurity questions
    answers = ask_questions()

    # Store responses
    responses = Responses()
    responses.save_answers(answers)

    # Example risk entry
    risk = Risk(
        name="Phishing Attack",
        category="Social Engineering",
        likelihood=4,
        impact=5
    )

    db.add_risk(risk)

    # Display results
    organisation.display_details()
    responses.display_answers()

    print("\nRisk Score:", risk.score())

    print("\nAssessment Complete!")


if __name__ == "__main__":
    main()