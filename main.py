from socket import gethostname

from fastapi import FastAPI

app = FastAPI()
result = {gethostname(): 0}


@app.get("/")
async def root():
    result[gethostname()] += 1
    return {"message": f"{gethostname()} {result}"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
