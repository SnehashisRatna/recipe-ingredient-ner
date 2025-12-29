from flask import Flask, request, jsonify
from ner_inference import RecipeNER
from utils import validate_input

app = Flask(__name__)
ner = RecipeNER()

@app.route("/extract", methods=["POST"])
def extract():
    data = request.get_json(force=True)
    valid, error = validate_input(data)

    if not valid:
        return jsonify({"error": error}), 400

    recipe_text = data["recipe_text"]
    entities = ner.extract_entities(recipe_text)

    return jsonify({
        "recipe_text": recipe_text,
        "ingredients": entities
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
