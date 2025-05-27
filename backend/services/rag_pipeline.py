import openai
from backend.config import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_VERSION, AZURE_OPENAI_DEPLOYMENT

openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = AZURE_OPENAI_VERSION
openai.api_key = AZURE_OPENAI_KEY

def run_rag_pipeline(query):
    response = openai.ChatCompletion.create(
        engine=AZURE_OPENAI_DEPLOYMENT,
        messages=[{"role": "user", "content": query}],
        temperature=0.5,
        max_tokens=200
    )
    return response.choices[0].message['content']
