from flask import Flask, jsonify, request, send_from_directory
from deforestation_api import fetch_deforestation_data

# Flask app initialization
app = Flask(__name__, static_folder='static')

# Route to serve the index.html file
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# API route to fetch deforestation data
@app.route('/get_deforestation_data')
def get_deforestation_data():
    year = request.args.get('year')

    if not year:
        return jsonify({"error": "Year parameter is missing"}), 400

    # Fetch the deforestation data (mock data in this case)
    try:
        data = fetch_deforestation_data(start_year=year, end_year=year, region='Amazon')
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any errors

if __name__ == '__main__':
    app.run(debug=True)
