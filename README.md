# GPT Classifier

AI-powered product classifier using OpenAI’s GPT-3.5 Turbo.  
Given a product name, it returns the most suitable category from a predefined list.

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:  
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Run the script:  
   ```bash
   python classifier_003.py
   ```

## 🧠 Example

```
Type a list of valid categories separated by commas: Green Electronics, Home Appliances, Toys

Type a product name: Solar rechargeable electric toothbrush

Output:  
  Product: Solar rechargeable electric toothbrush  
  Category: Green Electronics
```

## 🛠️ Customization

Enter your own category list when prompted at runtime.

## ⚠️ Note

This is a prototype using LLMs. Always validate the output before using it in real applications.

## 📄 License

MIT
