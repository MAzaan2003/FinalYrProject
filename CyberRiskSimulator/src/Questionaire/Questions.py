"""
Questions.py

Cyber Risk Simulator Questionnaire

This module displays a cybersecurity questionnaire,
collects responses and returns them to the dashboard.
"""


def ask_questions():

    questions = {

        # Governance
        1: "Does your organisation have a documented cybersecurity policy?",

        # Identity & Access Management
        2: "Is Multi-Factor Authentication (MFA) enabled for important accounts?",

        3: "Are strong password policies enforced across the organisation?",

        4: "Are user accounts reviewed regularly to remove unnecessary access?",

        # Asset Management
        5: "Does the organisation maintain an inventory of its hardware and software assets?",

        # System Security
        6: "Are operating systems and software updated regularly with security patches?",

        7: "Is antivirus or endpoint protection installed on all company devices?",

        # Network Security
        8: "Is a firewall configured and enabled to protect the network?",

        9: "Is network access restricted to authorised users and devices?",

        10: "Is network activity monitored for suspicious behaviour?",

        # Data Protection
        11: "Is sensitive business data encrypted when stored or transmitted?",

        12: "Are important files backed up regularly?",

        13: "Are backup restoration procedures tested periodically?",

        # Employee Awareness
        14: "Do employees receive regular cybersecurity awareness training?",

        15: "Are employees trained to recognise phishing and social engineering attacks?",

        # Incident Response
        16: "Does the organisation have a documented incident response plan?",

        17: "Are cybersecurity incidents recorded and reviewed after they occur?",

        # Application Security
        18: "Are applications tested for security vulnerabilities before deployment?",

        # Physical Security
        19: "Is physical access to servers and sensitive equipment restricted?",

        # Compliance
        20: "Are cybersecurity policies reviewed and updated regularly?"
    }

    answers = {}

    total_questions = len(questions)

    print("\n" + "=" * 70)
    print("           CYBER SECURITY RISK ASSESSMENT")
    print("=" * 70)

    for number, question in questions.items():

        print(f"\nQuestion {number} of {total_questions}")
        print("-" * 70)
        print(question)

        while True:

            answer = input("\nAnswer (yes/no): ").strip().lower()

            if answer in ("yes", "no"):

                answers[question] = answer
                break

            print("Invalid input. Please enter 'yes' or 'no'.")

    print("\nAssessment completed successfully.\n")

    return answers