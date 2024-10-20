from flask import Flask, jsonify, request, send_from_directory
import requests

app = Flask(__name__, static_folder='static', static_url_path='')

# Replace with your GFW API URL and token
GFW_API_URL = "https://data-api.globalforestwatch.org/deforestation-alerts"
API_TOKEN = "YOUR_GFW_API_TOKEN"

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Route to fetch deforestation data
@app.route('/get_deforestation_data')
def get_deforestation_data():
    year = request.args.get('year')

    if not year:
        return jsonify({"error": "Year parameter is missing"}), 400

    try:
        # Fetch data from the GFW API
        response = requests.get(
            GFW_API_URL,
            params={
                'start_year': year,
                'end_year': year,
                'geostore': 'amazon-basin',  # Replace with actual geostore or region
                'token': API_TOKEN
            }
        )
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": f"Error fetching data from API: {response.status_code}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
