import dspy
from .config import lm, prompt
from .modules import Extract, ClinicalSituation


def cs(text, model):
    dspy.configure(lm=lm(model))

    def extract_list(category):
        """Extrait et formate une liste d’éléments pour une catégorie donnée."""
        extractor = Extract(category)
        items = extractor(text)
        return "\n".join(f"- {x}" for x in items)

    motif = extract_list("motif")
    atcd = extract_list("atcd")
    symptomes = extract_list("symptomes")
    syndromes = extract_list("syndromes")
    diagnostics = extract_list("diagnostics")
    diagnosticprincipal = extract_list("diagnosticprincipal")
    soins = extract_list("soins")

    situation_clinique = ClinicalSituation()

    ehanced_text = prompt(
        motif, atcd, symptomes, syndromes, diagnostics, diagnosticprincipal, soins
    )

    print(ehanced_text)
    print(situation_clinique(ehanced_text))
