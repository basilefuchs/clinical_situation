import dspy
from typing import Literal
from signatures import ExtractPrimaryConditions, ExtractDiagnosis, ExtractCares


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


class Classify(dspy.Signature):
    """
    ### Tâche :
    Classer la situation clinique décrite dans un texte médical enrichi selon l’un des trois types d’hospitalisation suivants.

    ### Objectif :
    Analyser le texte fourni et attribuer la catégorie clinique la plus appropriée à la situation d’hospitalisation.

    ### Catégories de classification possibles :

    #### Diagnostic :
    Le patient est hospitalisé en raison d’une symptomatologie inexpliquée nécessitant une investigation étiologique.
    La symptomatologie peut inclure des signes cliniques, des plaintes du patient ou des anomalies d’examens complémentaires, sans diagnostic connu préalable.

    ####Traitement :
    Le patient est hospitalisé pour recevoir un traitement ciblé d’une affection déjà connue et diagnostiquée avant l’admission.
    L’objectif principal est la prise en charge thérapeutique de cette pathologie.

    #### Surveillance :
    Le patient présente une affection connue (déjà diagnostiquée et éventuellement traitée), et l’hospitalisation a pour but le suivi, la surveillance clinique, biologique ou radiologique, sans intervention thérapeutique immédiate attendue.

    ### Consignes :
    Lire attentivement le texte.
    Identifier les éléments pertinents : antécédents, symptômes, diagnostics, traitements, objectifs de l’hospitalisation.
    Choisir une seule catégorie parmi les trois proposées.
    Ne pas justifier la classification.
    """

    text: str = dspy.InputField(desc="une synthèse de la situation.")
    classification: Literal["Diagnostic", "Traitement", "Surveillance"] = (
        dspy.OutputField()
    )
    confidence: float = dspy.OutputField()


class ClinicalSituation(dspy.Module):
    def __init__(self):
        self.module = dspy.ChainOfThought(Classify)

    def forward(self, text):
        response = self.module(text=text)
        return [response.classification, response.confidence]
