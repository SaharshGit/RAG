import os

from sarvamai import SarvamAI

from dotenv import load_dotenv

load_dotenv()

class Generator:

    def __init__(self):

        api_key = os.getenv("sarvam_api_key")

        if not api_key:
            raise ValueError("NO API KEY SET")

        self.client = SarvamAI(
            api_subscription_key=api_key
        )

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
        response = self.client.chat.completions(
            model="sarvam-105b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=500,
            reasoning_effort=None,

        )

        return response.choices[0].message.content
