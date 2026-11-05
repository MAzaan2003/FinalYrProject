from Questionaire.Organisation import Organisation
from Questionaire.Questions import ask_questions
from Questionaire.Responses import Responses

from Risk_engine.risk_calculator import RiskCalculator


def main():

    print("=" * 50)
    print("        Cyber Risk Simulator")
    print("=" * 50)

    # Create Organisation object
    organisation = Organisation()

    # Collect organisation information
    organisation.collect_details()

    # Ask cybersecurity questions
    answers = ask_questions()

    # Save responses
    responses = Responses()
    responses.save_answers(answers)

    # Display organisation details
    organisation.display_details()

    # Display questionnaire responses
    responses.display_answers()

    # Calculate cyber risk
    risk = RiskCalculator(answers)

    risk.calculate_score()

    # Display risk assessment
    risk.display_results()

    print("\nAssessment Complete!")
    print("Simulation module will be added in the next stage.")


if __name__ == "__main__":
    main()