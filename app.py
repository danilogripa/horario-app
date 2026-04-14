from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_DIR  = os.environ.get('DATA_DIR', os.path.dirname(__file__))
DATA_FILE = os.path.join(DATA_DIR, 'schedule.json')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/load')
def load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({})


@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7500, debug=False)
