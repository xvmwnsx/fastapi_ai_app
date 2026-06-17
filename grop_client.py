
from openai import OpenAI
from config import config_obj
client = OpenAI(
    api_key=config_obj.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

def get_response(input: str):
    response = client.responses.create(
        input=input,
        model="openai/gpt-oss-20b",
    )
    return response.output_text

# if __name__ == '__main__':
#     print(get_response("Hello"))