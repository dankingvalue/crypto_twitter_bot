"""Flask app for health checks"""
from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'service': 'Crypto Twitter Bot',
        'status': 'online',
        'message': 'Bot is running 🚀'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'message': '✅ Bot is alive'
    })

@app.route('/wake')
def wake():
    return jsonify({'status': 'awake'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
