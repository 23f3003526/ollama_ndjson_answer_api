
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

ANSWER = {
    "A": {
        "text": "Report job-95b60a1b: caf\u00e9" + chr(10) + "Ready \u2705",
        "complete": True,
        "error": None
    },
    "B": {
        "text": "Partial job-95b60a1b",
        "complete": False,
        "error": None
    },
    "C": {
        "text": "Draft job-95b60a1b",
        "complete": False,
        "error": "model unloaded"
    }
}

@app.get("/")
def get_answer():
    return JSONResponse(content=ANSWER)
