"""Note routes module.

This module defines all the API endpoints for note operations.
"""

from typing import List, Dict
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from bson import ObjectId
from bson.errors import InvalidId

from services.note_service import NoteService
from utils.validation import validate_object_id

# Initialize router
note = APIRouter(
    tags=["notes"],
    responses={404: {"description": "Not found"}}
)

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="template")

# Service instance
note_service = NoteService()


@note.get("/", response_class=HTMLResponse)
async def get_all_notes(request: Request):
    """Retrieve and display all notes."""
    try:
        notes = note_service.get_all_notes()
        return templates.TemplateResponse("index.html", {"request": request, "newDoc": notes})
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving notes: {str(e)}"
        )


@note.post("/")
async def create_note(request: Request):
    """Create a new note from form data."""
    try:
        form = await request.form()
        formdict = dict(form)
        formdict["important"] = form.get("important") == "on"
        note_service.create_note(formdict)
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating note: {str(e)}"
        )


@note.post("/del/{item_id}")
async def delete_note(item_id: str):
    """Delete a note by its ID."""
    try:
        obj_id = validate_object_id(item_id)
        note_service.delete_note_by_id(obj_id)
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting note: {str(e)}"
        )


@note.patch("/update/{item_id}")
async def update_note(item_id: str, updated_fields: Dict):
    """Update specific fields of a note by its ID."""
    try:
        obj_id = validate_object_id(item_id)
        updated_note = note_service.update_note_by_id(obj_id, updated_fields)
        return updated_note
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating note: {str(e)}"
        )
