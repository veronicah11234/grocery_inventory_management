from flask_sqlalchemy import SQLAlchemy
# import uuid
# from dbqueries import insert_category, select_all_categories

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    @staticmethod
    def get_all_categories():
        return Category.query.all()

    # You can define other methods here to interact with categories, such as adding, updating, or deleting categories
