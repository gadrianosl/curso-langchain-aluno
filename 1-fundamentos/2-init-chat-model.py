from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import httpx
load_dotenv()

gemini = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai",
    client=httpx.Client(verify=False)
)
answer_gemini = gemini.invoke("Hello, world!")
print(answer_gemini.content)