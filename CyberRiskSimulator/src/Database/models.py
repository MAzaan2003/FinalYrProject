"""
models.py

Contains the main data models for the
Cyber Risk Simulator.
"""

from dataclasses import dataclass, field
from typing import Dict



# ==========================
# USER MODEL
# ==========================

@dataclass
class User:
    """
    Represents a system user.
    """

    user_id: int
    username: str
    email: str
    organisation_id: int



# ==========================
# ORGANISATION MODEL
# ==========================

@dataclass
class Organisation:
    """
    Stores organisation information.
    """

    organisation_id: int
    name: str
    industry: str
    employees: int



# ==========================
# ASSESSMENT MODEL
# ==========================

@dataclass
class Assessment:
    """
    Stores completed risk assessments.
    """

    assessment_id: int
    organisation_id: int
    date: str
    score: int
    risk_level: str



# ==========================
# RESPONSE MODEL
# ==========================

@dataclass
class Response:
    """
    Stores individual questionnaire answers.
    """

    question: str
    answer: str



# ==========================
# QUESTIONNAIRE MODEL
# ==========================

@dataclass
class Questionnaire:
    """
    Stores questionnaire responses.
    """

    responses: Dict[str, str] = field(
        default_factory=dict
    )


    def add_response(
            self,
            question,
            answer
    ):

        self.responses[question] = answer



    def get_responses(self):

        return self.responses



# ==========================
# RISK MODEL
# ==========================

@dataclass
class Risk:
    """
    Represents a cybersecurity risk.
    """

    name: str
    category: str
    likelihood: int
    impact: int



    def score(self):

        return self.likelihood * self.impact