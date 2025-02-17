from fastapi import FastAPI, Depends, Form
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from src.database import get_db
from src.models import jero_test

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Route pour afficher la page HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

from pydantic import BaseModel
# Route pour ajouter un test


class TestData(BaseModel):
    question: str
    response: str

@app.post("/add_test/")
async def add_test(data: TestData, db: AsyncSession = Depends(get_db)):
    test = jero_test(questions=data.question, responses=data.response)
    db.add(test)
    await db.commit() 
    print(data.question, data.response)
    return {"message": "Test ajouter avec sucès", "user": {"Question": data.question, "Response": data.response}}


# Route pour récupérer tous les tests
@app.get("/test/")
async def get_test(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(jero_test))
    test = result.scalars().all()
    return test