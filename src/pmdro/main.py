import click


@click.group()
def cli():
    pass


@cli.command("start")
@click.option(
    "-f",
    "--focus",
    "focus_duration",
    type=click.INT,
    help="Focus timer duration in minutes",
)
@click.option(
    "-b",
    "--break",
    "break_duration",
    type=click.INT,
    help="Break timer duration in minutes",
)
def start(focus_duration, break_duration):
    click.echo("You ran 'pmdro start'.")
    if focus_duration is not None:
        click.echo(f"Setting focus timer for {focus_duration} minutes.")

    if break_duration is not None:
        click.echo(f"Setting break timer for {break_duration} minutes.")
