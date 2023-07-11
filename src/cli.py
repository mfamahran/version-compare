from typing import Optional
import typer

from src import __app_name__, __version__


app = typer.Typer()

@app.command()
def compare(
    version1: str = typer.Option(
        "1.0.0",
        "--version1",
        "-v1",
        prompt="Version 1",
    ),
    version2: str = typer.Option(
        "1.1",
        "--version2",
        "-v2",
        prompt="Version 2",
    ),
) -> None:
    version1_nums = list(map(int, version1.split('.')))
    version2_nums = list(map(int, version2.split('.')))

    # ensure both lists are the same length 
    max_length = max(len(version1_nums), len(version2_nums))
    version1_nums += [0] * (max_length - len(version1_nums))
    version2_nums += [0] * (max_length - len(version2_nums))

    for v1, v2 in zip(version1_nums, version2_nums):
        if v1 > v2:
            typer.echo(1)
            return
        elif v1 < v2:
            typer.echo(-1)
            return
    typer.echo(0)
    return
    

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()
# callback is used to declare CLI params for the main CLI
# can be used to add something like --verbose or --debug
@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return