def ask_questions():

    print("\n========== Cyber Security Questionnaire ==========\n")

    questions = [
        "Do you use Multi-Factor Authentication (MFA)?",
        "Do you regularly update operating systems?",
        "Are backups performed regularly?",
        "Are backups tested regularly?",
        "Do employees receive cybersecurity awareness training?",
        "Is antivirus software installed on all devices?",
        "Do you have a firewall enabled?",
        "Are passwords changed regularly?",
        "Do you encrypt sensitive company data?",
        "Do you use secure SQL queries (Prepared Statements)?"
    ]

    answers = {}

    for question in questions:

        while True:

            answer = input(question + " (yes/no): ").lower()

            if answer in ["yes", "no"]:
                answers[question] = answer
                break

            print("Please answer yes or no.")

    return answers