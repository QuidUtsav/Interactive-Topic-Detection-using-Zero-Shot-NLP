# Interactive Topic Detection using Zero-Shot NLP

This project is an interactive command-line program that analyzes user input text and identifies the main topic(s) being discussed.  
It uses a transformer-based **zero-shot classification** model, allowing topic detection without training on a labeled dataset.

The goal of this project is to demonstrate **semantic understanding of text**, not keyword matching or traditional bag-of-words techniques.

---

## ✨ Features

- Interactive command-line interface
- Zero-shot topic classification using Hugging Face Transformers
- Human-readable topic labels
- Displays confidence scores for predictions
- Runs on CPU (no GPU required)
- Easily extensible topic list

---

## 🧠 How It Works

1. The user enters free-form text.
2. A zero-shot classification model compares the text against a predefined list of topic labels.
3. The model computes semantic similarity between the input and each topic.
4. The program outputs the most relevant topic(s) with confidence scores.

Unlike traditional classifiers, this approach does **not** require task-specific training data.

---

## 🏷️ Topic Categories

The program currently supports the following topics:

- Technology  
- Programming and Software Development  
- Artificial Intelligence and Machine Learning  
- Education and Learning  
- Science and Research  
- Business and Careers  
- Health and Fitness  
- Personal Life and Relationships  
- Entertainment and Media  
- Politics and Society  
- Current Events and News  
- Philosophy and Personal Thoughts  
- Food and Cooking  

Topics can be easily modified or extended in the source code.

---

## 🛠️ Technologies Used

- Python
- Hugging Face Transformers
- `facebook/bart-large-mnli` zero-shot classification model

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/interactive-topic-detector.git
   cd interactive-topic-detector
