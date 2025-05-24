import gradio as gr
import os
from dotenv import load_dotenv
import openai
import anthropic
import google.generativeai as genai

# Load API keys from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
anthropic_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# History tracker
chat_histories = {
    "OpenAI": [],
    "Claude": [],
    "Gemini": []
}

# Model handler
def chat_with_model(model_name, user_message):
    history = chat_histories[model_name]

    if model_name == "OpenAI":
        history.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=history,
            max_tokens=200
        )
        reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": reply})

    elif model_name == "Claude":
        history.append({"role": "user", "content": user_message})
        response = anthropic_client.messages.create(
            model="claude-3-haiku-20240307",
            messages=history,
            max_tokens=200
        )
        reply = response.content[0].text
        history.append({"role": "assistant", "content": reply})

    elif model_name == "Gemini":
        if not history:
            history_obj = genai.GenerativeModel("models/gemini-1.5-flash-latest").start_chat(history=[])
            chat_histories["Gemini"] = history_obj
        else:
            history_obj = chat_histories["Gemini"]
        reply = history_obj.send_message(user_message).text

    return reply

# Gradio UI
def chat_interface(model, message):
    reply = chat_with_model(model, message)
    return reply

force_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

gr.Interface(
    fn=chat_interface,
    inputs=[gr.Radio(["OpenAI", "Claude", "Gemini"], label="Choose Model"), gr.Textbox(label="Your Message")],
    outputs=gr.Textbox(label="Response"),
    js=force_dark_mode,
    title="Multi-Model AI Chat"
).launch(inbrowser=True, share=True)