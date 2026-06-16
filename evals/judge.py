from deepeval.models import DeepEvalBaseLLM


class AnthropicJudge(DeepEvalBaseLLM):
    """Custom DeepEval judge that uses Claude instead of OpenAI."""

    def __init__(self, model_name: str = "claude-sonnet-4-6"):
        self._model_name = model_name
        self._client = None

    def load_model(self):
        if self._client is None:
            import anthropic

            self._client = anthropic.Anthropic()
        return self._client

    def generate(self, prompt: str, schema=None, **kwargs) -> str:
        client = self.load_model()
        msg = client.messages.create(
            model=self._model_name,
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )
        text = msg.content[0].text

        if schema:
            import json

            # DeepEval may request structured output; try to extract JSON
            try:
                # Try parsing the whole response as JSON
                json.loads(text)
                return text
            except json.JSONDecodeError:
                # Try extracting JSON from markdown code blocks
                for block in text.split("```"):
                    block = block.strip()
                    if block.startswith("json"):
                        block = block[4:].strip()
                    try:
                        json.loads(block)
                        return block
                    except json.JSONDecodeError:
                        continue
                return text

        return text

    async def a_generate(self, prompt: str, schema=None, **kwargs) -> str:
        return self.generate(prompt, schema=schema, **kwargs)

    def get_model_name(self) -> str:
        return self._model_name
