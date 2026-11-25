"""CLI using Typer."""

import typer

app = typer.Typer(
    name="CLI using Typer"
)

@app.command()
def say_hi(name):
    """Say hello to the user."""
    typer.echo(f"Hello: {name}")

@app.command()
def goodbye():
    """Say goodbye to the user."""
    typer.echo("Goodbye!")

@app.command()
def greet(name):
    """Greet the user."""
    typer.echo(f"Greetings {name}...")

@app.command()
def welcome(
    name,
    greeting: str = typer.Option(default="Hello", help="Set custom greeting message."),
    enthusiastic: bool = typer.Option(default=False, help="Enable enthusiastic greeting.")
    ):
    """Welcome the user."""
    message = f"{greeting} {name}."
    if enthusiastic:
        message += "!!"
    typer.echo(message)

if __name__ == "__main__":
    app()
