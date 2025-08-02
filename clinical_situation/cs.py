import dspy
from .config import lm, prompt
from .modules import Extract, ClinicalSituation


def cs(text, model):
    dspy.configure(lm=lm(model))

    extract_motif = Extract("motif")
    motif = ", ".join(extract_motif(text))

    extract_diag = Extract("diag")
    diag = ", ".join(extract_diag(text))

    extract_soins = Extract("soins")
    soins = ", ".join(extract_soins(text))

    situation_clinique = ClinicalSituation()

    ehanced_text = prompt(motif, diag, soins)

    print(ehanced_text)
    print(situation_clinique(ehanced_text))
