class Responses:
    """
    Stores questionnaire responses.
    """

    def __init__(self):
        self.answers = {}

    def save_answers(self, answers):
        self.answers = answers

    def display_answers(self):

        print("\n========== Questionnaire Responses ==========\n")

        for question, answer in self.answers.items():
            print(f"{question}")
            print(f"Answer: {answer}\n")