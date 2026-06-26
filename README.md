# 🚀 AI Text Utility Suite

An AI-powered text processing web application built using **Python**, **Streamlit**, and **Groq LLM**. The application provides multiple intelligent text utilities through a clean, responsive, and user-friendly interface.

---

## 📌 Overview

AI Text Utility Suite is designed to simplify everyday text-processing tasks using Large Language Models (LLMs). It enables users to generate, transform, and improve text instantly through an intuitive web interface.

The application demonstrates integration with modern AI APIs, secure environment variable management, and a modular application structure suitable for future scalability.

---

## ✨ Features

- 📝 Text Summarization
- 📧 Professional Email Generator
- 🌍 Language Translator
- 🎯 Grammar & Spell Checker
- 😊 Sentiment Analysis
- ✍️ Text Rewriter
- ⚡ Fast AI responses powered by Groq LLM
- 🎨 Modern and responsive Streamlit UI
- 🔒 Secure API key management using `.env`

---

## 🛠️ Technologies Used

- Python 3
- Streamlit
- Groq API
- python-dotenv
- Git
- GitHub

---

## 📂 Project Structure

```
AI-CHATBOT/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env (not uploaded)
└── screenshots/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sanjanavishwanath07/ai-text-utility-suite.git
```

### 2. Navigate to the project

```bash
cd ai-text-utility-suite
```

### 3. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### 🏠 Home

![Home](./screenshots/home.png)

### 📝 Text Summarizer

![Text Summarizer](./screenshots/summarizer.png)

### 📧 Email Generator

![Email Generator](./screenshots/email%20generator.png)

### 🌍 Language Translator

![Language Translator](./screenshots/language%20translator.png)

---

## 💡 Future Enhancements

- PDF text summarization
- OCR support for images
- Voice-to-text conversion
- Chatbot mode
- File upload support
- Conversation history
- Multiple AI model selection

---

## 🔐 Security

Sensitive credentials are stored securely using environment variables and are excluded from version control via `.gitignore`.

---

## 👩‍💻 Author

**Sanjana V S**

Artificial Intelligence & Machine Learning Student

GitHub: https://github.com/sanjanavishwanath07

---

## 📄 License

This project is developed for educational and assessment purposes.
