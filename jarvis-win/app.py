from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Ana Sayfa
@app.route('/')
def home():
    return render_template('index.html')

# Örnek API
@app.route('/api/test')
def test_api():
    return jsonify({
        'status': 'success',
        'message': 'Flask API çalışıyor'
    })

# POST örneği
@app.route('/api/message', methods=['POST'])
def message():
    data = request.json

    return jsonify({
        'received': data
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)