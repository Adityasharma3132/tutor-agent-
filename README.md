# Multi-Agent Tutoring Bot

A multi-agent system that uses the Gemini API to provide tutoring assistance in Math and Physics subjects.

## Features

- Main Tutor Agent that delegates questions to specialized sub-agents
- Math Agent with calculator functionality
- Physics Agent with physics constants lookup
- FastAPI backend with web interface
- Gemini API integration for natural language processing

## Prerequisites

- Python 3.8 or higher
- Gemini API key (Get it from [Google MakerSuite](https://makersuite.google.com/app/apikey))

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory:
   ```bash
   # On Windows
   copy .env.example .env

   # On macOS/Linux
   cp .env.example .env
   ```

5. Edit the `.env` file and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Starting the Application

### Local Development
1. Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Open your browser and navigate to:
   - Web Interface: [http://localhost:8000](http://localhost:8000)
   - API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

### Railway Deployment

1. Fork/Push your code to GitHub

2. Create a new project on [Railway](https://railway.app/)

3. Connect your GitHub repository

4. Add the following environment variable in Railway:
   - `GEMINI_API_KEY`: Your Gemini API key

5. Railway will automatically detect the Procfile and deploy your application

6. Your application will be available at the URL provided by Railway

## Usage

1. Through the Web Interface:
   - Visit http://localhost:8000 (or your Railway URL)
   - Type your math or physics question in the text area
   - Click "Ask Question" or try one of the example questions

2. Through the API:
   ```bash
   # Replace {YOUR_APP_URL} with localhost:8000 or your Railway URL
   curl -X POST "{YOUR_APP_URL}/ask" \
        -H "Content-Type: application/json" \
        -d '{"question": "What is the speed of light?"}'
   ```

## Project Structure

```
.
├── app/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── tutor_agent.py
│   │   ├── math_agent.py
│   │   └── physics_agent.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── calculator.py
│   │   └── constants.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── gemini.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   ├── templates/
│   │   └── index.html
│   └── main.py
├── .env.example
├── .gitignore
├── Procfile
├── requirements.txt
└── README.md
```

## Development

- The application uses FastAPI for both the backend API and serving the web interface
- Templates are located in `app/templates/`
- Static files (CSS, JavaScript) are in `app/static/`
- The Gemini API is used for natural language processing and question classification

## Troubleshooting

1. If you see a "GEMINI_API_KEY not found" error:
   - Make sure you've created the `.env` file
   - Verify your API key is correctly set in the `.env` file
   - Ensure the `.env` file is in the root directory

2. If static files aren't loading:
   - Check that the `app/static/` directory exists
   - Verify file permissions
   - Clear your browser cache

3. If the server won't start:
   - Verify all dependencies are installed
   - Check if another process is using port 8000
   - Ensure Python 3.8 or higher is installed

4. Railway Deployment Issues:
   - Ensure Procfile exists in the root directory
   - Check if GEMINI_API_KEY is set in Railway environment variables
   - Verify the application logs in Railway dashboard for specific errors 