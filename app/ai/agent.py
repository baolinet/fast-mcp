import openai
from app.core.config import settings
from typing import Generator

class SmartAgent:
    def answer(self, question: str) -> str:
        try:
            client = openai.OpenAI(
                api_key=settings.OPENAI_API_KEY,
                base_url=settings.OPENAI_BASE_URL
            )
            response = client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[{"role": "user", "content": question}],
                temperature=0.7,
                max_tokens=512
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"[OpenAI API 调用失败] {e}"

    def stream_answer(self, question: str) -> Generator[str, None, None]:
        try:
            client = openai.OpenAI(
                api_key=settings.OPENAI_API_KEY,
                base_url=settings.OPENAI_BASE_URL
            )
            stream = client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[{"role": "user", "content": question}],
                temperature=0.7,
                max_tokens=512,
                stream=True
            )
            for chunk in stream:
                if hasattr(chunk.choices[0].delta, "content") and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"[OpenAI API 流式调用失败] {e}"
