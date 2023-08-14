from flask import Flask
from flask_pymongo import PyMongo

from app.commands.shell import shell_bp
from app.commands.initdb import initdb_bp
from app.routes.plan_routes import plan_bp

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://root:rootpassword@localhost:27020/health_insurance_planner?authSource=admin'
mongo = PyMongo(app)

# API Routes
app.register_blueprint(plan_bp, url_prefix='/api/plan')

# Commands
app.register_blueprint(initdb_bp, cli_group=None)
app.register_blueprint(shell_bp, cli_group=None)