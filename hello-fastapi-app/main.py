from fastapi import FastAPI
from fastapi.responses import JSONResponse

app=FastAPI(title="Hello FastAPI App", version="1.0.0")
@app.get("/health")
def health():
    return JSONResponse({"status": "ok"})
@app.get("/")
def root():
    return {"message": "Hello, World!"}
