import re
import yaml
import dspy


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
        # model_type=config["llm"]["model_type"], # add for vllm
    )
    return lm


def highlight_text_by_severity(text, diagnosis_severity):
    """
    Highlights words by severity and shows the severity number in brackets.
    """
    severity_colors = {
        1: "#4af6c3",
        2: "#0068ff",
        3: "#fb8b1e",
        4: "#ff433d",
    }

    if not diagnosis_severity:
        return text

    sorted_words = sorted(diagnosis_severity.keys(), key=len, reverse=True)

    def replacer(match):
        word = match.group(0)
        key = next((k for k in diagnosis_severity if k.lower() == word.lower()), None)
        severity = diagnosis_severity.get(key)
        color = severity_colors.get(severity, "#ffff99")
        severity_label = f"[{severity}]" if severity else "[?]"
        return f"<span style='background-color:{color}; color:white; display: inline-block; padding: 2px 6px; border-radius:4px; line-height:1.2;'><b>{word}</b> {severity_label}</span>"

    pattern = re.compile(
        r"\b(" + "|".join(re.escape(w) for w in sorted_words) + r")\b",
        re.IGNORECASE | re.UNICODE,
    )

    return pattern.sub(replacer, text)
