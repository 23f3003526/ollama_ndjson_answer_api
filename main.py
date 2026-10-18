from fastapi import FastAPI

app = FastAPI(title="NDJSON Reconstruction Answer")

ANSWER = {
    "A": {
        "text": "Report job-95b60a1b: café\\nReady ✅",
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
async def answer():
    return ANSWER
