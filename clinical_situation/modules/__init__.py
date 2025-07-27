import dspy


class ExtractPrimaryConditions(dspy.Signature):
    """Extract structured primary conditions from text."""

    text: str = dspy.InputField()
    # title: str = dspy.OutputField()
    headings: list[str] = dspy.OutputField()
    entities: list[dict[str, str]] = dspy.OutputField(
        desc="a list of primary conditions of admission"
    )
