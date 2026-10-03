# Emotion Detection Web App (AI-based)

Final project for the IBM course **Developing AI Applications with Python and Flask** (Coursera).

## Project Name
**Emotion Detector** — an AI-based web application that detects emotions in text using the **Watson NLP** Emotion Predict library.

## Description
The user enters any English sentence in the web page, and the app returns scores for five emotions:
**anger, disgust, fear, joy, sadness**, plus the **dominant emotion**.

## Project Structure
```
final_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Tasks Covered
1. Fork & clone the project repository
2. Create the emotion detection app using Watson NLP
3. Format the output of the application
4. Package the application (`EmotionDetection`)
5. Run unit tests on the application
6. Deploy as a web application using Flask
7. Incorporate error handling (blank input)
8. Run static code analysis with PyLint (10/10)

## How to Run
```bash
python3.11 -m pip install requests flask pylint
python3.11 test_emotion_detection.py
python3.11 server.py
```
Then open `http://localhost:5000`.

## Tech Stack
Python · Flask · Watson NLP · unittest · PyLint
