import click


@click.group()
def cli():
    pass


@cli.command("start")
@click.option("-f", "--focus", type=click.INT)
def start(focus):
    click.echo(f"Setting timer for {focus} minutes.")
