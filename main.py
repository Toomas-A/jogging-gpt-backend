from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# 🌐 Главная страница для проверки деплоя
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h1>✅ Jogging GPT Backend is Running</h1>
    <p>POST your data to <code>/gpt</code> to get running shoe recommendations.</p>
    """

# 📦 Структура запроса
class GPTRequest(BaseModel):
    prompt: str

# 🤖 Маршрут обращения к GPT
@app.post("/gpt")
async def ask_gpt(request: GPTRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Или "gpt-3.5-turbo" при необходимости
            messages=[
                {"role": "system", "content": "Ты эксперт по подбору беговых кроссовок."},
                {"role": "user", "content": request.prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )

        reply = response.choices[0].message["content"]
        return JSONResponse(content={"reply": reply})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
