"""Service layer for note operations."""

from typing import List, Dict
from bson import ObjectId
from config.db import conn, DATABASE_NAME

class NoteService:
    def __init__(self):
        self.collection = conn[DATABASE_NAME].notes

    def get_all_notes(self) -> List[Dict]:
        """Retrieve all notes from the database."""
        docs = self.collection.find()
        return [
            {
                "id": str(doc["_id"]),
                "title": doc.get("title", ""),
                "description": doc.get("description", ""),
                "important": doc.get("important", False),
            }
            for doc in docs
        ]

    def create_note(self, note_data: Dict):
        """Insert a new note into the database."""
        result = self.collection.insert_one(note_data)
        if not result.inserted_id:
            raise Exception("Failed to create note")

    def delete_note_by_id(self, note_id: ObjectId):
        """Delete a note by its ID."""
        result = self.collection.delete_one({"_id": note_id})
        if result.deleted_count == 0:
            raise Exception("Note not found")

    def update_note_by_id(self, note_id: ObjectId, updated_fields: Dict) -> Dict:
        """Update a note by its ID."""
        result = self.collection.update_one(
            {"_id": note_id}, {"$set": updated_fields}
        )
        if result.matched_count == 0:
            raise Exception("Note not found")
        return self.collection.find_one({"_id": note_id})