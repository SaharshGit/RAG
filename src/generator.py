import os

from dotenv import load_dotenv

load_dotenv()

# Select provider with LLM_PROVIDER in .env: "sarvam" (default) or "azure"
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_MODEL = os.getenv("AZURE_MODEL")
SARVAM_MODEL = os.getenv("SARVAM_MODEL", "sarvam-105b")


class Generator:

    def __init__(self):

        self.provider = os.getenv("LLM_PROVIDER", "sarvam").lower()

        if self.provider == "sarvam":
            from sarvamai import SarvamAI

            api_key = os.getenv("sarvam_api_key")

            if not api_key:
                raise ValueError("NO API KEY SET")

            self.client = SarvamAI(
                api_subscription_key=api_key
            )

        elif self.provider == "azure":
            from openai import OpenAI

            azure_api_key = os.getenv("AZURE_API_KEY")

            if not AZURE_ENDPOINT or not AZURE_MODEL or not azure_api_key:
                raise ValueError(
                    "AZURE_ENDPOINT, AZURE_MODEL and AZURE_API_KEY must be set in .env"
                )

            self.client = OpenAI(
                base_url=AZURE_ENDPOINT,
                api_key=azure_api_key
            )

        else:
            raise ValueError(f"Unknown LLM_PROVIDER: {self.provider}")

    def generate(self, query: str, context: str) -> str:

        prompt = f"""
Answer the question using only the provided context.

If the answer cannot be found in the provided context, say:
"I don't know based on the provided context."

Context:
{context}

Question:
{query}
"""
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        if self.provider == "sarvam":
            response = self.client.chat.completions(
                model=SARVAM_MODEL,
                messages=messages,
                temperature=0.2,
                max_tokens=500,
                reasoning_effort=None,
            )
        else:
            response = self.client.chat.completions.create(
                model=AZURE_MODEL,
                messages=messages,
        
                temperature=0.8,
                top_p=0.95,
                max_tokens=4000,
            )

        return response.choices[0].message.content
