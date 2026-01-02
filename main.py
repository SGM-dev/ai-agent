import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set.")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="ChatBot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

user_prompt = args.user_prompt
messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

print(f"User prompt: {user_prompt}")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
)

if response.usage_metadata:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    raise RuntimeError("Usage metadata is missing.")
print(f"Response: {response.text}")


# def main():
#     print("Hello from ai-agent!")


# if __name__ == "__main__":
#     main()
