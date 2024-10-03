from flask import Flask, jsonify, request
from deforestation_api import fetch_deforestation_data

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/get_deforestation_data')
def get_deforestation_data():
    year = request.args.get('year')
    region = request.args.get('region', 'Amazon')  # Default to Amazon if no region is provided
    data = fetch_deforestation_data(start_year=year, end_year=year, region=region)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
