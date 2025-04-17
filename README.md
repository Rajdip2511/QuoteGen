# Random Quote Generator

A web application that generates inspirational quotes using the Mistral AI API. The application consists of a Flask backend and a Next.js frontend with Shadcn UI components.

## Project Structure

```
random-quote-generator/
├── backend/               # Flask API to generate quotes
│   ├── app.py             # Flask app with /quote endpoint
│   ├── requirements.txt   # Python dependencies
│   ├── .env               # Stores MISTRAL_API_KEY
│   └── README.md          # Backend setup instructions
├── frontend/              # Next.js frontend
│   ├── src/               
│   │   ├── app/           # Next.js App Router
│   │   ├── components/    # React components
│   │   └── lib/           # Utility functions
│   ├── package.json       # Node dependencies
│   ├── .env.local         # Stores backend API URL
│   └── README.md          # Frontend setup instructions
└── README.md              # This file
```

## Setup Instructions

### Step 1: Set up the Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```
   The backend will be available at `http://localhost:5000`.

### Step 2: Set up the Frontend

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:3000`.

## Features

- **Backend**: Flask API that calls Mistral AI to generate inspirational quotes
- **Frontend**: Modern UI with Shadcn UI components
- **Responsive Design**: Works on both mobile and desktop
- **Error Handling**: Proper error states for API failures

## Technologies Used

- **Backend**: 
  - Flask (Python web framework)
  - Mistral AI API for quote generation
  
- **Frontend**:
  - Next.js 14 (React framework)
  - Shadcn UI (UI component library)
  - Tailwind CSS (Utility-first CSS framework)
  - TypeScript (Type-safe JavaScript)

## API Key

The application uses the Mistral AI API with the following key (already included in `.env`):
```
MISTRAL_API_KEY=8lqveCj59so7n1NVXXAWLCTnF8Rizz7M
```

## Troubleshooting

- **CORS Issues**: If you encounter CORS issues, ensure both servers are running and the frontend is requesting from `http://localhost:5000`.
- **API Key Issues**: If the API key doesn't work, check the Mistral AI documentation for any changes to their authentication system.

## Future Enhancements

- Add the ability to save favorite quotes
- Implement different quote categories
- Add social media sharing functionality 