from fastapi import FastAPI
app = FastAPI()

@app.post("/")
async def read_frame():
    return {"messege": "Hello, World"}
