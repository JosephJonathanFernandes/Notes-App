"""Note routes module.

This module defines all the API endpoints for note operations.
"""

from typing import List
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from bson.errors import InvalidId

from model.note import Note
from config.db import conn, DATABASE_NAME
from schema.note import noteCreate, Notes

# Initialize router
note = APIRouter(
    tags=["notes"],
    responses={404: {"description": "Not found"}}
)

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="template")

# Get database and collection references
db = conn[DATABASE_NAME]
notes_collection = db.notes


@note.get("/", response_class=HTMLResponse)
async def get_all_notes(request: Request):
    """Retrieve and display all notes.
    
    Args:
        request: The incoming HTTP request
        
    Returns:
        HTML page with all notes
    """
    try:
        docs = notes_collection.find()
        newDoc = []
        for doc in docs:
            newDoc.append({
                "id": str(doc["_id"]),
                "title": doc.get("title", ""),
                "description": doc.get("description", ""),
                "important": doc.get("important", False),
            })
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "newDoc": newDoc}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving notes: {str(e)}"
        )


@note.post("/")
async def create_note(request: Request):
    """Create a new note from form data.
    
    Args:
        request: The incoming HTTP request with form data
        
    Returns:
        Redirect to home page
    """
    try:
        form = await request.form()
        formdict = dict(form)
        
        # Convert checkbox value to boolean
        formdict["important"] = form.get("important") == "on"
        
        # Insert note into database
        result = notes_collection.insert_one(formdict)
        
        if not result.inserted_id:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create note"
            )
            
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating note: {str(e)}"
        )


@note.post("/del/{item_id}")
async def delete_note(item_id: str):
    """Delete a note by its ID.
    
    Args:
        item_id: The MongoDB ObjectId of the note to delete
        
    Returns:
        Redirect to home page
        
    Raises:
        HTTPException: If the note ID is invalid or deletion fails
    """
    try:
        # Validate ObjectId
        obj_id = ObjectId(item_id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid note ID format"
        )
    
    try:
        result = notes_collection.delete_one({"_id": obj_id})
        
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Note not found"
            )
            
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting note: {str(e)}"
        )
