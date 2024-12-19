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

class Skill(Base):
    __tablename__ = "skills"
    idCode = Column(String)
    name = Column(String)
    url = Column(String)
    description = Column(String)

# save data
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
skill = Skill(idCode="react", name="React", url="httpnnn", description="ddd")
session.add(skill)
session.commit()

# display data
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")

