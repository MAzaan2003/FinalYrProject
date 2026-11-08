from Questionaire.Organisation import Organisation

from Questionaire.Questions import ask_questions

from Questionaire.Responses import Responses


from Risk_engine.risk_calculator import RiskCalculator


from Reports.report_generator import ReportGenerator




def main():


    print("=" * 50)

    print("        Cyber Risk Simulator")

    print("=" * 50)



    organisation = Organisation()


    organisation.collect_details()



    answers = ask_questions()



    responses = Responses()

    responses.save_answers(
        answers
    )



    risk = RiskCalculator(
        answers
    )


    risk.calculate_score()



    report = ReportGenerator()



    report.generate_report(

        organisation,

        answers,

        risk.get_results()

    )





if __name__ == "__main__":

    main()