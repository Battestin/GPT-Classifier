from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model = "gpt-3.5-turbo"
system_prompt = """
    You are a product categorizer.
    You must use the categories present in the list below.

    # List of Valid Categories
        - Sustainable Fashion
        - Home Products
        - Natural Beauty
        - Green Electronics
        - Personal Hygiene

    # Output Format
    Product: Product Name
    Category: present the product's category

    # Example Output
    Product: Solar rechargeable electric toothbrush
    Category: Green Electronics
"""
user_prompt = input("Type a product name: ")

response = client.chat.completions.create(
    model=model,
    messages=[
        {   
            "role": "system", 
            "content": system_prompt
        },  
        {
            "role": "user", 
            "content": user_prompt
        } 
    ],
    temperature=0, # 0.0 = deterministic, 1.0 = random
    max_tokens=200  # max number of tokens to generate
)

print(f"\n{response.choices[0].message.content}")
    