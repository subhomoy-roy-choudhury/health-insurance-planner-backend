import click
from flask.cli import AppGroup
from flask import Blueprint

shell_bp = Blueprint('shell', __name__, cli_group=None)


@shell_bp.cli.command('shell')
# @click.argument('sample')
def shell():
    """Start an interactive Python shell with the app context."""
    import code
    from flask.globals import _app_ctx_stack

    app = _app_ctx_stack.top.app
    ctx = {'app': app}

    with app.app_context():
        code.interact(local=ctx)