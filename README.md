# NLP Insight Explorer

An intelligent, full-stack Natural Language Processing (NLP) web application that provides state-of-the-art **Text Summarization** and **Sentiment Analysis**.

![NLP Insight Explorer Banner](https://img.shields.io/badge/NLP-Insight%20Explorer-ff007f?style=for-the-badge)

## 📌 Project Overview
Built for complex NLP tasks, this application allows users to input any length of text and receive:
1. **Abstractive Summarization:** A concise summary of the main points extracted from large paragraphs using the `sshleifer/distilbart-cnn-12-6` model.
2. **Sentiment Analysis:** A concrete sentiment gauge classifying the overall tone (Positive, Negative, or Neutral) and returning its confidence score using `distilbert-base-uncased-finetuned-sst-2-english`.

## ✨ Features
- **Premium Glassmorphism UI:** A gorgeous, responsive frontend with atmospheric floating background effects. No external JavaScript frameworks required!
- **FastAPI Backend:** Fully asynchronous, concurrent logic processing for lighting fast NLP inference.
- **Hugging Face Integration:** Securely implemented singleton architecture to load heavy Deep Learning models efficiently on boot.
- **All-in-one Deployment:** Backend seamlessly serves the frontend static files on a single port for maximum simplicity.

## 💻 Tech Stack
- **Backend**: Python 3, FastAPI, Uvicorn, Pydantic
- **AI / NLP**: Hugging Face `transformers`, PyTorch
- **Frontend**: Vanilla HTML5, CSS3 (with custom variables and CSS animations), JavaScript (Async Fetch API)

## 📁 Project Structure
```text
23BAI10139_NLP/
├── backend/
│   ├── main.py            # FastAPI application and endpoint definitions
│   ├── nlp_engine.py      # HuggingFace pipeline implementations
│   └── requirements.txt   # Python dependencies
├── frontend/
│   ├── index.html         # User Interface Layout
│   ├── style.css          # Premium Design System & Animations
│   └── app.js             # API Integration and DOM Manipulation
└── README.md
```

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed. You **do not** need Node.js or `npm`.

### Installation
1. Open up your terminal and navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   *(We recommend doing this inside a Python virtual environment `venv`)*

### Running the App
1. With the requirements installed, run the server from the `backend` directory:
   ```bash
   python main.py
   ```
2. The API will spin up and load the AI models into memory. 
3. Open your favorite web browser and visit:
   ```
   http://localhost:8000
   ```

> **Note:** The very first time you click "Analyze Insights", the Hugging Face models will initiate a background download if they aren't already locally cached. This may take a few moments depending on your network connection. Subsequent requests will be extremely fast!
