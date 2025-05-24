from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {   
            "role": "system", 
            "content": """
            Rate the product below in one of the categories: Personal Care, Fashion or Home from a category description.
            """
        },  
        {
            "role": "user", 
            "content": """
            Bamboo Toothbrush
            """
        } 
    ]
)

#print(f"\n{response}")
#print(f"\n{response.choices[0].message.content}")

for contador in range(0,3):
    print(f"\n{response.choices[contador].message.content}")