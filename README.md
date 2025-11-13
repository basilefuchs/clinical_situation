# Clinical situation

Detect clinical situation in medical records using DSPy.

## How it works

```mermaid
flowchart TB

mr("Medical records")
ea("DSPy extract module")
ca("DSPy classification module")
cs("Clinical situation")

mr --> ea & ca
ea & ca --> cs
```

## Structure

```bash
.
├── LICENSE
├── README.md
├── clinical_situation
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── config.yaml
│   ├── modules
│   │   ├── __init__.py
│   │   └── signatures
│   │       └── __init__.py
│   └── utils.py
├── example.txt
├── example2.txt
├── requirements.txt
└── ui.py
```

## Set up

1. Install [Ollama](https://ollama.com/download) and follow instructions.
2. Create a `config.yaml` file in `clinical_situation/` with your settings :

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
python -m clinical_situation example.txt qwen3:8b 
```

> *Note: `example.txt` file is in the repo.*

Or install it as package :

```bash
pip install -e .
clinical_situation --help
clinical_situation example.txt qwen3:8b
```

Output :

```bash
['Diagnostic', 0.95]
{'infarctus cutané': 3, 'hyperlipidémie': 2, 'lésions érythémateuses': 3, 'vésicules': 3, 'céphalée chronique': 2, 'fatigue récurrents': 2}
```

## UI

Run directly :

```bash
streamlit run ui.py
```

And follow the link [http://localhost:8501](http://localhost:8501)
