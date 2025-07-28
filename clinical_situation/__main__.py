import yaml
import dspy
from config import load_config, lm
from modules import ExtractPrimaryConditions


# config = load_config("clinical_situation/config/config.yaml")

# lm = dspy.LM(config["llm"]["model"], api_base=config["llm"]["port"], api_key="")
dspy.configure(lm=lm())

text = (
    """
    Patient hospitalisé pour prise en charge d'une appendicectomie 
    devant une douleur abdominale et un météorisme.Notion de chute à domicile.
    Conclusion : Chute de sa hauteur dans un contexte démence non étiquettée, 
    compliquée d'une station allongée responsable d'une appendicite. 
    Sortie en SSR.
    """
)

modulePC = dspy.Predict(ExtractPrimaryConditions)
responsePC = modulePC(text=text)

print(responsePC.headings)
