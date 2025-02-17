from sqlalchemy import Column, Integer, String
from src.database import Base

class jero_test(Base):
    __tablename__ = "jero_test"

    id = Column(Integer, primary_key=True, index=True)
    questions = Column(String, index=True)
    responses = Column(String, index=True)

    def __repr__(self):
        return f"<JeroTest(id={self.id}, question={self.responses}, reponse={self.responses})>"