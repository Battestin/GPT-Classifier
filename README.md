# GPT Classifier

AI-powered product classifier using OpenAI’s GPT-3.5 Turbo.  
Given a product name, it returns the most suitable category from a predefined list.

## 🚀 How to Run

1. Clone the repo  
2. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` com sua chave de API:  
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Execute o script:  
   ```bash
   python classifier_003.py
   ```

## 🧠 Exemplo

```
Type a list of valid categories separated by commas: Green Electronics, Home Appliances, Toys

Type a product name: Solar rechargeable electric toothbrush

Output:  
  Product: Solar rechargeable electric toothbrush  
  Category: Green Electronics
```

## 🛠️ Customização

Digite sua própria lista de categorias quando solicitado na execução.

## ⚠️ Nota

Este é um protótipo usando LLMs. Sempre valide a saída antes de usar em aplicações reais.

## 📄 Licença

MIT
