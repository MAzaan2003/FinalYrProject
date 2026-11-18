"""
risk_calculator.py

Calculates cybersecurity risk score,
risk level and recommendations.
"""


class RiskCalculator:


    def __init__(self, answers):

        self.answers = answers
        self.score = 0
        self.level = ""
        self.maturity = ""
        self.recommendations = []



    def calculate_score(self):

        total_questions = len(self.answers)

        risk_points = 0


        for question, answer in self.answers.items():

            if answer.lower() == "no":

                risk_points += 1

                self.generate_recommendation(question)



        # Convert weaknesses into percentage

        self.score = int(
            (risk_points / total_questions) * 100
        )


        self.calculate_risk_level()


        return self.score




    def calculate_risk_level(self):


        if self.score <= 20:

            self.level = "Low"


            self.maturity = "Strong Cybersecurity Posture"



        elif self.score <= 50:

            self.level = "Medium"


            self.maturity = "Developing Cybersecurity Posture"



        elif self.score <= 75:

            self.level = "High"


            self.maturity = "Weak Cybersecurity Posture"



        else:

            self.level = "Critical"


            self.maturity = "Immediate Improvement Required"




    def generate_recommendation(self, question):


        recommendations = {


            "Multi-Factor Authentication":
            "Enable MFA for all important accounts.",


            "password":
            "Improve password policies and enforce strong passwords.",


            "updated":
            "Apply security updates and patches regularly.",


            "antivirus":
            "Install and maintain endpoint protection.",


            "firewall":
            "Configure and monitor firewall protection.",


            "network":
            "Improve network monitoring and access controls.",


            "encrypted":
            "Encrypt sensitive business information.",


            "backup":
            "Perform regular backups and test recovery.",


            "training":
            "Provide cybersecurity awareness training.",


            "phishing":
            "Train employees to identify phishing attacks.",


            "incident":
            "Create and test an incident response plan.",


            "vulnerabilities":
            "Perform regular vulnerability assessments.",


            "physical":
            "Improve physical security controls."

        }


        for keyword, recommendation in recommendations.items():


            if keyword.lower() in question.lower():

                self.recommendations.append(
                    recommendation
                )

                return



        self.recommendations.append(
            "Review and improve: " + question
        )




    def get_results(self):


        return {


            "score": self.score,


            "level": self.level,


            "maturity": self.maturity,


            "recommendations": self.recommendations

        }