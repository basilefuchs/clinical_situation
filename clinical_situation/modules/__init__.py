import dspy
from typing import Literal


class ExtractPrimaryConditions(dspy.Signature):
    """Extraire le motif d'hospitalisation à partir d'un compte rendu médical."""

    text: str = dspy.InputField(desc="un compte rendu médical.")
    entities: list[str] = dspy.OutputField(desc="le motif d'hospitalisation.")


class ExtractDiagnosis(dspy.Signature):
    """Extraire la pathologie principale d'un compte rendu médical."""

    text: str = dspy.InputField(desc="un compte rendu médical.")
    entities: list[str] = dspy.OutputField(desc="la pathologie principale.")

class ExtractCares(dspy.Signature):
    """Extraire tous les soins d'un compte rendu médicale."""

    text: str = dspy.InputField(desc="un compte rendu médical.")
    entities: list[str] = dspy.OutputField(desc="une liste de tous les soins.")

class Classify(dspy.Signature):
    """Classifier la situation clinique d'une hopitalisation à partir d'un compte rendu médical."""

    text: str = dspy.InputField(desc="un compte rendu médical.")
    classification: Literal["Diagnostic", "Traitement", "Surveillance"] = dspy.OutputField()
    confidence: float = dspy.OutputField()

class Extract(dspy.Module):
    def __init__(self, module):
        if module == "motif":
            self.module = dspy.ChainOfThought(ExtractPrimaryConditions)
        elif module == "diag":
            self.module = dspy.ChainOfThought(ExtractDiagnosis)
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