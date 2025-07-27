import yaml
import dspy
from config import load_config
from modules import ExtractPrimaryConditions, ExtractOutcomes

import yaml

config = load_config("clinical_situation/config/config.yaml")

lm = dspy.LM(config["llm"]["model"], api_base=config["llm"]["port"], api_key="")
dspy.configure(lm=lm)

text = (
    "Patient hospitalisé pour prise en charge d'une appendicectomie devant une douleur abdominale et un météorisme."
    "Patient hospitalisé pour bilan de chute."
    "Conclusion : Chute de sa hauteur dans un contexte démence non étiquettée, compliquée d'une station allngée responsable d'une appendicite. Sortie en SSR."
)

modulePC = dspy.Predict(ExtractPrimaryConditions)
responsePC = modulePC(text=text)

print(responsePC.headings)

moduleO = dspy.Predict(ExtractOutcomes)
responseO = moduleO(text=text)

print(responseO.headings)
