def individual_data(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "completed": todo["completed"],
    }


def all_data(todos):
    return [individual_data(todo) for todo in todos]
