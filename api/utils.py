def validate_input(data):
    if not data:
        return False, "Empty request body"

    if "recipe_text" not in data:
        return False, "Missing 'recipe_text' field"

    if not isinstance(data["recipe_text"], str):
        return False, "'recipe_text' must be a string"

    if len(data["recipe_text"].strip()) == 0:
        return False, "'recipe_text' cannot be empty"

    return True, None
