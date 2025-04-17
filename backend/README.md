# Random Quote Generator - Backend

This is the Flask backend for the Random Quote Generator app, which uses the Mistral AI API to generate inspirational quotes.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Pip (Python package installer)

### Installation

1. **Create a Virtual Environment**:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**:
   The `.env` file should already contain the Mistral API key:
   ```
   MISTRAL_API_KEY=8lqveCj59so7n1NVXXAWLCTnF8Rizz7M
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```
   The server will start at `http://localhost:5000`.

## API Endpoints

- **GET /quote**: Returns a randomly generated inspirational quote from Mistral AI.
  - Response format: `{"quote": "Your inspirational quote here"}`
  - Error format: `{"error": "Error message"}`

## Troubleshooting

- **CORS Issues**: If you encounter CORS issues, ensure the frontend is running on `http://localhost:3000` as configured in the CORS settings.
- **API Key Issues**: If the API key doesn't work, verify it in the `.env` file and ensure it's being loaded correctly. 