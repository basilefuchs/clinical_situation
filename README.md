# clinical_situation
Detect clinical situation in medical records using DSPy

# pipeline

```mermaid
flowchart TB

mr("Medical records")
ea("DSPy extract module")
ca("DSPY classification module")
cs("Clinical situation")

mr --> ea & ca
ea --"Primary conditions for admission"--> ca
ca --> cs
```
