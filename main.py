from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем запросы с GitHub Pages
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
        <h1>👟 Welcome to Jogging GPT!</h1>
        <p>⚙️ Сервер запущен в тестовом режиме (без GPT)</p>
      </body>
    </html>
    """

@app.post("/gpt")
async def fake_response(request: Request):
    body = await request.json()
    prompt = body.get("prompt")

    if not prompt:
        return {"error": "❌ Prompt is missing"}

    print("📥 Получен запрос (мок):", prompt)

    # Возвращаем фиктивные результаты (пример)
    fake_shoes = [
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
        },
        {
            "brand": "Hoka",
            "model": "Clifton 9",
            "year": "2024",
            "weight": "248g",
            "cushioning": "Moderate",
            "drop": "5mm",
            "stackHeight": "38mm",
            "surface": "Road",
            "features": "Легкие, универсальные для повседневных пробежек",
            "averagePrice": "$140",
            "reviewScores": {
                "RunRepeat": 8.7,
                "BelieveInTheRun": 8.5,
                "Runner's World": 8.9
            },
            "images": [
                "https://runrepeat.com/i/hoka-one-one/63962/hoka-clifton-9-ultimate-gray-pink-sand-womens.jpg"
            ]
        }
    ]

    return {"response": fake_shoes}
