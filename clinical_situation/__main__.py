import dspy
from config import lm, prompt
from modules import Extract, ClinicalSituation

dspy.configure(lm=lm())

text = """
Compte Rendu d'Hospitalisation

Identité du patient :

Nom : Jane
Prénom : Doe
Âge : 42 ans
Sexe : Féminin
Mode d'entrée : Urgences

Durée de l'hospitalisation : 1 jour

Service : Dermatologie

Motif d'admission :
Jane Doe, une femme de 42 ans, a été admise aux urgences en raison de douleurs 
persistantes et intenses localisées sur la face et les membres. L'examen clinique 
a révélé des lésions érythémateuses et des vésicules sur la peau. Les symptômes 
étaient associés à des sensations de brûlures et de douloureux picotements, 
ce qui a conduit à supposer un infarctus cutané.

Antécédents médicaux :
Jane a un passé médical sain sans antécédent particulier notifiable. 
Cependant, elle a signalé des épisodes de fatigue récurrents et une céphalée chronique 
qui l'ont amenée à consulter régulièrement un médecin généraliste.

Examen clinique à l'admission :
L'examen clinique a montré des lésions érythémateuses et vésiculeuses localisées 
sur la peau, avec des sensations de brûlures et de picotements persistants. 
L'échantillon prélevé a confirmé le diagnostic d'infarctus cutané.

Résultats biologiques :
Les résultats des tests sanguins étaient normaux. 
Cependant, les électrophorèses du sang ont montré une légère hyperlipidémie.

Traitement et évolution :
Jane a reçu un traitement local pour soulager la douleur et accélérer 
la guérison des lésions cutanées. Les médicaments prescrits étaient des 
anti-inflammatoires topiques, des antihistaminiques et des analgésiques. 
Elle a également été recommandée une régime alimentaire équilibré pour contrôler la hyperlipidémie. 
Au fil des heures, les symptômes ont progressivement disparu, 
et elle a pu quitter l'hôpital le jour suivant l'admission.

Conclusion et recommandations :
Après une hospitalisation de 1 jour, Jane a pu quitter l'hôpital avec un diagnostic final 
d'infarctus cutané, résolu par des traitements locaux et une régime alimentaire équilibré. 
Pour assurer un suivi optimal, il est recommandé de surveiller régulièrement la peau pour 
détecter de possibles récidives, de contrôler la hyperlipidémie et d'assurer un suivi régulier 
d'un médecin généraliste. Les médicaments prescrits doivent également être administrés comme indiqué 
pour garantir l'efficacité du traitement.
"""

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
