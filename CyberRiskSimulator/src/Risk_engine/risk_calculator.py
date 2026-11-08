from Risk_engine.risk_levels import get_risk_level



class RiskCalculator:


    def __init__(self, answers):

        self.answers = answers
        self.score = 0
        self.level = ""



    def calculate_score(self):

        risk_points = 0

        total = len(self.answers)



        for answer in self.answers.values():


            if answer.lower() == "no":

                risk_points += 1



        self.score = int(
            (risk_points / total) * 100
        )


        self.level = get_risk_level(
            self.score
        )


        return self.score



    def get_results(self):

        return {

            "score": self.score,

            "level": self.level

        }