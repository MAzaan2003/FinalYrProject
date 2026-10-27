from dataclasses import dataclass


@dataclass
class Organisation:
    name: str
    industry: str
    size: str


@dataclass
class Risk:
    name: str
    category: str
    likelihood: int
    impact: int

    def score(self):
        return self.likelihood * self.impact
    