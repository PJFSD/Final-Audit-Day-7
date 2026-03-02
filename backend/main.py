from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crud import get_all_projects

app = FastAPI()

# CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/projects")
def read_projects():
    return get_all_projects()