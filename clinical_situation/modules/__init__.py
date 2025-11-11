import dspy
from .signatures import ExtractDiagnosisSeverity, Classify


class Extract(dspy.Module):
    MODULES_MAP = {
        "severity": ExtractDiagnosisSeverity,
    }

    def __init__(self, module):
        if module not in self.MODULES_MAP:
            raise ValueError(f"Le module '{module}' n'existe pas.")
        self.module = dspy.ChainOfThought(self.MODULES_MAP[module])

    def forward(self, text):
        return self.module(text=text).entities


class ClinicalSituation(dspy.Module):
    def __init__(self):
        self.module = dspy.ChainOfThought(Classify)

    def forward(self, text):
        response = self.module(text=text)
        return [response.classification, response.confidence]
