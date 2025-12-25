from app import db, User, app

with app.app_context():
    db.create_all()
    admin = User(username="admin", password="1234")
    db.session.add(admin)
    db.session.commit()
    print("Admin created successfully!")
