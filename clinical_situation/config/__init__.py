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


def lm():
    """"""
    config = load_config("clinical_situation/config/config.yaml")
    lm = dspy.LM(config["llm"]["model"], api_base=config["llm"]["port"], api_key="")
    return lm


def prompt(motif, diag, soins) -> str:
    text = f"""
  ### Motif d'hospitalisation:
  {motif}

  ### Pathologie principale:
  {diag}

  ### Prise en charge:
  {soins}
  """
    return text
