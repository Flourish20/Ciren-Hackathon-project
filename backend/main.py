from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Ciren Hackathon API")


@app.get("/")
def read_root():
    return {"status": "ok"}
