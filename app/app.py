import csv
from flask import Flask
from flask.cli import AppGroup
from flask_pymongo import PyMongo

from .models.insurance_plans import InsurancePlan

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://root:rootpassword@localhost:27020/health_insurance_planner?authSource=admin'
mongo = PyMongo(app)

@app.cli.command('shell')
def myshell():
    """Start an interactive Python shell with the app context."""
    import code
    from flask.globals import _app_ctx_stack

    app = _app_ctx_stack.top.app
    ctx = {'app': app}

    with app.app_context():
        code.interact(local=ctx)

@app.cli.command('initdb')
def initdb():
    """Initialize the database with sample data."""
    with app.app_context():
        # Access the MongoDB collection
        insurance_plan_collection = mongo.db.insurance_plan

        # Insert data into the collection
        with open('sample--rates.csv', 'r') as csvfile:
            # Create a CSV reader object
            csvreader = csv.reader(csvfile)
            header = next(csvreader)
            amounts = header[3:]

            # Iterate through each row in the CSV file
            for row in csvreader:
                if len(row) > 0:
                    member_csv = row[0].split(",")
                    adult_count  = member_csv[0].strip('a')
                    children_count = member_csv[1].strip('c') if len(member_csv) > 1 else '0'
                    age_range = row[1].split("-")
                    tier = row[2].strip('tier-')
                    premiums = row[3:]
                    for index, amount in enumerate(amounts):
                        result = {
                            'adult': int(adult_count),
                            'children': int(children_count),
                            'age_range': {
                                'max': int(age_range[0]),
                                'min': int(age_range[1])
                            },
                            'tier': tier,
                            'premium': float(premiums[index]),
                            'amount': float(amount)
                        }
                        insurance_plan = InsurancePlan(**result)
                        unique_fields = {
                            'adult': insurance_plan.adult, 
                            'children': insurance_plan.children, 
                            'tier': insurance_plan.tier, 
                            'amount': insurance_plan.amount,
                            'age_range.max': int(age_range[0]),
                            'age_range.min': int(age_range[1])
                        }
                        exisiting_insurance_plan = insurance_plan_collection.find_one(unique_fields)
                        if exisiting_insurance_plan:
                            print("Duplicate Entry")
                        else :
                            inserted_insurance_plan = insurance_plan_collection.insert_one(insurance_plan.model_dump())
                            print(inserted_insurance_plan)
        print("DB Populated Successfully")