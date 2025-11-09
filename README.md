# Clinical situation
Detect clinical situation in medical records using DSPy.

## How it works

```mermaid
flowchart TB

mr("Medical records")
ea("DSPy extract module")
ca("DSPy classification module")
cs("Clinical situation")

mr --> ea
ea --"Primary conditions for admission"--> ca
ea --"Medical history"--> ca
ea --"Symptoms"--> ca
ea --"Syndromes"--> ca
ea --"Diagnosis"--> ca
ea --"Care provided"--> ca
ca --> cs
```

## Structure

```
.
├── clinical_situation
│   ├── cli.py
│   ├── config
│   │   ├── config.yaml
│   │   └── __init__.py
│   ├── cs.py
│   ├── __init__.py
│   ├── __main__.py
│   └── modules
│       ├── __init__.py
│       └── signatures
│           └── __init__.py
├── example.txt
├── LICENSE
├── pyproject.toml
└── README.md
```

## Set up

1. Install [Ollama](https://ollama.com/download) and follow instructions.
2. Create a `config.yaml` file in `clinical_situation/config/` with your settings :

```yaml
llm:
  service: "ollama_chat/"
  port: "http://localhost:11434"
  api_key: ""
```

## CLI

Run it directly :

```bash
python -m clinical_situation --help 
```

Or install it as package :

```bash
pip install -e .
clinical_situation --help
clinical_situation . mistral
```

Output :warning: **WORK IN PROGRESS** :warning: : 

```
### Motif d'hospitalisation:
- infarctus cutané

### Antécédant:
- épisodes de fatigue récurrents
- céphalée chronique

### Symptomes:
- douleurs persistantes et intenses localisées sur la face et les membres
- lésions érythémateuses
- vésicules sur la peau
- sensations de brûlures
- douloureux picotements
- fatigue récurrents
- céphalée chronique
  
### Syndromes:
- infarctus cutané
  
### Patholgies:
- infarctus cutané
- hyperlipidémie

### Pathologie principale:
- infarctus cutané

### Prise en charge:
- anti-inflammatoires topiques
- antihistaminiques
- analgésiques
- régime alimentaire équilibré
  
['Traitement', 0.95]
```