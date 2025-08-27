
import os
from dotenv import load_dotenv
import openai
import httpx
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
http_client=httpx.Client(verify=False)
)
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[{"role": "user", "content": "Hello, world!"}]
)
print(response.choices[0].message.content)