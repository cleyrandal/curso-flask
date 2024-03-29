from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from delivery.ext.auth.models import User
from delivery.ext.db import db
from flask import flash
from markupsafe import Markup

# def format_user(self,request, user, *args):
#     return user.email.split("@")[0]

# TODO: descrever todos os models


class UserAdmin(ModelView):
    """Interface admin de user"""

    column_formatters = {
            "email": lambda s, r, u, *a: Markup(f'<b>{u.email.split("@")[0]}</b>')
    }

    column_list = ["admin", "email"]

    column_searchable_list = ["email"]

    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email,
            "domínio",
            options=(("gmail", "Gmail"), ("uol", "Uol"))
        )
    ]

    can_edit = False
    can_create = True
    can_delete = True

    @action(
        'toggle_admin',
        'toggle_admin_status',
        'Are you sure?'
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f" {len(users)} usuários alterados com sucesso!", "success")

    @action(
        'send_email',
        'Send email to all users',
        'Are you sure?'
    )
    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # 1) redirect para um form para escrever a mensagem do email
        # 2) enviar o email
        flash(f" {len(users)} emails enviados.", "success")
