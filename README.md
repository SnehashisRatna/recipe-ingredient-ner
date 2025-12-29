# Recipe Ingredient Extraction using Named Entity Recognition (NER)
 
This project extracts ingredients, quantities, and units from cooking recipes using a custom spaCy Named Entity Recognition (NER) model and exposes the functionality via a Flask API. 


- **INGREDIENT** (e.g., rice, sugar)
- **QUANTITY** (e.g., 2, 1)
- **UNIT** (e.g., cups, tablespoon)

A **custom-trained spaCy Named Entity Recognition (NER) model** is used for extraction, and the model is deployed through a **Flask REST API** that returns results in **JSON format**.

This project is implemented as a **learning-oriented prototype**, covering the complete workflow from dataset creation to API deployment.

---

## Technologies Used

- Python 3.10  
- spaCy (NER model training)  
- Flask (REST API)  
- Docker (containerization)  
- Git & GitHub  

---

## Project Structure
      recipe-ingredient-ner/
│
├── api/
│ ├── app.py # Flask application
│ ├── ner_inference.py # Model inference logic
│ └── utils.py # Input validation
│
├── data/
│ └── annotated/
│ └── train.spacy # Training data (DocBin format)
│
├── training/
│ ├── config.cfg # spaCy training configuration
│ └── convert_to_docbin.py# Dataset conversion script
│
├── model/ # Trained spaCy model (not committed)
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md



---

## Dataset and Model Training

- A small, manually annotated recipe dataset was created.
- Each sentence was labeled with the entities: `INGREDIENT`, `QUANTITY`, and `UNIT`.
- The dataset was converted into **spaCy DocBin (`.spacy`) format**, which is required for spaCy v3 training.
- A custom **spaCy NER model** was trained using this dataset.

Since this is a prototype and the dataset is small, the same data was used for both training and evaluation. This is acceptable for demonstration and learning purposes.

---

## Flask API

The trained NER model is exposed through a Flask REST API.

### API Endpoint

**URL:** `/extract`  
**Method:** `POST`  
**Content-Type:** `application/json`

---

### Request Example

```json
{
  "recipe_text": "Add 2 cups of rice and 1 tablespoon sugar"
}

{
  "recipe_text": "Add 2 cups of rice and 1 tablespoon sugar",
  "ingredients": [
    {
      "ingredient": "rice",
      "quantity": "2",
      "unit": "cups"
    },
    {
      "ingredient": "sugar",
      "quantity": "1",
      "unit": null
    }
  ]
}

## Known Limitations

This system uses Named Entity Recognition (NER), which predicts entities independently and does not model relationships between them.

As a result:

In some cases, a UNIT may not be perfectly associated with its INGREDIENT, especially when the unit appears after the ingredient in the sentence.

This behavior is expected in NER-based systems.

Possible Improvements (Future Work)

Dependency parsing to capture grammatical relationships

Rule-based post-processing for entity association

Relation extraction models

These improvements were intentionally kept out of scope to maintain simplicity and focus on core NLP concepts.

How to Run the Project (Without Docker)

Create and activate a virtual environment

Install dependencies:

pip install -r requirements.txt


Start the Flask server:

python api/app.py


Test the API using PowerShell, CMD, or Postman

How to Run the Project (Using Docker)

Build the Docker image:

docker build -t recipe-ingredient-ner .


Run the Docker container:

docker run -p 5000:5000 recipe-ingredient-ner


Access the API at:

http://127.0.0.1:5000/extract

Learning Outcomes

Through this project, I gained hands-on experience with:

Creating and annotating NLP datasets

Training custom spaCy NER models

Converting datasets to DocBin format

Building REST APIs using Flask

Debugging model inference behavior

Understanding real-world NLP limitations

Containerizing machine learning applications using Docker

Conclusion

This project demonstrates an end-to-end NLP pipeline for extracting structured data from unstructured recipe text. While the system is a prototype, it effectively showcases how machine learning models can be trained, deployed, and served through APIs for practical applications.
