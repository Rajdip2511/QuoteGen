# Random Quote Generator - Frontend

This is the Next.js frontend for the Random Quote Generator app, which displays inspirational quotes fetched from the Flask backend.

## Setup Instructions

### Prerequisites
- Node.js 18 or higher
- npm (Node package manager)

### Installation

1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Set up Environment Variables**:
   The `.env.local` file should already contain the backend API URL:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:5000
   ```

3. **Run the Development Server**:
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:3000`.

## Features

- Modern UI with Shadcn UI components
- Displays inspirational quotes from Mistral AI
- Responsive design that works on both mobile and desktop
- Loading and error states for better user experience

## Components

- **QuoteCard**: Displays the quote, loading state, and refresh button
- **UI Components**: Using Shadcn UI for Button and Card components

## Troubleshooting

- **API Connection Issues**: Ensure the backend server is running at `http://localhost:5000`.
- **CORS Errors**: The backend should have CORS configured to allow requests from `http://localhost:3000`.
- **Dependencies Issues**: If you encounter any issues with dependencies, try running `npm install` again.

## Building for Production

To build the app for production:

```bash
npm run build
npm start
``` 