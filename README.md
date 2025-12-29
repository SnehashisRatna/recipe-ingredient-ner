# Recipe Ingredient Extraction using Named Entity Recognition (NER)

## Project Overview

This project extracts structured ingredient information from cooking recipes using **Natural Language Processing (NLP)**.  
Given a recipe text, the system identifies and extracts:

- **INGREDIENT** (e.g., rice, sugar)
- **QUANTITY** (e.g., 2, 1)
- **UNIT** (e.g., cups, tablespoon)

A custom-trained **spaCy Named Entity Recognition (NER)** model is used for extraction, and the model is deployed using a **Flask REST API** that returns structured output in **JSON format**.

This project is implemented as a **learning-oriented student prototype**, covering the complete workflow from dataset creation to API deployment.

---

## Technologies Used

- Python 3.10
- spaCy (NER model training)
- Flask (REST API)
- Docker (containerization)
- Git & GitHub

---


---

## Dataset and Model Training

- A small, manually annotated recipe dataset was created.
- Each sentence is labeled with the entities:
  - `INGREDIENT`
  - `QUANTITY`
  - `UNIT`
- The dataset was converted into **spaCy DocBin (`.spacy`) format**, which is required for spaCy v3.
- A custom **spaCy NER model** was trained using this dataset.

Since this is a prototype and the dataset is small, the same data was used for both training and evaluation. This is acceptable for demonstration and learning purposes.

---

## Flask API

The trained NER model is exposed through a Flask REST API.

### API Endpoint

- **URL:** `/extract`
- **Method:** `POST`
- **Content-Type:** `application/json`

## Known Limitations

This system uses **Named Entity Recognition (NER)**, which predicts entities independently and does not model relationships between them.

As a result:

- In some cases, a **UNIT** may not be perfectly associated with its **INGREDIENT**, especially when the unit appears after the ingredient in the sentence.
- This behavior is expected in NER-based systems.

### Possible Improvements (Future Work)

- Dependency parsing to capture grammatical relationships  
- Rule-based post-processing for entity association  
- Relation extraction models  

These improvements were intentionally kept out of scope to maintain simplicity and focus on core NLP concepts.

---

## How to Run the Project (Without Docker)

1. Create and activate a virtual environment

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Start the Flask server:
   ```bash
   python api/app.py
4. Test the API using PowerShell, CMD, or Postman

