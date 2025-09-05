from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import json

app = Flask(__name__)
CORS(app)

# Groq API (not Grok)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # This is correct for Groq

def get_groq_response(message):
    """Get response from Groq API"""
    if not GROQ_API_KEY:
        return "Error: API key not configured."
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama3-8b-8192",  # Valid Groq model
        "messages": [
            {
                "role": "system", 
                "content": "You are AquaAdvisor, a water quality expert. Provide practical advice about pH levels (6.5-8.5 ideal), TDS values, and water purification methods. Keep responses under 100 words."
            },
            {
                "role": "user", 
                "content": message
            }
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:200]}...")  # Debug
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            return f"API Error: HTTP {response.status_code}. Response: {response.text}"
            
    except Exception as e:
        print(f"Error: {e}")
        return f"Connection error: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')
        
        if not message:
            return jsonify({'response': 'Please provide a message', 'session_id': session_id}), 400
        
        response_text = get_groq_response(message)
        return jsonify({
            'response': response_text,
            'session_id': session_id
        })
        
    except Exception as e:
        return jsonify({
            'response': f'Server error: {str(e)}',
            'session_id': 'error'
        }), 500

@app.route('/')
def home():
    return jsonify({
        "message": "🌊 AquaAdvisor AI Agent is running!",
        "version": "1.0",
        "endpoints": {
            "chat": "/chat (POST)",
            "health": "/health (GET)"
        }
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "agent": "AquaAdvisor",
        "timestamp": "2025-09-05",
        "api_key_configured": bool(GROQ_API_KEY)
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)
    
