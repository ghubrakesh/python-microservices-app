from fastapi import FastAPI
import uvicorn
from mylib.logic import wiki as search_page
from mylib.logic import search_wiki
from mylib.logic import phrase as wikiphrases

app = FastAPI()


@app.get("/")
async def home():
    return {
        "message": "Enter the /search/<query> to search the pages or \n /wiki/<name> to get the summary of the page"
    }


@app.get("/search/{query}")
async def search(query: str):
    """retrive wikipedia and return maching pages"""
    res = search_wiki(query)
    d = dict()
    for i in range(len(res)):
        d[i + 1] = res[i]
    return {"result": d}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """retrive wikipedia page and return summary"""
    res = search_page(name)
    return {name: res}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """retrive wikipedia page and return phrases"""
    res = wikiphrases(name)
    return {"results": res}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
