from fastapi import FastAPI, Depends, Form
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from src.database import get_db
from src.models import jero_test
from fastapi.middleware.cors import CORSMiddleware


# Liste des origines autorisées
allowed_origins = [
    "*"
    #"http://localhost:3000",  # Ex: Frontend React en local
    #"https://Jero1onrender.com",   # Ex: Domaine en production
]

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


@app.get("/test/", response_class=HTMLResponse)
async def get_test(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(jero_test))
    tests = result.scalars().all()

    # Convertir les objets SQLAlchemy en une liste de dictionnaires
    test_data = [{"id": t.id, "questions": t.questions, "responses": t.responses} for t in tests]

    return templates.TemplateResponse("test.html", {"request": request, "test_data": test_data})

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Seuls ces domaines peuvent accéder à l'API
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les headers
)

url = "https://fast-api-xj59.onrender.com/"