import click


@click.group()
def cli():
    pass


@cli.command("start")
def start():
    click.echo("Starting timer")
