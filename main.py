from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="template")
conn=MongoClient("mongodb://localhost:27017")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request ):
    docs=conn.notes.notes.find()
    newDoc=[]
    for doc in docs:
       newDoc.append({
           "id":doc["_id"],
           "note":doc["note"]
       })
    return templates.TemplateResponse("index.html",
       { "request":request,"newDoc":newDoc,"v":"vvv"}
    )