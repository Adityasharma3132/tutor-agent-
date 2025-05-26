# Multi-Agent Tutoring Bot

A multi-agent system that uses the Gemini API to provide tutoring assistance in Math and Physics subjects.

## Features

- Main Tutor Agent that delegates questions to specialized sub-agents
- Math Agent with calculator functionality
- Physics Agent with physics constants lookup
- FastAPI backend with /ask endpoint
- Gemini API integration for natural language processing

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
5. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

Send a POST request to `/ask` endpoint with your question:

```bash
curl -X POST "http://localhost:8000/ask" \
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
│   └── main.py
├── .env
├── requirements.txt
└── README.md
``` 