from fastapi.responses import JSONResponse
import json

@app.get("/")
def get_answer():
    with open("answer.json", encoding="utf-8") as f:
        data = json.load(f)
    return JSONResponse(content=data)
