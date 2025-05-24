# 🧠 Multi-Model AI Chatbot (Gradio Interface)

An interactive chatbot app built with Python and Gradio that allows seamless switching between multiple LLM providers — OpenAI (GPT), Claude (Anthropic), and Gemini (Google). Each model retains its own chat history, making it easy to experiment and compare responses side-by-side.

---

![image](https://github.com/user-attachments/assets/0f62cb23-94ae-4053-bbe2-b47fb328ae4d)

---

## 🚀 Features

- 🔄 **Multi-Model Switching**: Choose between OpenAI, Claude, and Gemini.
- 💬 **Persistent Chat History**: Context is retained per model across messages.
- 🖼️ **Simple Gradio Interface**: Clean UI to interact and compare LLMs opens up in Browser tab.
- 🔐 **Environment Variable Support**: API keys managed securely via `.env`.

---

## Architecture

![image](https://github.com/user-attachments/assets/39b1e3e1-78c5-4466-9cb0-58e964039383)

---

## 🧰 Tech Stack

- Python 3.x
- Gradio
- OpenAI API
- Anthropic API
- Google Generative AI SDK
- python-dotenv

---

## 📦 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/multi-model-chatbot.git
   cd multi-model-chatbot

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Create a .env file with your API keys**  
   ```bash
   OPENAI_API_KEY=your-openai-key
   ANTHROPIC_API_KEY=your-anthropic-key
   GOOGLE_API_KEY=your-gemini-key

4. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # or venv\Scripts\activate on Windows

5. **Run the app**  
   ```bash
   python multi_model_chatbot_app.py

--

## Chat Interface Layout

![image](https://github.com/user-attachments/assets/bcb5a8f3-18fc-4504-8667-b862acd62bb7)

--

## 📁 Project Structure
   ```bash
  multi-model-chatbot/
  │
  ├── multi_model_chatbot_app.py    # Main application script
  ├── requirements.txt              # Dependencies
  ├── .gitignore                    # Git exclusions
  ├── .env                          # API keys (not committed)
  └── venv/                         # Virtual environment (excluded from Git)
```

---

## 📜 License
This project is licensed under the MIT License. Feel free to use, extend, or modify it.

---

## 🙌 Acknowledgements

- Gradio
- OpenAI
- Anthropic
- Google Generative AI

---
