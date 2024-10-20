import requests

def fetch_deforestation_data(start_year, end_year, region):
    # Replace this with the actual NASA or GFW API endpoint
    api_url = f"https://api.deforestationdata.org/deforestation?start_year={start_year}&end_year={end_year}&region={region}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data: {response.status_code}")
    except Exception as e:
        raise Exception(f"API request failed: {str(e)}")
