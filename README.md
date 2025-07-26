# clinical_situation
Detect clinical situation in medical records using DSPy

# pipeline

```mermaid
flowchart TB

mr("Medical records")
ea("DSPy extract agent")
ca("DSPY classification agent")
cs("Clinical situation")

mr --> ea & ca
ea --"Leading cause of hospitalisation"--> ca
ca --> cs
```
