import os
import typer
from pathlib import Path
import dspy
from clinical_situation import modules, utils

app = typer.Typer(
    help="CLI to run clinical situation analysis on files or directories."
)


@app.command(
    help="Run clinical situation analysis on a .txt file or all .txt files in a directory."
)
def clinical_situation(
    p: str = typer.Argument(".", help="Directory or file to run."),
    m: str = typer.Argument(..., help="Model to run."),
):
    p = Path(p).resolve()

    if p.is_file() and p.suffix == ".txt":
        with open(p, "r", encoding="utf-8") as file:
            text = file.read()
        dspy.configure(lm=utils.lm(m))
        classifier = modules.Classify()
        extractor = modules.Extract("severity")
        print(classifier(text))
        print(extractor(text))

    elif p.is_dir():
        os.chdir(p)
        txt_files = [f for f in p.iterdir() if f.is_file() and f.suffix == ".txt"]
        if not txt_files:
            typer.BadParameter(f"❌ No .txt files found in the directory: {p}")
            raise typer.Exit(code=1)
        for _ in txt_files:
            with open(_, "r", encoding="utf-8") as file:
                text = file.read()
                print(f"\tFile : {_}")
                dspy.configure(lm=utils.lm(m))
                classifier = modules.Classify()
                extractor = modules.Extract("severity")
                print(classifier(text))
                print(extractor(text))

    else:
        typer.BadParameter(f"❌ Not a .txt file: {p}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
