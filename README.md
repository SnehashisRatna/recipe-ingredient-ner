# Recipe Ingredient Extraction using Named Entity Recognition (NER)

This project implements an end-to-end **Recipe Ingredient Extraction system** using **Natural Language Processing (NLP)**.  
It extracts **ingredients, quantities, and units** from unstructured cooking recipe text using a **custom-trained spaCy Named Entity Recognition (NER) model**, and exposes the functionality through a **Flask REST API** with an optional web interface.

The project is developed as a **learning-oriented prototype**, covering the complete workflow from dataset creation and model training to API deployment and containerization.

---

##  Objective

The main goal of this project is to:
- Automatically extract structured information from recipe text
- Understand how custom NER models are trained using spaCy
- Deploy a trained NLP model through a REST API
- Gain hands-on experience with real-world NLP limitations

---

##  Entity Schema

The model is trained to recognize the following entities:

- **INGREDIENT** – food items (e.g., rice, sugar, cocoa powder)
- **QUANTITY** – numeric or word-based amounts (e.g., 2, one, half)
- **UNIT** – measurement units (e.g., cups, tablespoon, ml)

---

## 🛠️ Technologies Used

- **Python 3.10**
- **spaCy** (custom NER model training)
- **Flask** (REST API)
- **HTML / JavaScript** (lightweight frontend)
- **Docker** (containerization)
- **Git & GitHub** (version control)

---

## 📊 Dataset and Model Training

- A **manually annotated recipe dataset** was created using spaCy’s entity format.
- The raw dataset is maintained in **Python format** (`train_data.py`) for readability and version control.
- The dataset is converted into **spaCy DocBin (`.spacy`) format**, which is required for spaCy v3 training.
- A **custom NER model** was trained using this dataset.

> Since this is a prototype and the dataset is small, the same data was used for both training and evaluation.  
> This is acceptable for learning and demonstration purposes.

---

## 🚀 Flask API

The trained NER model is served via a Flask REST API.

###  Endpoint

- **URL:** `/extract`
- **Method:** `POST`
- **Content-Type:** `application/json`

###  Request Example

```json
{
  "recipe_text": "Add 2 cups of rice and 1 tablespoon sugar"
}

###  Response Example

```{
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
```
  ---
## Web Interface 

A lightweight web interface is provided to:

- Enter recipe text

-View extracted entities

-Display results in a table format

This makes the project easier to demonstrate and test without external tools.

## Known Limitations

This system uses Named Entity Recognition (NER), which predicts entities independently and does not model relationships between them.

As a result:

-In some cases, a UNIT may not be perfectly associated with its INGREDIENT

-Errors may occur in medium or complex sentences

-This behavior is expected in NER-based systems

---

## How to Run the Project (Without Docker)

1. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Start the Flask server:
   ```bash
   python api/app.py
4. Test the API using PowerShell, CMD, or Postman
5. Access the application
   -API Endpoint: http://127.0.0.1:5000/extract
   -Web UI: http://127.0.0.1:5000/

  ---

## How to Run the Project (Using Docker)

1. Build the Docker image
   ```bash
   docker build -t recipe-ingredient-ner .
2. Run the Docker container
   ```bash
   docker run -p 5000:5000 recipe-ingredient-ner
3. Access the application
   -API Endpoint: http://127.0.0.1:5000/extract
   -Web UI: http://127.0.0.1:5000/

 ---

## Learning Outcomes

-Through this project, I gained hands-on experience with:

-Creating and annotating NLP datasets

-Training custom spaCy NER models

-Converting datasets to DocBin format

-Building REST APIs using Flask

-Debugging real-world NLP behavior

-Understanding limitations of NER models

-Containerizing ML applications using Docker

## Conclusion

This project demonstrates a complete NLP pipeline for extracting structured information from unstructured recipe text.
While the system is a prototype, it effectively showcases how machine learning models can be trained, deployed, and served through APIs for practical applications.