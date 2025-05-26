from flask import Flask, render_template, request, jsonify
import aiohttp
import asyncio
from functools import wraps

app = Flask(__name__)

def async_route(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))
    return wrapped

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
@async_route
async def ask():
    """Handle the question submission"""
    try:
        question = request.json.get('question', '')
        if not question:
            return jsonify({'error': 'Question cannot be empty'}), 400

        # Send request to FastAPI backend
        async with aiohttp.ClientSession() as session:
            async with session.post('http://localhost:8000/ask', 
                                  json={'question': question}) as response:
                if response.status == 200:
                    result = await response.json()
                    return jsonify(result)
                else:
                    error_text = await response.text()
                    return jsonify({'error': f'Backend error: {error_text}'}), response.status

    except Exception as e:
        return jsonify({'error': f'Error processing request: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 