@app.post("/gpt")
async def ask_gpt(request: Request):
    body = await request.json()
    prompt = body.get("prompt")

    if not prompt:
        return {"error": "❌ Prompt is missing!"}

    print("📨 Получен prompt:", prompt)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        answer = response.choices[0].message["content"]
        return {"response": answer}
    except Exception as e:
        print("🚨 Ошибка GPT:", str(e))
        return {"error": f"⚠️ Ошибка GPT: {str(e)}"}
