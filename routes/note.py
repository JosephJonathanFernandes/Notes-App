from model.note import Note
from fastapi import APIRouter
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from config.db import conn
from bson import ObjectId
from schema.note import noteCreate,Notes


note=APIRouter()


templates = Jinja2Templates(directory="template")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request ):
    docs=conn.notes.notes.find()
    newDoc=[]
    for doc in docs:
       newDoc.append({
           "id":doc["_id"],
           "title":doc["title"],
           "description":doc["description"],
           "important":doc["important"],
       })
    return templates.TemplateResponse("index.html",
       { "request":request,"newDoc":newDoc}
    )

@note.post("/")
async def add_note(request:Request):
    form=await request.form()
    formdict=dict(form)
    formdict["important"]=True if form.get("important")=="on" else False
    note=conn.notes.notes.insert_one(formdict)
    return RedirectResponse(url="/", status_code=303)


@note.post("/del/{item_id}")
async def dell(item_id):
   l=conn.notes.notes.delete_one({"_id":ObjectId(item_id)})
   return RedirectResponse(url="/", status_code=303)
