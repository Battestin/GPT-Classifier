from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-3.5-turbo"

def classify_product(product_name, list_possible_categories):

    system_prompt = f"""
        You are a product categorizer.
        You must use the categories present in the list below.

        # List of Valid Categories
        {list_possible_categories.split(",")}

        # Output Format
        Product: Product Name
        Category: present the product's category

        # Example Output
        Product: Solar rechargeable electric toothbrush
        Category: Green Electronics
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {   
                "role": "system", 
                "content": system_prompt
            },  
            {
                "role": "user", 
                "content": product_name
            } 
        ],
        temperature=0, # 0.0 = deterministic, 1.0 = random
        max_tokens=200  # max number of tokens to generate
    )

    return response.choices[0].message.content

valid_categories = input("Type a list of valid categories separated by commas: ")

while True:
    product_name = input("Type a product name: ")
    repsonse_text = classify_product(product_name, valid_categories)
    print(f"\n{repsonse_text}")

    