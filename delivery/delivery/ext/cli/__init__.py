import click
from delivery.ext.db import db
from delivery.ext.auth.models import User
from delivery.ext.db import models # noqa


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db."""
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """adiciona novo usuario"""
        user = User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f"Usuário {email} criado com sucesso!")

    @app.cli.command()
    def listar_pedidos():
        # TODO: usar tabulate
        click.echo("lista de pedidos")

    @app.cli.command()
    def listar_usuarios():
        users = User.query.all()
        click.echo(f"lista de usuarios {users}")
