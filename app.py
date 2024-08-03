from flask import Flask, render_template, request, redirect, url_for
from model import db, User, Income, Expense, Category, Scholarship
from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budgeting.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///merodata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    categories = Category.query.all()
    return render_template('index.html', categories=categories)

@app.route('/add_income', methods=['POST'])
def add_income():
    try:
        amount = float(request.form['amount'])
        description = request.form.get('description', '')
        user_id = 1  # Replace with dynamic user ID if authentication is implemented

        income = Income(amount=amount, description=description, user_id=user_id) # type: ignore
        db.session.add(income)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error adding income: {e}")
        return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    try:
        amount = float(request.form['amount'])
        description = request.form.get('description', '')
        category_id = int(request.form['category_id'])
        user_id = 1  # Replace with dynamic user ID if authentication is implemented

        expense = Expense(amount=amount, description=description, category_id=category_id, user_id=user_id) # type: ignore
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error adding expense: {e}")
        return redirect(url_for('index'))

@app.route('/search_scholarships', methods=['GET'])
def search_scholarships():
    query = request.args.get('query', '')
    scholarships = Scholarship.query.filter(Scholarship.name.ilike(f'%{query}%')).all()
    return render_template('scholarships.html', scholarships=scholarships)

@app.route('/career')
def career():
    return render_template('career.html')


@app.route('/job_listings')
def job_listings():
    job_listings = [
        {"title": "Software Engineer", "company": "Tech Corp", "location": "San Francisco", "description": "Develop and maintain software."},
        {"title": "Data Analyst", "company": "Data Inc", "location": "New York", "description": "Analyze and interpret complex data."}
    ]
    return render_template('job_listings.html', job_listings=job_listings)

@app.route('/user_profile')
def user_profile():
    user = User.query.get(1)  # Example user ID, replace with dynamic user ID if authentication is implemented
    return render_template('user_profile.html', user=user)

@app.route('/financial')
def financial():
    return render_template('financial.html')

# Remove or correct this route if needed
# @app.route('/career')
# def career():
#     return render_template('career.html')

if __name__ == '__main__':
    app.run(debug=True)


from app import app, db

@app.cli.command("create-tables")
def create_tables():
    with app.app_context():
        db.create_all()
        print("All tables created.")
        
from app import app, db
from sqlalchemy import text

@app.cli.command("fix-schema")
def fix_schema():
    with app.app_context():
        with db.engine.connect() as conn:
            try:
                # Example SQL command to add a new column
                conn.execute(text("ALTER TABLE user ADD COLUMN password TEXT;"))
                print("Schema fixed.")
            except Exception as e:
                print(f"Error fixing schema: {e}")
                
from app import app, db
from sqlalchemy import inspect

@app.cli.command("check-tables")
def check_tables():
    with app.app_context():
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print("Tables in the database:", tables)