def individual_sirial(todo) ->dict:
    return{
        "id":str(todo["_id"]),
        "name":todo["name"],
        "description":todo["description"],
        "complete":todo["complete"],
}

def list_sirial(todos) ->dict:
    return [individual_sirial(todo) for todo in todos] 