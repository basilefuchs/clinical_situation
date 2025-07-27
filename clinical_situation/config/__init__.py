import yaml

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
        raise ValueError(
            f"Erreur lors de la validation de la configuration : {e}")