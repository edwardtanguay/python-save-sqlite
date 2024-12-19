from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database engine and base
engine = create_engine("sqlite:///example.db")  # SQLite database file
Base = declarative_base()

# Define the table as a Python class
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Write: Add a new user
new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()

# Read: Query the users table
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
