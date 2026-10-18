# NDJSON reconstruction answer endpoint

Deploy as a Render Web Service.

- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

The root GET endpoint `/` returns the required raw JSON response (not an HTML page).
After deployment, submit the base URL, e.g. `https://your-service.onrender.com`.
