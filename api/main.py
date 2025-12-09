from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Microservice")

# Allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Adjust for production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from API Microservice!"}

@app.get("/api/user")
def read_api_api():
    return {"message": "Single user goes here!"}

@app.get("/api/users")
def read_users():
    return {"message": "Users list goes here"}

