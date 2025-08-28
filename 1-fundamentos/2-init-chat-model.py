import os
import requests
import json

# Carrega a chave do Gemini do .env (e fallback manual)
def load_env_direct():
    env_vars = {}
    try:
        with open('.env', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    env_vars[key] = value
    except Exception:
        pass
    return env_vars

env = load_env_direct()
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY') or env.get('GOOGLE_API_KEY')

if not GEMINI_API_KEY:
    print('❌ Erro: GOOGLE_API_KEY não encontrada no .env nem no ambiente.')
    raise SystemExit(1)

MODEL = 'gemini-1.5-flash'
BASE_URL = 'https://generativelanguage.googleapis.com/v1beta/models'


def invoke_gemini(message: str) -> str:
    url = f"{BASE_URL}/{MODEL}:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": message}
                ]
            }
        ]
    }
    try:
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if 'candidates' in data and data['candidates']:
            return data['candidates'][0]['content']['parts'][0]['text']
        return 'Erro: Resposta vazia do Gemini.'
    except Exception as e:
        return f'Erro na API Gemini: {e}'


if __name__ == '__main__':
    answer = invoke_gemini('Hello, world!')
    print(answer)