import yaml
import dspy
from config import lm
from modules import ExtractPrimaryConditions, ExtractCares, ClinicalSituation

dspy.configure(lm=lm())

text = """
Compte Rendu d'Hospitalisation

Identité du patient :

Nom : Jeanne
Prénom : Dupont
Âge : 32 ans
Sexe : Féminin
Mode d'entrée : Surveillance à haut risque

Durée de l'hospitalisation : 3 jours

Service : Obstétrique

Motif d'admission :
Jeanne Dupont, une femme de 32 ans, a été admise à la maternité en raison de douleurs abdominales persistantes et d'une cervix prématurément dilatée. En raison de son état critique, elle nécessitait une surveillance à haut risque pour éviter un accouchement prématuré.

Antécédents médicaux :
Jeanne est enceinte de jumeaux et présente déjà un passé médical complexe marqué par plusieurs grossesses à haut risque précédentes. Aucun autre antécédent médical connu.

Examen clinique à l'admission :
À son arrivée, Jeanne présentait une cervix dilatée de 3 cm et des contractions abdominales fréquentes. L'échographie a révélé que les deux bébés étaient en bonne position et avaient un poids acceptable.

Résultats biologiques :

FHC : 0.5 ng/mL (valeur normale < 0.1 ng/mL)
Glycémie : 90 mg/dL (valeur normale < 140 mg/dL)
Hémoglobine A1c : 5.2% (valeur normale < 5.7%)
Créatinine : 0.8 mg/dL (valeur normale < 1.3 mg/dL)
Cholestérol total : 180 mg/dL (valeur normale < 200 mg/dL)
LDL : 110 mg/dL (valeur normale < 100 mg/dL)
HDL : 60 mg/dL (valeur normale > 40 mg/dL)
Triglycérides : 150 mg/dL (valeur normale < 150 mg/dL)
Pathologies associées fictives :
Jeanne présente également une insuffisance rénale chronique légère et un hypercholestérolémie, mais il n'y a pas de complications majeures à ce jour.

Traitement et évolution :
Jeanne a reçu un traitement pour arrêter les contractions abdominales, ainsi qu'un suivi constant de son cervix et des bébés. Elle a également été administrée des hormones progestéroneiques pour retarder l'accouchement prématuré. Au fil des jours, sa cervix s'est rétrécie progressivement et les contractions abdominales ont diminué.

Conclusion et recommandations :
Après une hospitalisation de 3 jours, Jeanne a pu quitter l'hôpital avec un diagnostic final d'un faux travail avant 37 semaines entières de gestation. Pour assurer un suivi optimal des jumeaux, il est recommandé de surveiller régulièrement la croissance intra-utérine et la fonction cardiaque de Jeanne, ainsi que de suivre de près l'évolution de son insuffisance rénale chronique légère. Des visites de suivi régulières sont également nécessaires pour s'assurer qu'il n'y a pas de récidive du faux travail avant l'accouchement prévu à terme.
"""

extract_motif = ClinicalSituation("motif")
extract_soins = ClinicalSituation("soins")

print(extract_motif(text))
print(extract_soins(text))
