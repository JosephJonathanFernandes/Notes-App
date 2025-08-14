from model.note import Note

def noteCreate(item)->Note:
    return {
        "id":item["_id"],
        "title":item["title"],
        "description":item["description"],
        "important":item["important"]

    }

def Notes(items)->list:
    return [noteCreate(item) for item in items]
