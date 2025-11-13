import dspy
from typing import Literal


class ExtractDiagnosisSeverity(dspy.Signature):
    """
    Analyser attentivement le texte médical fourni (compte rendu, observation clinique, rapport opératoire, etc.)
    et identifier toutes les pathologies, maladies, antécédents, anomalies, symptômes ou diagnostics mentionnés, qu'ils soient explicites ou implicites.

    ⚠️ Contraintes importantes :
    - Extraire **uniquement les termes exacts tels qu'ils apparaissent dans le texte** (même orthographe, même formulation).
    - Ne pas reformuler, regrouper, ni généraliser les termes.
    - Si plusieurs formulations proches apparaissent (ex : "infection pulmonaire" et "pneumonie"), les garder séparément.
    - Ne pas inventer ni inférer de pathologies absentes du texte.
    - Ne pas inclure d’informations non médicales (âge, nom, contexte, etc.).

    Pour chaque pathologie, anomalie ou symptôme identifié, évaluer le **niveau de charge de soins** sur une échelle de 1 à 4,
    selon l’intensité et la complexité des soins nécessaires pour la prise en charge :

        1 - Peu de soins : suivi simple, consultation ambulatoire, traitements légers ou ponctuels
        2 - Soins modérés : traitements médicamenteux réguliers, suivi médical actif, interventions limitées, surveillance rapprochée
        3 - Soins élevés : hospitalisation nécessaire, interventions multiples ou traitements complexes
        4 - Soins majeurs : soins intensifs, réanimation, interventions urgentes ou hospitalisation prolongée

    Sortie attendue :
    - Un dictionnaire Python clair associant chaque **terme médical exact extrait du texte** à son niveau de charge de soins (1 à 4).
    - Exemple : {"pneumonie": 3, "hypertension artérielle": 2}

    L'objectif est de permettre la coloration du texte original à partir des termes extraits : 
    la précision des chaînes de caractères est donc essentielle.
    """

    text: str = dspy.InputField(
        desc="Un compte rendu médical ou observation clinique détaillée."
    )
    entities: dict[str, int] = dspy.OutputField(
        desc=(
            "Dictionnaire associant chaque pathologie, maladie, antécédant, anomalie, symptôme ou diagnostic EXACTEMENT tel qu'il apparaît dans le texte "
            "à un niveau de charge de soins (1 à 4). "
            "Exemple : {'pneumonie': 3, 'hypertension artérielle': 1}"
        )
    )


class ClinicalSituation(dspy.Signature):
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
