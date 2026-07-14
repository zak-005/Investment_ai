from fastapi import FastAPI


app = FastAPI(
    title="FinSight API Gateway",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Finsight API Gateway"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }