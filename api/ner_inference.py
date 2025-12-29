import spacy

class RecipeNER:
    def __init__(self, model_path="model/model-last"):
        self.nlp = spacy.load(model_path)

    def extract_entities(self, text):
        doc = self.nlp(text)
        ents = list(doc.ents)

        ingredients = []
        quantity = None
        unit = None

        for i, ent in enumerate(ents):
            if ent.label_ == "QUANTITY":
                quantity = ent.text

            elif ent.label_ == "UNIT":
                unit = ent.text

            elif ent.label_ == "INGREDIENT":
                # Look ahead for UNIT if not already seen
                if unit is None and i + 1 < len(ents) and ents[i + 1].label_ == "UNIT":
                    unit = ents[i + 1].text

                ingredients.append({
                    "ingredient": ent.text,
                    "quantity": quantity,
                    "unit": unit
                })

                quantity = None
                unit = None

        return ingredients
