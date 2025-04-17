import os
import requests
import random
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
# Enable CORS for requests from frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

# List of different prompt templates to get varied quotes
PROMPT_TEMPLATES = [
    "Generate a specific, inspirational quote (max 50 words) about overcoming challenges. Don't include any introductory text, just the quote itself.",
    "Create a unique, motivational quote (max 50 words) about personal growth. Return just the quote with no additional text.",
    "Write a powerful, meaningful quote (max 50 words) about achieving goals. Only include the quote itself.",
    "Provide an uplifting, encouraging quote (max 50 words) about finding happiness. Only return the quote text.",
    "Create a thoughtful quote (max 50 words) about perseverance. Skip any introductory phrases and only give the quote.",
    "Generate a unique, inspiring quote (max 50 words) about success. Return only the quote without any additional text.",
    "Write a meaningful quote (max 50 words) about taking risks. Provide just the quote text.",
    "Create a powerful quote (max 50 words) about self-belief. Return only the quote with no other text."
]

@app.route('/quote', methods=['GET'])
def get_quote():
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Add randomness to the prompt
    random_number = random.randint(1, 10000)
    current_time = datetime.now().strftime("%H:%M:%S")
    selected_prompt = random.choice(PROMPT_TEMPLATES)
    
    # Include the random elements in the prompt to ensure different responses
    prompt = f"{selected_prompt} (Request ID: {random_number}, Time: {current_time})"
    
    data = {
        "model": "mistral-small-latest",
        "messages": [
            {"role": "system", "content": "You are a quote generator that only returns inspirational quotes. Never include any additional text, explanations, or prefixes like 'Here's a quote:'. Just provide the quote text itself."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 100,
        "temperature": 0.7  # Add some randomness to the generation
    }
    
    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        
        quote_text = response.json()['choices'][0]['message']['content'].strip()
        
        # Remove any "Here's a quote:" or similar prefix text
        prefixes_to_remove = [
            "here's a quote:", "here is a quote:", "sure,", "certainly,", 
            "here you go:", "of course,", "here's an inspirational quote:",
            "here is an inspirational quote:"
        ]
        
        lower_quote = quote_text.lower()
        for prefix in prefixes_to_remove:
            if lower_quote.startswith(prefix):
                quote_text = quote_text[len(prefix):].strip()
        
        # Remove any quotation marks that might be in the response
        quote_text = quote_text.strip('"\'')
        
        return jsonify({"quote": quote_text})
    
    except requests.exceptions.RequestException as e:
        app.logger.error(f"API error: {str(e)}")
        if hasattr(e, 'response') and e.response:
            app.logger.error(f"Response status code: {e.response.status_code}")
            app.logger.error(f"Response text: {e.response.text}")
        return jsonify({"error": f"API error: {str(e)}"}), 500
    except (KeyError, IndexError) as e:
        app.logger.error(f"Error parsing response: {str(e)}")
        return jsonify({"error": f"Error parsing response: {str(e)}"}), 500
    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 