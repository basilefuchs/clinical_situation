import re
import yaml
import dspy
from .modules import Extract, ClinicalSituation


def load_config(yaml_file: str) -> dict:
    """"""
    try:
        with open(yaml_file, "r") as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier {yaml_file} est introuvable.")
    except yaml.YAMLError as e:
        raise ValueError(f"Erreur lors de la lecture du fichier YAML : {e}")
    except Exception as e:
        raise ValueError(f"Erreur lors de la validation de la configuration : {e}")


def lm(model):
    """"""
    config = load_config("clinical_situation/config.yaml")
    lm = dspy.LM(
        config["llm"]["service"] + model,
        api_base=config["llm"]["port"],
        api_key=config["llm"]["api_key"],
    )
    return lm

def extract_list(text):
    categories = [
        "motif", "atcd", "symptomes", 
        "syndromes", "diagnostics", 
        "diagnosticprincipal", "soins"
    ]

    results = set()
    for cat in categories:
        extractor = Extract(cat)
        items = extractor(text)
        results.update(items)

    return list(results)

def highlight_text(text, words):
    couleur = "#ffff99"
    words = sorted(words, key=len, reverse=True)
    for word in words:
        pattern = re.compile(rf"\b({re.escape(word)})\b", re.IGNORECASE)
        text = pattern.sub(rf"<span style='background-color:{couleur}'><b>\1</b></span>", text)

    return text

def assess_situation(text):
    classifier = ClinicalSituation()
    result = classifier(text)

    return result