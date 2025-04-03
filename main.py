from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os
import openai
import uvicorn

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
      <head><title>Jogging GPT</title></head>
      <body>
        <h1>👟 Welcome to Jogging GPT!</h1>
        <p>Server is running successfully ✅</p>
      </body>
    </html>
    """

@app.post("/gpt")
async def ask_gpt(request: Request):
    body = await request.json()
    prompt = body.get("prompt")

    if not prompt:
        return {"error": "Prompt is missing."}

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message["content"]
        return {"response": answer}
    except Exception as e:
        return {"error": str(e)}

# Для запуска через Render (указываем PORT!)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
