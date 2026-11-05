"""
Calculates the organisation's cyber risk score.
"""

from Risk_engine.risk_levels import get_risk_level


class RiskCalculator:

    def __init__(self, answers):
        self.answers = answers
        self.score = 0
        self.level = ""


    def calculate_score(self):

        score = 0

        # Score based on questionnaire responses
        for answer in self.answers:

            answer = answer.lower()

            if answer == "yes":
                score += 0          # Secure answer

            elif answer == "maybe":
                score += 10

            elif answer == "no":
                score += 20


        # Maximum score = 100
        if score > 100:
            score = 100

        self.score = score
        self.level = get_risk_level(score)

        return score


    def calculate_percentage(self):

        return self.score


    def get_risk_level(self):

        return self.level


    def display_results(self):

        print("\n")
        print("=" * 40)
        print(" Cyber Risk Assessment")
        print("=" * 40)

        print(f"Risk Score : {self.score}/100")
        print(f"Risk Level : {self.level}")

        print("=" * 40)

        