import spacy
from spacy.tokens import DocBin

# Load blank English model
nlp = spacy.blank("en")

# Your TRAINING DATA (PASTE YOUR DATA HERE IF NOT LOADING)
TRAIN_DATA = [
    ("Add 2 cups of rice", {"entities": [(4, 5, "QUANTITY"), (6, 10, "UNIT"), (14, 18, "INGREDIENT")]}),
    ("Chop 1 onion finely", {"entities": [(5, 6, "QUANTITY"), (7, 12, "INGREDIENT")]}),
    ("Mix 200 ml milk with sugar", {"entities": [(4, 7, "QUANTITY"), (8, 10, "UNIT"), (11, 15, "INGREDIENT"), (21, 26, "INGREDIENT")]}),
    # 👉 ADD THE REST OF YOUR DATASET HERE
]

doc_bin = DocBin()

for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annotations["entities"]:
        span = doc.char_span(start, end, label=label)
        if span is not None:
            ents.append(span)
    doc.ents = ents
    doc_bin.add(doc)

# Save to binary .spacy file
doc_bin.to_disk("data/annotated/train.spacy")

print("✅ train.spacy created successfully (DocBin format)")
