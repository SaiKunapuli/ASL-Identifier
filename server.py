from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/open-python-window', methods=['POST'])
def open_python_window():
    try:
        subprocess.run(['python', 'main.py'])
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
