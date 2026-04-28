import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = ""

def analyze_habits(data):

    prompt = f"""
You are an AI productivity coach.

Analyze these habits:

{data}

Provide:
1. Consistency analysis
2. Positive habits
3. Areas to improve
4. Motivational advice

Keep it simple and practical.
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    return result["choices"][0]["message"]["content"]