import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def test_mistral_api():
    print("Testing Mistral AI API...")
    print(f"API Key: {MISTRAL_API_KEY[:5]}...{MISTRAL_API_KEY[-4:]} (shortened for security)")
    
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "mistral-small-latest",
        "messages": [
            {"role": "user", "content": "Generate a short test quote"}
        ],
        "max_tokens": 50
    }
    
    try:
        print("Sending request to Mistral AI...")
        response = requests.post(MISTRAL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        quote = result['choices'][0]['message']['content']
        print("Success! Received response:")
        print(f"Quote: {quote}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"API error: {str(e)}")
        if hasattr(e, 'response') and e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response text: {e.response.text}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    test_mistral_api() 