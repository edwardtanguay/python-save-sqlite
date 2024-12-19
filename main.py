import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db.sqlite") 
Base = declarative_base()

url = "https://edwardtanguay.vercel.app/share/skills.json"

response = requests.get(url)

if response.status_code == 200:
	data = response.json()

	for item in data[:5]:
		print(item)
else:
	print(f"Failed to fetch data: {response.status_code}")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# save data
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
new_user = User(name="Hans", age=22)
session.add(new_user)
new_user = User(name="Sarah", age=20)
session.commit()

# display data
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")
