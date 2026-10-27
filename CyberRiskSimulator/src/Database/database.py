from .models import Organisation, Risk


class Database:
    def __init__(self):
        self.organisations = []
        self.risks = []

    def add_organisation(self, organisation):
        self.organisations.append(organisation)

    def add_risk(self, risk):
        self.risks.append(risk)

    def get_risks(self):
        return self.risks

    def get_organisations(self):
        return self.organisations


# Test database instance
db = Database()