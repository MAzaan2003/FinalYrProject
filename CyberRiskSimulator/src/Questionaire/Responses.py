"""
Responses.py

Stores and displays questionnaire answers.
"""


class Responses:


    def __init__(self):

        self.answers = {}



    def save_answers(self, answers):

        self.answers = answers



    def get_answers(self):

        return self.answers



    def display_answers(self):


        print("\n")
        print("=" * 50)
        print("       QUESTIONNAIRE RESPONSES")
        print("=" * 50)


        for question, answer in self.answers.items():

            symbol = "✓" if answer == "yes" else "✗"


            print(
                f"{symbol} {question}"
            )

            print(
                f"Answer: {answer.upper()}\n"
            )