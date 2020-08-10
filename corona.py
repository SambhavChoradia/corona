from corona import Corona
import typer

corona = Corona()
app = typer.Typer()

@app.command()
def summary():
    typer.echo(corona.get_summary())

typer.echo(typer.style(f"Corona tracker  ", fg="green"))
if __name__ == "__main__":
    app()
