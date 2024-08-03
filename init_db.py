from app import app, db
from model import Category, Income, Expense, User, Scholarship
from datetime import date

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database initialized.")

        # Add initial categories if they don't already exist
        categories = [
            'Housing Costs',
            'Food and Groceries',
            'Transportation',
            'Healthcare',
            'Insurance',
            'Savings and Investments',
            'Debt Repayment',
            'Entertainment and Leisure',
            'Education',
            'Clothing and Personal Care',
            'Communication',
            'Gifts and Donations',
            'Miscellaneous'
        ]

        existing_categories = {cat.name for cat in Category.query.all()}

        for category_name in categories:
            if category_name not in existing_categories:
                category = Category(name=category_name, user_id=1)  # type: ignore # Adjust user_id as needed
                db.session.add(category)

        db.session.commit()
        print("Categories seeded successfully.")

        # Optional: Add initial users or other necessary records
        if not User.query.first():
            sample_user = User(username='default_user') # type: ignore
            db.session.add(sample_user)
            db.session.commit()
            print("Sample user added.")

        # Optional: Add sample income and expenses if needed
        if not Income.query.first():
            sample_income = Income(amount=1000.00, description='Sample Income', user_id=1) # type: ignore
            db.session.add(sample_income)
            db.session.commit()
            print("Sample income added.")

        if not Expense.query.first():
            sample_expense = Expense(amount=200.00, description='Sample Expense', category_id=1, user_id=1) # type: ignore
            db.session.add(sample_expense)
            db.session.commit()
            print("Sample expense added.")

        # Optional: Add sample scholarships if needed
        if not Scholarship.query.first():
            sample_scholarship = Scholarship(
                name='Sample Scholarship',
                description='This is a sample scholarship description.',
                deadline=date(2024, 12, 31),  # Use a Python date object here
                eligibility='All students are eligible.',
                link='http://example.com'
            ) # type: ignore
            db.session.add(sample_scholarship)
            db.session.commit()
            print("Sample scholarship added.")

if __name__ == '__main__':
    init_db()
