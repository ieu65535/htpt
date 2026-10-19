from fastapi import FastAPI
app = FastAPI()

@app.get("/{path:path}", status_code=418)
async def teapot():
    return {
        "error": "I'm a teapot",
        "status": 418,
        "message": "The server refuses to brew coffee because it is, permanently, a teapot.",
    }
