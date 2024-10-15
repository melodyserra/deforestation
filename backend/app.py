from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='')

# Serve index.html from static folder
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Other API routes
@app.route('/get_deforestation_data')
def get_deforestation_data():
    year = request.args.get('year')
    # Mocked response for testing
    data = {
        "deforestation_areas": [
            {"lat": -3.4653, "lon": -62.2159, "deforested_hectares": 1200}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
