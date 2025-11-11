import dspy
from typing import Literal


class ExtractDiagnosisSeverity(dspy.Signature):
    """
    Analyser attentivement le texte médical fourni (compte rendu, observation, compte rendu opératoire, etc.) et identifier toutes les pathologies, anomalies, symptômes ou diagnostics mentionnés, explicites ou implicites.
    Pour chaque pathologie ou anomalie identifiée, évaluer le niveau de charge de soins sur une échelle de 1 à 4, basée sur l'intensité et la complexité des soins nécessaires pour la prise en charge :
        1 - Peu de soins : suivi simple, consultation ambulatoire, traitements légers ou ponctuels
        2 - Soins modérés : traitements médicamenteux réguliers, suivi médical actif, interventions limitées
        3 - Soins élevés : hospitalisation possible, interventions multiples ou traitements complexes, surveillance rapprochée
        4 - Soins majeurs : soins intensifs, réanimation, interventions urgentes ou hospitalisation prolongée
    Fournir un dictionnaire clair associant chaque pathologie ou anomalie à son niveau de charge de soins.
    Ne pas inclure d’informations non médicales, spéculations ou interprétations non supportées par le texte.
    """

    text: str = dspy.InputField(
        desc="Un compte rendu médical ou observation clinique détaillée."
    )
    entities: dict[str, int] = dspy.OutputField(
        desc=(
            "Dictionnaire associant chaque pathologie, anomalie ou symptôme identifié à un niveau de charge de soins de 1 à 4, "
            "basé uniquement sur le texte fourni et la complexité/intensité des soins nécessaires. "
            "Exemple de sortie : {'pneumonie': 3, 'hypertension': 2}"
        )
    )


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

    text: str = dspy.InputField(desc="compte rendu médicale.")
    classification: Literal["Diagnostic", "Traitement", "Surveillance"] = (
        dspy.OutputField()
    )
    confidence: float = dspy.OutputField()
