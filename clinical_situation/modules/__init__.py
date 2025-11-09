import dspy
from .signatures import (
    ExtractPrimaryConditions,
    ExtractMedicalHistory,
    ExtractSymptoms,
    ExtractSyndromes,
    ExtractDiagnosis,
    ExtractMainDiagnosis,
    ExtractCares,
    Classify,
)


class Extract(dspy.Module):
    def __init__(self, module):
        if module == "motif":
            self.module = dspy.ChainOfThought(ExtractPrimaryConditions)
        elif module == "atcd":
            self.module = dspy.ChainOfThought(ExtractMedicalHistory)
        elif module == "symptomes":
            self.module = dspy.ChainOfThought(ExtractSymptoms)
        elif module == "syndromes":
            self.module = dspy.ChainOfThought(ExtractSyndromes)
        elif module == "diagnostics":
            self.module = dspy.ChainOfThought(ExtractDiagnosis)
        elif module == "diagnosticprincipal":
            self.module = dspy.ChainOfThought(ExtractMainDiagnosis)
        elif module == "soins":
            self.module = dspy.ChainOfThought(ExtractCares)
        else:
            raise Exception("Ce module n'existe pas.")

    def forward(self, text):
        response = self.module(text=text)
        return response.entities


class ClinicalSituation(dspy.Module):
    def __init__(self):
        self.module = dspy.ChainOfThought(Classify)

    def forward(self, text):
        response = self.module(text=text)
        return [response.classification, response.confidence]
