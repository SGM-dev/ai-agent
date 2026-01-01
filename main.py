import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set.")

client = genai.Client(api_key=api_key)


user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

print(f"User prompt: {user_prompt}")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_prompt,
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
