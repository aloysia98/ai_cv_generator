import os
from huggingface_hub import InferenceClient

MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"

client = InferenceClient(
    model=MODEL_ID,
    token=os.getenv("HF_TOKEN")
)

def call_llm(prompt: str) -> str:
#     response = client.chat_completion(
#         messages=[
#             {"role": "system", "content": "You are a professional CV optimization assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=900,
#         temperature=0.4,
#     )

    # return response.choices[0].message.content
    response = client.chat_completion(
        messages=[
            {"role": "system", "content": "You are a professional CV optimization assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.65,
        top_p=0.9,
        max_tokens=1200
    )

    return response.choices[0].message.content