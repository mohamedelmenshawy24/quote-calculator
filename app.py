from flask import Flask, request, jsonify

app = Flask(__name__)


def calculate_quote(base_price, markup_percent):
    """Calculate price after adding markup."""
    if base_price < 0 or markup_percent < -100:
        raise ValueError("Invalid base price or markup")
    return base_price * (1 + markup_percent / 100)


@app.route('/quote', methods=['POST'])
def quote():
    data = request.get_json()
    base_price = data.get('base_price')
    markup_percent = data.get('markup_percent')

    if base_price is None or markup_percent is None:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        result = calculate_quote(float(base_price), float(markup_percent))
        return jsonify({'quote': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
