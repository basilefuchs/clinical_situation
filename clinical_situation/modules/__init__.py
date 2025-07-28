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
    """
    Classer la situation clinique d'une hopitalisation à partir d'un text enrichi.
    Classification possible :
      - Diagnostic : La situation est celle d’un patient hospitalisé en raison d’une symptomatologie,
      pour un diagnostic étiologique. Le mot symptomatologie inclut les signes cliniques et les résultats
      anormaux d’examens complémentaires.
      - Traitement : La situation est celle d’un patient atteint d’une affection connue,
      diagnostiquée avant l’admission, hospitalisé pour le traitement de celle-ci.
      - Suveillance : La situation est celle d’un patient atteint d'une affection connue, antérieurement diagnostiquée,
      éventuellement traitée (antérieurement traitée ou en cours de traitement), hospitalisé pour la surveillance de celle-ci.
    """

    text: str = dspy.InputField(desc="une synthèse de la situation.")
    classification: Literal["Diagnostic", "Traitement", "Surveillance"] = (
        dspy.OutputField()
    )
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
