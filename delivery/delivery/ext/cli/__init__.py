import click
from delivery.ext.db import db
from delivery.ext.site import models # noqa


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db."""
        db.create_all()

    @app.cli.command()
    def listar_pedidos():
        # TODO: usar tabulate
        click.echo("lista de pedidos")

    @app.cli.command()
    def listar_usuarios():
        click.echo("lista de usuarios")
