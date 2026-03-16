from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import shutil

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from ats_scoring import calculate_ats_score

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze", response_class=HTMLResponse)
async def analyze_resume(request: Request, file: UploadFile):

    file_location = "resume.pdf"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_resume_text(file_location)

    skills = extract_skills(text)

    score = calculate_ats_score(skills)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "score": score,
            "skills": skills
        }
    )