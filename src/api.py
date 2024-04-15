from fastapi import FastAPI

app = FastAPI()

@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}