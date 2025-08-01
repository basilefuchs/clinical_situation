import dspy


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
