import requests

# Function to fetch deforestation data
def fetch_deforestation_data(start_year, end_year, region):
    # NASA Earthdata API call (replace with actual endpoint and query params)
    url = f'https://earthdata.nasa.gov/api/deforestation?start_year={start_year}&end_year={end_year}&region={region}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return JSON data
    else:
        return {'error': 'Failed to fetch data'}
