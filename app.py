from flask import Flask, request, jsonify, render_template
import pyshorteners
from flask_cors import CORS
import os



app = Flask(__name__)
CORS(app)  # Allows frontend requests from different origins

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    long_url = data.get('url')

    if not long_url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        s = pyshorteners.Shortener()
        short_url = s.dagd.short(long_url)
        return jsonify({'short_url': short_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port,debug=True)

