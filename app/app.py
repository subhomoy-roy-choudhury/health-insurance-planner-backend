from flask import Flask

from app.commands.shell import shell_bp
from app.commands.initdb import initdb_bp
from app.routes.plan_routes import plan_bp

app = Flask(__name__)

# API Routes
app.register_blueprint(plan_bp, url_prefix="/api/plan")

# Commands
app.register_blueprint(initdb_bp, cli_group=None)
app.register_blueprint(shell_bp, cli_group=None)
