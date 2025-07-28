import dspy


class ExtractPrimaryConditions(dspy.Signature):
    """Extrait le motif d'hospitalisation à partir d'un compte rendu médical."""

    text: str = dspy.InputField(desc="un compte rendu médical.")
    entities: list[str] = dspy.OutputField(desc="le motif d'hospitalisation.")


class ExtractDiagnosis(dspy.Signature):
    """Extrait la pathologie principale d'un compte rendu médical."""

    text: str = dspy.InputField(desc="un compte rendu médical.")
    entities: list[str] = dspy.OutputField(desc="la pathologie principale.")

class ExtractCares(dspy.Signature):
    """Extrait tous les soins d'un compte rendu médicale."""

    text: str = dspy.InputField(desc="un compte rendu médical.")
    entities: list[str] = dspy.OutputField(desc="une liste de tous les soins.")


class ClinicalSituation(dspy.Module):
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
