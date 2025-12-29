# Recipe Ingredient Extraction using NER 
 
This project extracts ingredients, quantities, and units from cooking recipes using a custom spaCy Named Entity Recognition (NER) model and exposes the functionality via a Flask API. 

## Known Limitations

This project uses a Named Entity Recognition (NER) model to extract
INGREDIENT, QUANTITY, and UNIT entities from recipe text.

NER models predict entities independently and do not model relationships
between entities. As a result, in some cases, a unit may not be perfectly
associated with its ingredient (e.g., when the unit appears after the
ingredient in the sentence).

For a production-grade system, this can be improved by:
- Syntactic dependency parsing
- Rule-based post-processing
- Relation extraction models


