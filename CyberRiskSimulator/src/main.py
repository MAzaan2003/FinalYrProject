from questionnaire.organisation import Organisation
from questionnaire.questions import ask_questions
from questionnaire.responses import Responses


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

    # Store responses
    responses = Responses()
    responses.save_answers(answers)

    # Display results
    organisation.display_details()
    responses.display_answers()

    print("\nAssessment Complete!")
    print("Risk scoring will be added in the next stage.")


if __name__ == "__main__":
    main()
    