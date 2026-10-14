# Experiment 1: Basic Prompt Engineering

from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

prompt = "Say hello to IV B.Tech CSE students in exactly one sentence."

response = client.chat.completions.create(
  model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=100
)

print("USER PROMPT:")
print(prompt)
print("\nMODEL RESPONSE:")
print(response.choices[0].message.content)
import os

os.makedirs("outputs", exist_ok=True)

with open("outputs/output.txt", "w", encoding="utf-8") as f:
    f.write("USER PROMPT:\n")
    f.write(prompt + "\n\n")
    f.write("MODEL RESPONSE:\n")
    f.write(response.choices[0].message.content)
