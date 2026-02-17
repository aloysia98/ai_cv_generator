import os
from huggingface_hub import InferenceClient

MODEL_ID = "HuggingFaceH4/zephyr-7b-beta"

client = InferenceClient(
    model=MODEL_ID,
    token=os.getenv("HF_TOKEN")
)

def call_llm(prompt: str) -> str:
    response = client.text_generation(
        prompt,
        max_new_tokens=900,
        temperature=0.4,
        do_sample=True,
        return_full_text=False
    )

    return response
