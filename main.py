import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

# 💬 Обрабатываем POST-запрос с анкетой
@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.json
        prompt = generate_prompt(data)

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты профессиональный консультант по беговым кроссовкам. Используй только модели 2024–2025 годов, с учетом пола, стиля бега и предпочтений пользователя."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        reply = response.choices[0].message.content
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def generate_prompt(data):
    # 🧠 Собираем все ответы пользователя
    lines = ["Вот анкета пользователя:\n"]
    for key, value in data.items():
        lines.append(f"{key}: {value}")
    lines.append("\nПредложи 3–5 лучших моделей кроссовок с кратким описанием.")
    return "\n".join(lines)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
