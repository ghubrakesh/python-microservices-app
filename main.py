from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as search_page
from mylib.logic import search_wiki

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Enter the /search/<query> to search the pages or \n /wiki/<name> to get the summary of the page"}

@app.get("/search/{query}")
async def search(query:str):
    res =  search_wiki(query)
    d = dict()
    for i in range(len(res)):
        d[i+1] = res[i]
    return {"result": d}

@app.get("/wiki/{name}")
async def wiki(name:str):
    res = search_page(name)
    return {"result": res}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")