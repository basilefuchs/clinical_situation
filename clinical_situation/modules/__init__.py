import dspy


class ExtractPrimaryConditions(dspy.Signature):
    """Extract structured primary conditions from text."""

    text: str = dspy.InputField()
    # title: str = dspy.OutputField()
    headings: list[str] = dspy.OutputField()
    entities: list[dict[str, str]] = dspy.OutputField(
        desc="a list of reasons for admission"
    )


class ExtractOutcomes(dspy.Signature):
    """Extract structured outcomes from text."""

    text: str = dspy.InputField()
    # title: str = dspy.OutputField()
    headings: list[str] = dspy.OutputField()
    entities: list[dict[str, str]] = dspy.OutputField(
        desc="a list of outcomes of admission"
    )
