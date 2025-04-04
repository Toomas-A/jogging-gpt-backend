from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://toomas-a.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
      <head><title>Jogging GPT</title></head>
      <body>
        <h1>👟 Jogging GPT работает!</h1>
        <p>Мок-сервер запущен (без GPT)</p>
      </body>
    </html>
    """

@app.post("/gpt")
async def mock_response(request: Request):
    body = await request.json()
    prompt = body.get("prompt")

    if not prompt:
        return {"error": "❌ Prompt is missing"}

    print("📥 Мок получен:", prompt)

    # Фейковые данные
    return {
        "response": [
            {
                "brand": "Asics",
                "model": "Gel-Nimbus 26",
                "year": "2025",
                "weight": "290g",
                "cushioning": "Maximal",
                "drop": "8mm",
                "stackHeight": "42mm",
                "surface": "Road",
                "features": "Подходит для длинных пробежек, отличная амортизация",
                "averagePrice": "$160",
                "reviewScores": {
                    "RunRepeat": 9.1,
                    "BelieveInTheRun": 8.9,
                    "Runner's World": 9.0
                },
                "images": [
                    "https://runrepeat.com/i/asics/65347/asics-gel-nimbus-26-luxury-green-9cf1-mens.jpg"
                ]
            }
        ]
    }
