from app import app
from models.db import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def seed_data():
    with app.app_context():
        try:
            print("Starting database sending...")
            try:
                db.drop_all()
                db.create_all()
                print("Tables dropped and recreated successfully. ")
            
                seed_users = [
                    User(
                        fname= "admin",
                        lname="User",
                        uname="admin",
                        email="admin@example.com",
                        pass_word=generate_password_hash("admin123")
                    
                    ),
                    User(
                        fname="Fel",
                        lname="Dela Cruz",
                        uname="juandc",
                        email="felicity@gamil.com",
                        pass_word=generate_password_hash("password123"),
                    ),
                ]

                for user in seed_users:
                    exisiting_user = User.query.filter_by (email=user.email).first()
                    if exisiting_user:
                        print(f"Skipping existing user: {user.email}")
                        continue
                    db.session.add(user)

                db.session.commit()
                print("Database seeding completed successfully.")
            except SQLAlchemyError as e:
                print(f"Warning: Could not recreate tables. Error: {e}")


        except IntegrityError as ie:
            db.session.rollback()
            print(f"Integrity Error: {ie.orig}")

        except SQLAlchemyError as sae:
            db.session.rollback()
            print(f"SQLAlchemy Error: {e}")
        except Exception as e:
            db.session.rollback()
            print(f"Unexpected error: {e}")

        finally:
            db.session.close()

if __name__ == "__main__":
    seed_data()
                   
            