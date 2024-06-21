from config import GOOGLE_API_TOKEN
import requests
import json

def get_ai_response(prompt):
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                ]
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }

    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GOOGLE_API_TOKEN}'

    proxies = {
        'http': '210.87.125.150:1111',
        'https': '210.87.125.150:1111',
    }

    response = requests.post(url, json=data, headers=headers, proxies=proxies)

    return response

if __name__ == '__main__':
    print(get_ai_response("Hello, how are you?").text)