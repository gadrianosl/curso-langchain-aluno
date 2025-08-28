
import os
import openai


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

# Carregar variáveis do .env manualmente (robusto)
env = load_env_direct()
api_key = env.get('OPENAI_API_KEY') or os.getenv('OPENAI_API_KEY')

if not api_key:
    print('❌ Erro: OPENAI_API_KEY não encontrada no .env nem no ambiente.')
    raise SystemExit(1)

openai.api_key = api_key

try:
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": "Hello, world!"}]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"❌ Erro ao chamar a API OpenAI: {e}")