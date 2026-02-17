import os
from huggingface_hub import InferenceClient

MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"

client = InferenceClient(
    model=MODEL_ID,
    token=os.getenv("HF_TOKEN")
)

def call_llm(prompt: str) -> str:
    response = client.chat_completion(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        top_p=0.9,
        repetition_penalty=1.1,
        max_tokens=1200
    )

    return response.choices[0].message.content